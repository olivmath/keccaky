from Crypto.Hash import keccak as pycryptodome_keccak
from keccaky import hash_it_bytes
from pytest import mark

KAT = []

with open("./tests/pycryptodome/CompareMsgKAT_256.txt", "r") as file:
    lines = file.readlines()

    for msg in lines:
        data = bytes.fromhex(msg.split("=")[1].strip().lower())
        KAT.append(data)


@mark.parametrize("data", KAT)
def test_compare_msg_pycryptodome(data: bytes):
    # PY_CRYPTODOME
    pycryptodome = pycryptodome_keccak.new(digest_bits=256)
    pycryptodome.update(data)
    result_pycryptodome = pycryptodome.digest()

    # KECCAKY
    result_keccaky = hash_it_bytes(data)

    assert result_keccaky == result_pycryptodome
