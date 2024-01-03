from Crypto.Hash import keccak as cryptodome_keccak
from keccaky import Keccaky
import pytest


def keccaky_hash():
    k = Keccaky()
    result = k.digest("keccaky".encode())
    total_iterations = 1000
    for _ in range(total_iterations):
        result = k.digest(result)
    return result.hex()

def pycryptodome_hash():
    keccak_256 = cryptodome_keccak.new(digest_bits=256)
    keccak_256.update("keccaky".encode())
    result = keccak_256.digest()
    total_iterations = 1000
    for _ in range(total_iterations):
        keccak_256 = cryptodome_keccak.new(digest_bits=256)
        keccak_256.update(result)
        result = keccak_256.digest()
    return result.hex()

@pytest.mark.benchmark(group="KeccakyHash")
def test_keccaky_hash_speed(benchmark):
    result = benchmark(keccaky_hash)
    assert result == "8e9efbfab4a6693f61778ca0cc7401af1685912f7ffb4dc946eae43b4384dc14"

@pytest.mark.benchmark(group="PyCryptodomeHash")
def test_pycryptodome_hash_speed(benchmark):
    result = benchmark(pycryptodome_hash)
    assert result == "8e9efbfab4a6693f61778ca0cc7401af1685912f7ffb4dc946eae43b4384dc14"
