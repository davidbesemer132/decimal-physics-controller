"""
Benchmark tests for energy calculations.

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

from src.core.controller import (
    DecimalPhysicsController,
    PhysicsObject,
    Vector3D
)


def benchmark_kinetic_energy(iterations=10000):
    """
    Benchmark kinetic energy calculations.
    
    Measures the performance of calculating kinetic energy (KE = 0.5 * m * v^2)
    for physics objects using decimal precision.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    controller = DecimalPhysicsController()
    
    obj = PhysicsObject(
        name="TestObject",
        mass=Decimal('1000'),
        position=Vector3D(Decimal(0), Decimal(0), Decimal(0)),
        velocity=Vector3D(Decimal('100.5'), Decimal('200.3'), Decimal('150.7'))
    )
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        ke = controller.calculate_kinetic_energy(obj)
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_potential_energy(iterations=10000):
    """
    Benchmark gravitational potential energy calculations.
    
    Measures the performance of calculating gravitational potential energy
    (PE = -G * m1 * m2 / r) between two objects using decimal precision.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    controller = DecimalPhysicsController()
    
    obj1 = PhysicsObject(
        name="Object1",
        mass=Decimal('1e24'),
        position=Vector3D(Decimal(0), Decimal(0), Decimal(0))
    )
    
    obj2 = PhysicsObject(
        name="Object2",
        mass=Decimal('5e22'),
        position=Vector3D(Decimal('1e9'), Decimal('1e9'), Decimal('1e9'))
    )
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        pe = controller.calculate_gravitational_potential_energy(obj1, obj2)
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_total_energy_single_body(iterations=10000):
    """
    Benchmark total energy calculation for a single body.
    
    Measures the performance of calculating total energy (kinetic only)
    for a single-body system.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    controller = DecimalPhysicsController()
    
    obj = PhysicsObject(
        name="SingleBody",
        mass=Decimal('1000'),
        position=Vector3D(Decimal(0), Decimal(0), Decimal(0)),
        velocity=Vector3D(Decimal('100'), Decimal('200'), Decimal('300'))
    )
    controller.add_object(obj)
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        total_e = controller.calculate_total_energy()
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_total_energy_multi_body(iterations=1000):
    """
    Benchmark total energy calculation for multiple bodies.
    
    Measures the performance of calculating total energy (kinetic + potential)
    for a multi-body system with all pairwise interactions.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    controller = DecimalPhysicsController()
    
    # Create a system with 10 bodies
    for i in range(10):
        obj = PhysicsObject(
            name=f"Body{i}",
            mass=Decimal(f'{(i+1) * 1e23}'),
            position=Vector3D(Decimal(i * 1e9), Decimal(i * 1e8), Decimal(0)),
            velocity=Vector3D(Decimal(1000 * i), Decimal(500), Decimal(0))
        )
        controller.add_object(obj)
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        total_e = controller.calculate_total_energy()
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_energy_conservation_check(iterations=100):
    """
    Benchmark energy conservation verification in a simulation.
    
    Measures the performance of running a short simulation while tracking
    total energy to verify conservation (for benchmark purposes).
    
    Args:
        iterations: Number of simulation steps per iteration
        
    Returns:
        Average time per energy check in seconds
    """
    controller = DecimalPhysicsController()
    controller.set_time_step(0.01)
    
    # Create a two-body system
    obj1 = PhysicsObject(
        name="Body1",
        mass=Decimal('1e24'),
        position=Vector3D(Decimal(0), Decimal(0), Decimal(0)),
        velocity=Vector3D(Decimal(0), Decimal(0), Decimal(0))
    )
    
    obj2 = PhysicsObject(
        name="Body2",
        mass=Decimal('5e23'),
        position=Vector3D(Decimal('1e9'), Decimal(0), Decimal(0)),
        velocity=Vector3D(Decimal(0), Decimal('1000'), Decimal(0))
    )
    
    controller.add_object(obj1)
    controller.add_object(obj2)
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        controller.step()
        energy = controller.calculate_total_energy()
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def run_all_benchmarks():
    """Run all energy calculation benchmark tests and display results."""
    print("=" * 70)
    print("Decimal Physics Controller - Energy Calculations Benchmarks")
    print("=" * 70)
    print(f"Copyright (c) 2025 David A. Besemer")
    print(f"Dual Licensed: MIT License OR CC BY 4.0")
    print(f"See LICENSE file for details")
    print("=" * 70)
    print()
    
    print("Running energy calculation benchmarks...")
    print()
    
    # Kinetic energy benchmark
    print("1. Kinetic Energy Calculation:")
    avg_time = benchmark_kinetic_energy(10000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} calculations/second")
    print()
    
    # Potential energy benchmark
    print("2. Gravitational Potential Energy:")
    avg_time = benchmark_potential_energy(10000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} calculations/second")
    print()
    
    # Single body total energy
    print("3. Total Energy (Single Body):")
    avg_time = benchmark_total_energy_single_body(10000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} calculations/second")
    print()
    
    # Multi-body total energy
    print("4. Total Energy (10-Body System):")
    avg_time = benchmark_total_energy_multi_body(1000)
    print(f"   Average time: {avg_time * 1e3:.2f} milliseconds")
    print(f"   Throughput: {1/avg_time:.2f} calculations/second")
    print()
    
    # Energy conservation check
    print("5. Energy Conservation Check (per simulation step):")
    avg_time = benchmark_energy_conservation_check(100)
    print(f"   Average time: {avg_time * 1e3:.2f} milliseconds")
    print(f"   Throughput: {1/avg_time:.2f} steps/second")
    print()
    
    print("=" * 70)
    print("Energy calculation benchmarks complete!")
    print("=" * 70)


if __name__ == "__main__":
    run_all_benchmarks()
