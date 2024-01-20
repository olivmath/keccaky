# Benchmark Results for Keccaky Library

This document presents the benchmark results for the Keccaky library, providing insights into its performance characteristics.

## Test Environment

- **Model Name**: MacBook Air
- **Chip**: Apple M2
- **Memory**: 8 GB
- **Operating System**: macOS 13.4.1

## Benchmark Tests

The benchmarks were conducted using the following tests:

1. **Keccaky Hash Function**: Testing the hash function performance of Keccaky library.
2. **PyCryptodome Hash Function**: Comparing the performance of Keccaky hash function with PyCryptodome's hash function.
3. **Hash Creation Performance**: Evaluating the performance of creating multiple hashes with Keccaky.

### Test Implementation

The tests were implemented in Python using `pytest` and `Crypto.Hash` from PyCryptodome.
The benchmarking was performed for different scales (10, 100, 1000 hashes) and compared between Keccaky and PyCryptodome hash functions.

## Results

### Hash Creation Benchmark

| Test Name             | Min Time (ms) | Max Time (ms) | Mean Time (ms) | StdDev | Median Time (ms) | IQR    | Outliers | OPS      | Rounds | Iterations |
| --------------------- | ------------- | ------------- | -------------- | ------ | ---------------- | ------ | -------- | -------- | ------ | ---------- |
| test_create_10_hash   | 8.3959        | 8.6651        | 8.4982         | 0.0490 | 8.4882           | 0.0572 | 33;3     | 117.6722 | 116    | 1          |
| test_create_100_hash  | 84.4929       | 84.9259       | 84.7084        | 0.1344 | 84.6931          | 0.2027 | 4;0      | 11.8052  | 12     | 1          |
| test_create_1000_hash | 847.2729      | 851.1820      | 848.5554       | 1.7237 | 847.5971         | 2.6027 | 1;0      | 1.1785   | 5      | 1          |

### Keccaky vs PyCryptodome Hash Function Performance

| Test Name                    | Min Time (ms) | Max Time (ms) | Mean Time (ms) | StdDev | Median Time (ms) | IQR    | Outliers | OPS      | Rounds | Iterations |
| ---------------------------- | ------------- | ------------- | -------------- | ------ | ---------------- | ------ | -------- | -------- | ------ | ---------- |
| test_keccaky_hash_speed      | 858.4659      | 866.1925      | 861.4367       | 3.1592 | 861.4287         | 4.7179 | 1;0      | 1.1609   | 5      | 1          |
| test_pycryptodome_hash_speed | 3.6407        | 4.0103        | 3.6709         | 0.0367 | 3.6611           | 0.0177 | 17;20    | 272.4092 | 174    | 1          |
