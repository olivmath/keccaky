from pytest import mark
from Crypto.Hash import keccak
from tqdm import tqdm
import os

@mark.slow
def test_check_state_file_KAT_256():
    state_file = "./tests/keccaky/test_state.txt"

    if not os.path.exists(state_file):
        raise FileNotFoundError(f"State file {state_file} not found.")

    with open(state_file, "r") as f:
        lines = f.readlines()

    if not lines or len(lines) < 2:
        raise ValueError(
            "The state file does not have enough lines for verification."
        )

    initial_message = "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmno"
    hash_obj = keccak.new(data=initial_message.encode(), digest_bits=256)
    initial_hash_hex = hash_obj.hexdigest()

    assert (
        initial_hash_hex == lines[0].split(" ")[1].strip()
    ), "🚨 Discrepancy in the initial hash."

    for i in tqdm(range(len(lines) - 1), desc="Verifying hashes"):
        current_hash_hex = lines[i].split(" ")[1].strip()
        expected_next_hash_hex = lines[i + 1].split(" ")[1].strip()

        hash_obj = keccak.new(data=bytes.fromhex(current_hash_hex), digest_bits=256)
        calculated_next_hash_hex = hash_obj.hexdigest()

        assert (
            calculated_next_hash_hex == expected_next_hash_hex
        ), f"🚨 Discrepancy in hash at index {i}."

    print("✅ All hashes verified correctly.")
