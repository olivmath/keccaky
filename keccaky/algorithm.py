from math import log
from operator import xor
from copy import deepcopy
import functools


RoundConstants = [
    0x0000000000000001,
    0x0000000000008082,
    0x800000000000808A,
    0x8000000080008000,
    0x000000000000808B,
    0x0000000080000001,
    0x8000000080008081,
    0x8000000000008009,
    0x000000000000008A,
    0x0000000000000088,
    0x0000000080008009,
    0x000000008000000A,
    0x000000008000808B,
    0x800000000000008B,
    0x8000000000008089,
    0x8000000000008003,
    0x8000000000008002,
    0x8000000000000080,
    0x000000000000800A,
    0x800000008000000A,
    0x8000000080008081,
    0x8000000000008080,
    0x0000000080000001,
    0x8000000080008008,
]

RotationConstants = [
    [
        0,
        1,
        62,
        28,
        27,
    ],
    [
        36,
        44,
        6,
        55,
        20,
    ],
    [
        3,
        10,
        43,
        25,
        39,
    ],
    [
        41,
        45,
        15,
        21,
        8,
    ],
    [
        18,
        2,
        61,
        56,
        14,
    ],
]

Masks = [(1 << i) - 1 for i in range(65)]


def rol(value, left, bits):
    top = value >> (bits - left)
    bot = (value & Masks[bits - left]) << left
    return bot | top


def ror(value, right, bits):
    top = value >> right
    bot = (value & Masks[right]) << (bits - right)
    return bot | top


class KeccakState(object):
    W = 5
    H = 5

    rangeW = range(W)
    rangeH = range(H)

    def __init__(self, bitrate, b):
        self.bitrate = bitrate
        self.b = b

        # only byte-aligned
        if self.bitrate % 8 != 0:
            raise ValueError(f"bitrate must be multiple of 8, bitrate: {self.bitrate}")
        self.bitrate_bytes = self.__bits2bytes(self.bitrate)

        if self.b % 25 != 0:
            raise ValueError(f"bitrate must be multiple of 25, bitrate: {self.bitrate}")
        self.lanew = self.b // 25

        self.s = KeccakState.zero()

    def __bits2bytes(self, x):
        return (int(x) + 7) // 8

    @staticmethod
    def zero():
        return [[0] * KeccakState.W for x in KeccakState.rangeH]

    @staticmethod
    def format(st):
        rows = []

        def fmt(x):
            return "%016x" % x

        for y in KeccakState.rangeH:
            row = []
            for x in rangeW:
                row.append(fmt(st[x][y]))
            rows.append(" ".join(row))
        return "\n".join(rows)

    @staticmethod
    def lane2bytes(s, w):
        o = []
        for b in range(0, w, 8):
            o.append((s >> b) & 0xFF)
        return o

    @staticmethod
    def bytes2lane(bb):
        r = 0
        for b in reversed(bb):
            r = r << 8 | b
        return r

    def __str__(self):
        return KeccakState.format(self.s)

    def absorb(self, bb):
        if len(bb) != self.bitrate_bytes:
            msg = f"length of bb ({len(bb)}) must be equal bitrate_bytes ({self.bitrate_bytes})"
            raise ValueError(msg)

        bb += [0] * int(self.__bits2bytes(self.b - self.bitrate))
        i = 0

        for y in self.rangeH:
            for x in self.rangeW:
                self.s[x][y] ^= KeccakState.bytes2lane(bb[i : i + 8])
                i += 8

    def squeeze(self):
        return self.get_bytes()[: self.bitrate_bytes]

    def get_bytes(self):
        out = [0] * int(self.__bits2bytes(self.b))
        i = 0
        for y in self.rangeH:
            for x in self.rangeW:
                v = KeccakState.lane2bytes(self.s[x][y], self.lanew)
                out[i : i + 8] = v
                i += 8
        return out

    def set_bytes(self, bb):
        i = 0
        for y in self.rangeH:
            for x in self.rangeW:
                self.s[x][y] = KeccakState.bytes2lane(bb[i : i + 8])
                i += 8


