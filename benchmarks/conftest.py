"""pytest-benchmark configuration for performance tests."""

import pytest


@pytest.fixture(scope="session")
def benchmark_min_rounds():
    """Minimum number of rounds for benchmarks."""
    return 5


def pytest_configure(config):
    """Configure pytest with benchmark defaults."""
    config.addinivalue_line(
        "markers", "benchmark: mark test as a performance benchmark"
    )
