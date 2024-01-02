import keccaky
from keccaky.wip import KeccakHash


def test_mock_result():
    msg = "Hello, world"
    result = "db99debe7fc546756227481ecaf5136f5b86180d99c5666a14421367c7187e5c"

    assert keccaky.keccak256(msg) == bytes.fromhex(result)
    assert keccaky.keccak256(msg).hex() == result

    k = KeccakHash()
    x = k.digest(msg)
    assert bytes(x).hex() == result
