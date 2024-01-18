from pytest import mark
from keccaky import Keccaky
from tqdm import tqdm
import os


def load_state(state_file):
    if os.path.exists(state_file):
        with open(state_file, "r") as f:
            lines = f.readlines()
            if lines:
                lines = [line for line in lines if line.strip()]
                if lines:
                    last_saved_loop = len(lines) - 1
                    last_saved_result = lines[-1].split(" ")[1].strip()
                    return last_saved_loop, bytes.fromhex(last_saved_result)
    return 0, None


def write_buffer_to_file(f, buffer):
    for loop_index, result in buffer:
        f.write(f"{loop_index} {result.hex()}\n")
    buffer.clear()


def run_test(k, start_loop, initial_result, state_file):
    with open("./tests/keccaky/ExtremelyLongMsgKAT_256.txt", "r") as file:
        lines = file.readlines()
        msg = lines[0].split("=")[1].strip()
        expected = lines[1].split("=")[1].strip().lower()
        loop = int(lines[2].split("=")[1].strip())

        result = initial_result if initial_result else k.digest(msg.encode())

        buffer = []
        buffer_size = 1000  # Buffer size

        with open(state_file, "a") as f:
            if start_loop == 0:
                buffer.append((0, result))

            with tqdm(total=loop, initial=start_loop, desc="Running test") as pbar:
                for i in range(start_loop, loop):
                    result = k.digest(result)
                    buffer.append((i, result))

                    if i % buffer_size == 0 or i == loop - 1:
                        write_buffer_to_file(f, buffer)
                    pbar.update()

            assert result.hex() == expected


@mark.slow
def test_extremely_long_loop_msg_KAT_256():
    k = Keccaky()
    state_file = "./tests/keccaky/test_state.txt"

    start_loop, initial_result = load_state(state_file)
    run_test(k, start_loop, initial_result, state_file)
