"""
Pytest configuration for benchmark tests.

This module configures pytest-benchmark for the Decimal Physics Controller benchmarks.

Author: David A. Besemer
License: Free for Python community; commercial usage requires agreement.
"""

import pytest
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


def pytest_configure(config):
    """Configure pytest with custom markers for benchmarks."""
    config.addinivalue_line(
        "markers", "filesystem: mark test as filesystem benchmark"
    )
    config.addinivalue_line(
        "markers", "fileformat: mark test as file format benchmark"
    )
    config.addinivalue_line(
        "markers", "application: mark test as application benchmark"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


@pytest.fixture(scope="session")
def benchmark_config():
    """Provide benchmark configuration."""
    return {
        "rounds": 100,
        "warmup_rounds": 10,
        "iterations": 1,
        "min_time": 0.000005,
    }


@pytest.fixture(scope="session")
def temp_benchmark_dir(tmp_path_factory):
    """Create a temporary directory for benchmark tests."""
    return tmp_path_factory.mktemp("benchmarks")


@pytest.fixture
def sample_data_small():
    """Provide small sample data for benchmarks."""
    return list(range(100))


@pytest.fixture
def sample_data_medium():
    """Provide medium sample data for benchmarks."""
    return list(range(10000))


@pytest.fixture
def sample_data_large():
    """Provide large sample data for benchmarks."""
    return list(range(100000))
