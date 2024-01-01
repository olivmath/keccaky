import keccaky


def test_mock_result():
    assert keccaky.keccak256("Hello, world") == bytes.fromhex(
        "db99debe7fc546756227481ecaf5136f5b86180d99c5666a14421367c7187e5c"
    )
    assert (
        keccaky.keccak256("Hello, world").hex()
        == "db99debe7fc546756227481ecaf5136f5b86180d99c5666a14421367c7187e5c"
    )
