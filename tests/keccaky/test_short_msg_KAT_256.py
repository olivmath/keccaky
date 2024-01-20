from keccaky import hash_it_bytes
from typing import Dict
from pytest import mark


KAT = []
with open("./tests/keccaky/ShortMsgKAT_256.txt", "r") as file:
    lines = file.readlines()

    for i in range(0, len(lines), 3):
        KAT.append(
            {
                "msg": bytes.fromhex(lines[i].split("=")[1].strip().lower()),
                "expected": bytes.fromhex(lines[i + 1].split("=")[1].strip().lower()),
            }
        )


@mark.parametrize("data", KAT)
def test_short_msg_KAT_256(data: Dict[str, bytes]):
    result = hash_it_bytes(data["msg"])

    assert result == data["expected"]
