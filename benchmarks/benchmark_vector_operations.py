"""
Benchmark tests for vector operations with decimal precision.

Copyright (c) 2025 David A. Besemer

Dual Licensed under:
1. MIT License - for commercial/derivative use
2. Creative Commons Attribution 4.0 International - for academic/scientific use

See the LICENSE file in the repository root for full license text.

For academic/scientific use (CC BY 4.0):
- You must give appropriate credit to David A. Besemer
- Provide a link to the license: http://creativecommons.org/licenses/by/4.0/
- Indicate if changes were made

For commercial/derivative use (MIT):
- Permission is granted to use, copy, modify, merge, publish, distribute,
  sublicense, and/or sell copies of the Software
- The above copyright notice and this permission notice shall be included
  in all copies or substantial portions of the Software

Choose the license that best fits your use case. Both are equally valid.
"""

import time
from decimal import Decimal
import sys
import os

# Add parent directory to path to import the controller
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.controller import Vector3D


def benchmark_vector_magnitude(iterations=10000):
    """
    Benchmark vector magnitude calculations.
    
    Measures the performance of calculating the magnitude of 3D vectors
    using decimal precision and Newton's method for square root.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    vector = Vector3D(Decimal('123.456'), Decimal('789.012'), Decimal('345.678'))
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        mag = vector.magnitude()
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_vector_normalization(iterations=10000):
    """
    Benchmark vector normalization.
    
    Measures the performance of normalizing 3D vectors to unit length,
    which involves magnitude calculation and component division.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    vector = Vector3D(Decimal('123.456'), Decimal('789.012'), Decimal('345.678'))
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        normalized = vector.normalize()
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_dot_product(iterations=10000):
    """
    Benchmark dot product calculations.
    
    Measures the performance of calculating dot products between 3D vectors
    using decimal precision arithmetic.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    vec1 = Vector3D(Decimal('1.23'), Decimal('4.56'), Decimal('7.89'))
    vec2 = Vector3D(Decimal('9.87'), Decimal('6.54'), Decimal('3.21'))
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        result = vec1.dot_product(vec2)
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_cross_product(iterations=10000):
    """
    Benchmark cross product calculations.
    
    Measures the performance of calculating cross products between 3D vectors
    using decimal precision arithmetic.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    vec1 = Vector3D(Decimal('1.23'), Decimal('4.56'), Decimal('7.89'))
    vec2 = Vector3D(Decimal('9.87'), Decimal('6.54'), Decimal('3.21'))
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        result = vec1.cross_product(vec2)
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_vector_creation(iterations=10000):
    """
    Benchmark vector object creation and initialization.
    
    Measures the performance of creating Vector3D objects with decimal
    component conversion and validation.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per creation in seconds
    """
    start_time = time.perf_counter()
    
    for i in range(iterations):
        vec = Vector3D(Decimal(i), Decimal(i * 2), Decimal(i * 3))
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def run_all_benchmarks():
    """Run all vector operation benchmark tests and display results."""
    print("=" * 70)
    print("Decimal Physics Controller - Vector Operations Benchmarks")
    print("=" * 70)
    print(f"Copyright (c) 2025 David A. Besemer")
    print(f"Dual Licensed: MIT License OR CC BY 4.0")
    print(f"See LICENSE file for details")
    print("=" * 70)
    print()
    
    print("Running vector operation benchmarks...")
    print()
    
    # Vector creation benchmark
    print("1. Vector Creation:")
    avg_time = benchmark_vector_creation(10000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} creations/second")
    print()
    
    # Magnitude benchmark
    print("2. Vector Magnitude Calculation:")
    avg_time = benchmark_vector_magnitude(10000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} calculations/second")
    print()
    
    # Normalization benchmark
    print("3. Vector Normalization:")
    avg_time = benchmark_vector_normalization(10000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} normalizations/second")
    print()
    
    # Dot product benchmark
    print("4. Dot Product Calculation:")
    avg_time = benchmark_dot_product(10000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} calculations/second")
    print()
    
    # Cross product benchmark
    print("5. Cross Product Calculation:")
    avg_time = benchmark_cross_product(10000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} calculations/second")
    print()
    
    print("=" * 70)
    print("Vector operation benchmarks complete!")
    print("=" * 70)


if __name__ == "__main__":
    run_all_benchmarks()
