"""Physics application performance benchmarks.

This module benchmarks physics simulation and calculation performance
including vector operations, force calculations, and integration methods.
"""

import pytest
from decimal import Decimal
import math


class TestPhysicsApplicationPerformance:
    """Benchmark physics calculations and simulations."""

    def test_decimal_arithmetic_operations(self, benchmark, large_decimal_array):
        """Benchmark basic arithmetic operations with Decimal values."""
        def decimal_arithmetic():
            result = Decimal('0')
            for val in large_decimal_array:
                result += val
            return result
        
        result = benchmark(decimal_arithmetic)
        assert isinstance(result, Decimal)

    def test_decimal_multiplication(self, benchmark, large_decimal_array):
        """Benchmark multiplication operations with Decimal values."""
        multiplier = Decimal('1.5')
        
        def decimal_multiply():
            return [val * multiplier for val in large_decimal_array]
        
        result = benchmark(decimal_multiply)
        assert len(result) == len(large_decimal_array)

    def test_vector_magnitude_calculation(self, benchmark, physics_constants):
        """Benchmark vector magnitude calculations."""
        vectors = [(Decimal('3'), Decimal('4')), (Decimal('5'), Decimal('12'))] * 500
        
        def calculate_magnitudes():
            magnitudes = []
            for x, y in vectors:
                # Using Pythagorean theorem
                mag_squared = x * x + y * y
                magnitudes.append(mag_squared)
            return magnitudes
        
        result = benchmark(calculate_magnitudes)
        assert len(result) == len(vectors)

    def test_force_calculation(self, benchmark, physics_constants):
        """Benchmark force calculation (F = m * a)."""
        masses = [Decimal('1.0') + Decimal(str(i * 0.01)) for i in range(1000)]
        accelerations = [Decimal('9.81') for _ in range(1000)]
        
        def calculate_forces():
            return [m * a for m, a in zip(masses, accelerations)]
        
        result = benchmark(calculate_forces)
        assert len(result) == 1000

    def test_kinetic_energy_calculation(self, benchmark):
        """Benchmark kinetic energy calculation (KE = 0.5 * m * v^2)."""
        masses = [Decimal('1.0') + Decimal(str(i * 0.01)) for i in range(1000)]
        velocities = [Decimal('10.0') + Decimal(str(i * 0.1)) for i in range(1000)]
        half = Decimal('0.5')
        
        def calculate_ke():
            return [half * m * v * v for m, v in zip(masses, velocities)]
        
        result = benchmark(calculate_ke)
        assert len(result) == 1000
        assert all(ke > 0 for ke in result)

    def test_momentum_calculation(self, benchmark):
        """Benchmark momentum calculation (p = m * v)."""
        masses = [Decimal('1.0') + Decimal(str(i * 0.01)) for i in range(1000)]
        velocities = [Decimal('10.0') + Decimal(str(i * 0.1)) for i in range(1000)]
        
        def calculate_momentum():
            return [m * v for m, v in zip(masses, velocities)]
        
        result = benchmark(calculate_momentum)
        assert len(result) == 1000

    def test_velocity_update_integration(self, benchmark):
        """Benchmark simple Euler integration for velocity updates."""
        velocities = [Decimal('10.0') for _ in range(1000)]
        accelerations = [Decimal('9.81') for _ in range(1000)]
        dt = Decimal('0.01')
        
        def update_velocities():
            return [v + a * dt for v, a in zip(velocities, accelerations)]
        
        result = benchmark(update_velocities)
        assert len(result) == 1000

    def test_position_update_integration(self, benchmark):
        """Benchmark position updates using velocity."""
        positions = [Decimal(str(i)) for i in range(1000)]
        velocities = [Decimal('10.0') for _ in range(1000)]
        dt = Decimal('0.01')
        
        def update_positions():
            return [p + v * dt for p, v in zip(positions, velocities)]
        
        result = benchmark(update_positions)
        assert len(result) == 1000

    def test_gravitational_force(self, benchmark, physics_constants):
        """Benchmark gravitational force calculation (F = G * m1 * m2 / r^2)."""
        G = Decimal('6.67430e-11')  # Gravitational constant
        m1 = Decimal('1e24')  # Mass 1
        m2 = Decimal('1e24')  # Mass 2
        distances = [Decimal(str(1e8 + i * 1000)) for i in range(100)]  # Various distances
        
        def calculate_gravity():
            forces = []
            for r in distances:
                f = G * m1 * m2 / (r * r)
                forces.append(f)
            return forces
        
        result = benchmark(calculate_gravity)
        assert len(result) == len(distances)

    def test_collision_detection(self, benchmark, mock_physics_data):
        """Benchmark collision detection with distance calculations."""
        threshold = Decimal('1.5')
        
        def detect_collisions():
            collisions = []
            positions = mock_physics_data['positions']
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]
                    dx = x2 - x1
                    dy = y2 - y1
                    dist_squared = dx * dx + dy * dy
                    if dist_squared < threshold * threshold:
                        collisions.append((i, j))
            return collisions
        
        result = benchmark(detect_collisions)
        assert isinstance(result, list)

    def test_simulation_step(self, benchmark, mock_physics_data):
        """Benchmark a complete simulation step."""
        dt = Decimal('0.01')
        g = Decimal('9.81')
        
        def simulate_step():
            # Create mutable copies
            positions = [list(p) for p in mock_physics_data['positions']]
            velocities = [list(v) for v in mock_physics_data['velocities']]
            
            # Update velocities (apply gravity)
            for i in range(len(velocities)):
                velocities[i][1] -= g * dt
            
            # Update positions
            for i in range(len(positions)):
                positions[i][0] += velocities[i][0] * dt
                positions[i][1] += velocities[i][1] * dt
            
            return positions, velocities
        
        result = benchmark(simulate_step)
        positions, velocities = result
        assert len(positions) == len(mock_physics_data['positions'])

    def test_physics_constant_operations(self, benchmark, physics_constants):
        """Benchmark operations using physics constants."""
        iterations = 1000
        pi = physics_constants['pi']
        e = physics_constants['e']
        
        def constant_operations():
            results = []
            for i in range(iterations):
                val = pi * e * Decimal(str(i))
                results.append(val)
            return results
        
        result = benchmark(constant_operations)
        assert len(result) == iterations
