from pytest import mark
from keccaky import Keccaky


@mark.slow
def test_extremely_long_loop_msg_KAT_256():
    k = Keccaky()

    with open("./tests/keccaky/ExtremelyLongMsgKAT_256.txt", "r") as file:
        lines = file.readlines()

        msg = lines[0].split("=")[1].strip()
        expected = lines[1].split("=")[1].strip().lower()
        loop = int(lines[2].split("=")[1].strip())

        result = k.digest(msg.encode())
        for i in range(loop - 1):
            if i % 1000 == 0:
                print(f"Progress: {i/loop:0.4f}%, loop: {i}")

            result = k.digest(result)

        assert result == expected
