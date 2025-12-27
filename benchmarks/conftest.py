"""Pytest configuration for benchmark tests.

This module provides common fixtures and configuration for all benchmark tests
using pytest-benchmark.
"""

import pytest
from decimal import Decimal
import tempfile
import os
from pathlib import Path


@pytest.fixture
def benchmark_data_dir():
    """Create a temporary directory for benchmark data files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_decimal_values():
    """Generate sample decimal values for benchmarking."""
    return [
        Decimal('3.14159265358979323846'),
        Decimal('2.71828182845904523536'),
        Decimal('1.41421356237309504880'),
        Decimal('1.73205080756887729352'),
        Decimal('0.57721566490153286060'),
    ]


@pytest.fixture
def large_decimal_array():
    """Generate a large array of decimal values for performance testing."""
    return [Decimal(str(i * 0.1)) for i in range(10000)]


@pytest.fixture
def benchmark_config(benchmark):
    """Configure benchmark settings for tests."""
    # Set minimum rounds and iterations for benchmarks
    benchmark.extra_info = {
        'python_implementation': 'CPython',
        'benchmark_suite': 'decimal-physics-controller',
    }
    return benchmark


def pytest_configure(config):
    """Configure pytest for benchmark tests."""
    config.addinivalue_line(
        "markers", "benchmark: mark test as a benchmark test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


@pytest.fixture
def physics_constants():
    """Provide physics constants as Decimal values."""
    return {
        'pi': Decimal('3.14159265358979323846'),
        'e': Decimal('2.71828182845904523536'),
        'g': Decimal('9.80665'),  # standard gravity
        'c': Decimal('299792458'),  # speed of light in m/s
        'h': Decimal('6.62607015e-34'),  # Planck's constant
    }


@pytest.fixture
def mock_physics_data():
    """Generate mock physics simulation data."""
    return {
        'positions': [(Decimal(str(i*0.1)), Decimal(str(i*0.2))) for i in range(100)],
        'velocities': [(Decimal(str(i*0.05)), Decimal(str(i*0.03))) for i in range(100)],
        'accelerations': [(Decimal(str(i*0.01)), Decimal(str(i*0.02))) for i in range(100)],
        'masses': [Decimal(str(1.0 + i*0.01)) for i in range(100)],
    }
