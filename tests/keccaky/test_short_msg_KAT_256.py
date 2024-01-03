from typing import Dict
from pytest import mark
from keccaky import Keccaky


KAT = []
with open("./tests/keccaky/ShortMsgKAT_256.txt", "r") as file:
    lines = file.readlines()

    for i in range(0, len(lines), 3):
        KAT.append(
            {
                "msg": lines[i].split("=")[1].strip().lower(),
                "expected": lines[i + 1].split("=")[1].strip().lower(),
            }
        )


@mark.parametrize("data", KAT)
def test_short_msg_KAT_256(data: Dict[str, bytes]):
    k = Keccaky()

    result = k.digest(data["msg"])

    assert result == data["expected"]
