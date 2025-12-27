"""
Benchmark tests for core physics calculations.

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
    Vector3D,
    SimulationMode
)


def benchmark_gravitational_force_calculation(iterations=1000):
    """
    Benchmark gravitational force calculations between two objects.
    
    This benchmark measures the performance of calculating gravitational forces
    using decimal precision arithmetic.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    controller = DecimalPhysicsController()
    
    # Create two objects
    obj1 = PhysicsObject(
        name="Object1",
        mass=Decimal('5.972e24'),  # Earth's mass
        position=Vector3D(Decimal(0), Decimal(0), Decimal(0))
    )
    
    obj2 = PhysicsObject(
        name="Object2",
        mass=Decimal('7.348e22'),  # Moon's mass
        position=Vector3D(Decimal('384400000'), Decimal(0), Decimal(0))  # Moon's distance
    )
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        force = controller.calculate_gravitational_force(obj1, obj2)
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_energy_calculation(iterations=1000):
    """
    Benchmark total energy calculations for a multi-body system.
    
    This benchmark measures the performance of calculating kinetic and potential
    energy for multiple objects in a simulation.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per calculation in seconds
    """
    controller = DecimalPhysicsController()
    
    # Create multiple objects
    for i in range(5):
        obj = PhysicsObject(
            name=f"Object{i}",
            mass=Decimal('1e24'),
            position=Vector3D(Decimal(i * 1e9), Decimal(0), Decimal(0)),
            velocity=Vector3D(Decimal(1000), Decimal(0), Decimal(0))
        )
        controller.add_object(obj)
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        energy = controller.calculate_total_energy()
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def benchmark_simulation_step(iterations=100):
    """
    Benchmark a complete simulation step including force, velocity, and position updates.
    
    This benchmark measures the performance of a full simulation step cycle,
    which includes calculating forces, updating velocities, and updating positions.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Average time per simulation step in seconds
    """
    controller = DecimalPhysicsController()
    controller.set_time_step(0.01)
    
    # Create a simple two-body system
    obj1 = PhysicsObject(
        name="Star",
        mass=Decimal('1.989e30'),  # Sun's mass
        position=Vector3D(Decimal(0), Decimal(0), Decimal(0)),
        velocity=Vector3D(Decimal(0), Decimal(0), Decimal(0))
    )
    
    obj2 = PhysicsObject(
        name="Planet",
        mass=Decimal('5.972e24'),  # Earth's mass
        position=Vector3D(Decimal('1.496e11'), Decimal(0), Decimal(0)),  # 1 AU
        velocity=Vector3D(Decimal(0), Decimal('29780'), Decimal(0))  # Orbital velocity
    )
    
    controller.add_object(obj1)
    controller.add_object(obj2)
    
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        controller.step()
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    return avg_time


def run_all_benchmarks():
    """Run all benchmark tests and display results."""
    print("=" * 70)
    print("Decimal Physics Controller - Physics Calculations Benchmarks")
    print("=" * 70)
    print(f"Copyright (c) 2025 David A. Besemer")
    print(f"Dual Licensed: MIT License OR CC BY 4.0")
    print(f"See LICENSE file for details")
    print("=" * 70)
    print()
    
    print("Running benchmarks...")
    print()
    
    # Gravitational force benchmark
    print("1. Gravitational Force Calculation:")
    avg_time = benchmark_gravitational_force_calculation(1000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} calculations/second")
    print()
    
    # Energy calculation benchmark
    print("2. Total Energy Calculation (5-body system):")
    avg_time = benchmark_energy_calculation(1000)
    print(f"   Average time: {avg_time * 1e6:.2f} microseconds")
    print(f"   Throughput: {1/avg_time:.0f} calculations/second")
    print()
    
    # Simulation step benchmark
    print("3. Complete Simulation Step (2-body system):")
    avg_time = benchmark_simulation_step(100)
    print(f"   Average time: {avg_time * 1e3:.2f} milliseconds")
    print(f"   Throughput: {1/avg_time:.0f} steps/second")
    print()
    
    print("=" * 70)
    print("Benchmarks complete!")
    print("=" * 70)


if __name__ == "__main__":
    run_all_benchmarks()
