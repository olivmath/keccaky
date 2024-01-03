from pytest import mark
from keccaky import Keccaky
from Crypto.Hash import keccak as pycryptodome_keccak

KAT = []
with open("./tests/keccaky/pycryptodome/CompareMsgKAT_256.txt", "r") as file:
    lines = file.readlines()

    for i in range(0, len(lines), 3):
        KAT.append(bytes.fromhex(lines[i].split("=")[1].strip()))


@mark.parametrize("data", KAT)
def test_compare_msg_pycryptodome(data: bytes):
    keccaky = Keccaky()
    pycryptodome = pycryptodome_keccak.new(digest_bits=256)

    # PY_CRYPTODOME
    pycryptodome.update(data)
    result_pycryptodome = pycryptodome.digest()

    # KECCAKY
    result_keccaky = keccaky.digest(data)

    assert result_keccaky == result_pycryptodome

test_compare_msg_pycryptodome(KAT)