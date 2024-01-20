from keccaky import hash_it_bytes
import pytest
import time


@pytest.mark.benchmark(group="HashCreation", timer=time.time)
def test_create_10_hash(benchmark):
    benchmark(lambda: [hash_it_bytes(str(i).encode()).hex() for i in range(10)])


@pytest.mark.benchmark(group="HashCreation", timer=time.time)
def test_create_100_hash(benchmark):
    benchmark(lambda: [hash_it_bytes(str(i).encode()).hex() for i in range(100)])


@pytest.mark.benchmark(group="HashCreation", timer=time.time)
def test_create_1000_hash(benchmark):
    benchmark(lambda: [hash_it_bytes(str(i).encode()).hex() for i in range(1000)])