class KeccakSponge(object):
    def __init__(self, bitrate, width, padfn, permfn):
        self.state = KeccakState(bitrate, width)
        self.padfn = padfn
        self.permfn = permfn
        self.buffer = []

    def copy(self):
        return deepcopy(self)

    def absorb_block(self, bb):
        self.state.bitrate_bytes = int(self.state.bitrate_bytes)
        if len(bb) != self.state.bitrate_bytes:
            msg = f"length of bb ({len(bb)}) must be equal to bitrate_bytes ({self.state.bitrate_bytes})"
            raise ValueError(msg)

        self.state.absorb(bb)
        self.permfn(self.state)

    def absorb(self, s):
        self.buffer = list(s)

        while len(self.buffer) >= self.state.bitrate_bytes:
            self.absorb_block(self.buffer[: self.state.bitrate_bytes])
            self.buffer = self.buffer[self.state.bitrate_bytes :]

    def absorb_final(self):
        padded = self.buffer + self.padfn(len(self.buffer), self.state.bitrate_bytes)
        self.absorb_block(padded)
        self.buffer = []

    def squeeze_once(self):
        rc = self.state.squeeze()
        self.permfn(self.state)
        return rc

    def squeeze(self, l):
        Z = self.squeeze_once()
        while len(Z) < l:
            Z += self.squeeze_once()
        return Z[: int(l)]


class Keccak(object):
    def __init__(self, bitrate_bits=1088, capacity_bits=512, digest_bits=256):
        self.sponge = KeccakSponge(
            bitrate_bits,
            bitrate_bits + capacity_bits,
            self.__multirate_padding,
            self.__keccak_f,
        )
        self.digest_size = self.__bits2bytes(digest_bits)
        self.block_size = self.__bits2bytes(bitrate_bits)

    def __bits2bytes(self, x):
        return (int(x) + 7) / 8

    def __round(self, state, A, RC):
        W, H = state.W, state.H
        rangeW, rangeH = state.rangeW, state.rangeH
        lanew = state.lanew
        zero = state.zero

        # theta
        C = [functools.reduce(xor, A[x]) for x in rangeW]
        D = [0] * W
        for x in rangeW:
            D[x] = C[(x - 1) % W] ^ rol(C[(x + 1) % W], 1, lanew)
            for y in rangeH:
                A[x][y] ^= D[x]

        # rho and pi
        B = zero()
        for x in rangeW:
            for y in rangeH:
                B[y % W][(2 * x + 3 * y) % H] = rol(
                    A[x][y], RotationConstants[y][x], lanew
                )

        # chi
        for x in rangeW:
            for y in rangeH:
                A[x][y] = B[x][y] ^ ((~B[(x + 1) % W][y]) & B[(x + 2) % W][y])

        # iota
        A[0][0] ^= RC

    def __keccak_f(self, state):
        l = int(log(state.lanew, 2))
        nr = 12 + 2 * l

        for ir in range(nr):
            self.__round(state, state.s, RoundConstants[ir])

    def __multirate_padding(self, used_bytes, align_bytes):
        padlen = align_bytes - used_bytes
        if padlen == 0:
            padlen = align_bytes
        # note: padding done in 'internal bit ordering', wherein LSB is leftmost
        if padlen == 1:
            return [0x81]
        else:
            return [0x01] + ([0x00] * (int(padlen) - 2)) + [0x80]

    def __repr__(self):
        inf = (
            self.sponge.state.bitrate,
            self.sponge.state.b - self.sponge.state.bitrate,
            self.digest_size * 8,
        )
        return "<KeccakHash with r=%d, c=%d, image=%d>" % inf

    def digest(self, data: bytes) -> bytes:
        self.sponge.absorb(data)
        finalised = self.sponge.copy()
        finalised.absorb_final()
        digest = finalised.squeeze(self.digest_size)
        return bytes(digest)
