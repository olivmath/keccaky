from Crypto.Hash import keccak as pycryptodome_keccak
from keccaky import Keccaky
from pytest import mark

KAT = []

with open("./tests/pycryptodome/CompareMsgKAT_256.txt", "r") as file:
    lines = file.readlines()

    for msg in lines:
        data = bytes.fromhex(msg.split("=")[1].strip().lower())
        KAT.append(data)


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
