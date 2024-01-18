from keccaky import Keccaky
import pytest
import time


@pytest.mark.benchmark(group="HashCreation", timer=time.time)
def test_create_10_hash(benchmark):
    k = Keccaky()
    benchmark(lambda: [k.digest(str(i).encode()).hex() for i in range(10)])


@pytest.mark.benchmark(group="HashCreation", timer=time.time)
def test_create_100_hash(benchmark):
    k = Keccaky()
    benchmark(lambda: [k.digest(str(i).encode()).hex() for i in range(100)])


@pytest.mark.benchmark(group="HashCreation", timer=time.time)
def test_create_1000_hash(benchmark):
    k = Keccaky()
    benchmark(lambda: [k.digest(str(i).encode()).hex() for i in range(1000)])
