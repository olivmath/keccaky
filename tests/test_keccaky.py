from keccaky import KeccakHash



def test_hello_world():
    msg = "Hello, world"
    result = "db99debe7fc546756227481ecaf5136f5b86180d99c5666a14421367c7187e5c"

    k = KeccakHash()
    x = k.digest(msg)
    assert bytes(x).hex() == result
