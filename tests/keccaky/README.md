# Keccak 256 Know-Answer-Tests (KAT)

Files downloaded on 2 January 2024 from https://keccak.team/obsolete/KeccakKAT-3.zip

## Overview of Tests

The tests in this directory are designed to validate the functionality and correctness of the Keccak hashing implementation provided by the `keccaky` library. The tests are structured to cover various scenarios, including short messages, long messages, and extremely long messages, ensuring comprehensive coverage of the hashing algorithm.

### Test Files

1. **test_check_state_file_KAT_256.py**: 
   - This test verifies the integrity of the hash states stored in a state file. It reads the initial message and its corresponding hash from the file, computes the hash using the Keccak algorithm, and checks for discrepancies. It also iterates through the hashes in the file to ensure that each subsequent hash is correctly derived from the previous one.

2. **test_short_msg_KAT_256.py**: 
   - This test uses a set of known answer tests (KAT) for short messages. It reads the messages and their expected hashes from a file and asserts that the computed hash matches the expected value for each message.

3. **test_long_msg_KAT_256.py**: 
   - Similar to the short message test, this file tests the hashing of longer messages. It reads the messages and their expected hashes from a separate file and performs assertions to ensure correctness.

4. **test_extremely_long_loop_msg_KAT_256.py**: 
   - This test is designed to handle extremely long messages by processing them in a loop. It maintains a state file to keep track of the last processed message, allowing for resuming tests without starting over. The test verifies that the computed hash matches the expected hash after a specified number of iterations.

### Running the Tests

To run the tests, ensure you have `pytest` installed. You can execute the tests by running the following command in your terminal:
