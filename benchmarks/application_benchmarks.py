"""
Application Performance Benchmarks

This module contains benchmark tests for the Decimal Physics Controller
application, including simulation performance and calculation benchmarks.

Author: David A. Besemer
License: Free for Python community; commercial usage requires agreement.
"""

import pytest
import sys
from pathlib import Path
from decimal import Decimal

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.controller import (
    DecimalPhysicsController,
    PhysicsObject,
    Vector3D,
    SimulationMode
)


@pytest.mark.application
class TestPhysicsControllerBenchmarks:
    """Benchmark tests for DecimalPhysicsController."""

    def test_controller_initialization(self, benchmark):
        """Benchmark controller initialization."""
        result = benchmark(DecimalPhysicsController)
        assert isinstance(result, DecimalPhysicsController)

    def test_add_single_object(self, benchmark):
        """Benchmark adding a single object to simulation."""
        controller = DecimalPhysicsController()
        
        def add_object():
            obj = PhysicsObject(
                name="test_obj",
                mass=Decimal("1000"),
                position=Vector3D(Decimal("0"), Decimal("0"), Decimal("0"))
            )
            try:
                controller.add_object(obj)
            except ValueError:
                # Object already exists, remove and re-add
                controller.remove_object("test_obj")
                controller.add_object(obj)
        
        benchmark(add_object)

    def test_vector3d_magnitude_calculation(self, benchmark):
        """Benchmark Vector3D magnitude calculation."""
        vector = Vector3D(Decimal("3"), Decimal("4"), Decimal("5"))
        
        result = benchmark(vector.magnitude)
        assert isinstance(result, Decimal)

    def test_vector3d_dot_product(self, benchmark):
        """Benchmark Vector3D dot product calculation."""
        v1 = Vector3D(Decimal("1"), Decimal("2"), Decimal("3"))
        v2 = Vector3D(Decimal("4"), Decimal("5"), Decimal("6"))
        
        result = benchmark(v1.dot_product, v2)
        assert isinstance(result, Decimal)

    def test_vector3d_cross_product(self, benchmark):
        """Benchmark Vector3D cross product calculation."""
        v1 = Vector3D(Decimal("1"), Decimal("2"), Decimal("3"))
        v2 = Vector3D(Decimal("4"), Decimal("5"), Decimal("6"))
        
        result = benchmark(v1.cross_product, v2)
        assert isinstance(result, Vector3D)

    def test_vector3d_normalize(self, benchmark):
        """Benchmark Vector3D normalization."""
        vector = Vector3D(Decimal("3"), Decimal("4"), Decimal("5"))
        
        result = benchmark(vector.normalize)
        assert isinstance(result, Vector3D)

    def test_gravitational_force_calculation(self, benchmark):
        """Benchmark gravitational force calculation between two objects."""
        controller = DecimalPhysicsController()
        
        obj1 = PhysicsObject(
            name="earth",
            mass=Decimal("5.972e24"),
            position=Vector3D(Decimal("0"), Decimal("0"), Decimal("0"))
        )
        obj2 = PhysicsObject(
            name="moon",
            mass=Decimal("7.342e22"),
            position=Vector3D(Decimal("384400000"), Decimal("0"), Decimal("0"))
        )
        
        result = benchmark(controller.calculate_gravitational_force, obj1, obj2)
        assert isinstance(result, Vector3D)

    def test_kinetic_energy_calculation(self, benchmark):
        """Benchmark kinetic energy calculation."""
        controller = DecimalPhysicsController()
        
        obj = PhysicsObject(
            name="particle",
            mass=Decimal("1000"),
            position=Vector3D(Decimal("0"), Decimal("0"), Decimal("0")),
            velocity=Vector3D(Decimal("10"), Decimal("20"), Decimal("30"))
        )
        
        result = benchmark(controller.calculate_kinetic_energy, obj)
        assert isinstance(result, Decimal)

    def test_potential_energy_calculation(self, benchmark):
        """Benchmark gravitational potential energy calculation."""
        controller = DecimalPhysicsController()
        
        obj1 = PhysicsObject(
            name="obj1",
            mass=Decimal("1000"),
            position=Vector3D(Decimal("0"), Decimal("0"), Decimal("0"))
        )
        obj2 = PhysicsObject(
            name="obj2",
            mass=Decimal("2000"),
            position=Vector3D(Decimal("100"), Decimal("0"), Decimal("0"))
        )
        
        result = benchmark(
            controller.calculate_gravitational_potential_energy, obj1, obj2
        )
        assert isinstance(result, Decimal)

    def test_single_simulation_step(self, benchmark):
        """Benchmark a single simulation step."""
        controller = DecimalPhysicsController()
        
        # Add two objects
        obj1 = PhysicsObject(
            name="obj1",
            mass=Decimal("1000"),
            position=Vector3D(Decimal("0"), Decimal("0"), Decimal("0")),
            velocity=Vector3D(Decimal("10"), Decimal("0"), Decimal("0"))
        )
        obj2 = PhysicsObject(
            name="obj2",
            mass=Decimal("2000"),
            position=Vector3D(Decimal("100"), Decimal("0"), Decimal("0")),
            velocity=Vector3D(Decimal("-5"), Decimal("0"), Decimal("0"))
        )
        
        controller.add_object(obj1)
        controller.add_object(obj2)
        
        benchmark(controller.step)

    def test_multiple_simulation_steps(self, benchmark):
        """Benchmark multiple simulation steps."""
        controller = DecimalPhysicsController()
        controller.set_time_step(0.01)
        
        # Add two objects
        obj1 = PhysicsObject(
            name="obj1",
            mass=Decimal("1000"),
            position=Vector3D(Decimal("0"), Decimal("0"), Decimal("0")),
            velocity=Vector3D(Decimal("10"), Decimal("0"), Decimal("0"))
        )
        obj2 = PhysicsObject(
            name="obj2",
            mass=Decimal("2000"),
            position=Vector3D(Decimal("100"), Decimal("0"), Decimal("0")),
            velocity=Vector3D(Decimal("-5"), Decimal("0"), Decimal("0"))
        )
        
        controller.add_object(obj1)
        controller.add_object(obj2)
        
        def run_steps():
            for _ in range(10):
                controller.step()
        
        benchmark(run_steps)

    def test_total_energy_calculation(self, benchmark):
        """Benchmark total energy calculation."""
        controller = DecimalPhysicsController()
        
        # Add multiple objects
        for i in range(5):
            obj = PhysicsObject(
                name=f"obj{i}",
                mass=Decimal("1000"),
                position=Vector3D(
                    Decimal(str(i * 100)),
                    Decimal(str(i * 50)),
                    Decimal("0")
                ),
                velocity=Vector3D(
                    Decimal(str(i * 10)),
                    Decimal(str(i * 5)),
                    Decimal("0")
                )
            )
            controller.add_object(obj)
        
        result = benchmark(controller.calculate_total_energy)
        assert isinstance(result, Decimal)

    def test_apply_forces_multiple_objects(self, benchmark):
        """Benchmark force application for multiple objects."""
        controller = DecimalPhysicsController()
        
        # Add multiple objects
        for i in range(5):
            obj = PhysicsObject(
                name=f"obj{i}",
                mass=Decimal("1000"),
                position=Vector3D(
                    Decimal(str(i * 100)),
                    Decimal(str(i * 50)),
                    Decimal("0")
                )
            )
            controller.add_object(obj)
        
        benchmark(controller.apply_forces)

    def test_full_simulation_run(self, benchmark):
        """Benchmark a full simulation run with multiple objects."""
        def setup_and_run():
            controller = DecimalPhysicsController()
            controller.set_time_step(0.01)
            
            # Add objects
            obj1 = PhysicsObject(
                name="obj1",
                mass=Decimal("1000"),
                position=Vector3D(Decimal("0"), Decimal("0"), Decimal("0")),
                velocity=Vector3D(Decimal("10"), Decimal("0"), Decimal("0"))
            )
            obj2 = PhysicsObject(
                name="obj2",
                mass=Decimal("2000"),
                position=Vector3D(Decimal("100"), Decimal("0"), Decimal("0")),
                velocity=Vector3D(Decimal("-5"), Decimal("0"), Decimal("0"))
            )
            
            controller.add_object(obj1)
            controller.add_object(obj2)
            
            # Run simulation
            return controller.run_simulation(50)
        
        result = benchmark(setup_and_run)
        assert isinstance(result, list)
        assert len(result) == 50


@pytest.mark.application
@pytest.mark.slow
class TestPhysicsControllerStressTests:
    """Stress test benchmarks for the physics controller."""

    def test_many_objects_simulation(self, benchmark):
        """Benchmark simulation with many objects."""
        def setup_and_run():
            controller = DecimalPhysicsController()
            controller.set_time_step(0.01)
            
            # Add many objects
            for i in range(10):
                obj = PhysicsObject(
                    name=f"obj{i}",
                    mass=Decimal("1000"),
                    position=Vector3D(
                        Decimal(str(i * 50)),
                        Decimal(str(i * 25)),
                        Decimal(str(i * 10))
                    ),
                    velocity=Vector3D(
                        Decimal(str(i)),
                        Decimal(str(-i)),
                        Decimal("0")
                    )
                )
                controller.add_object(obj)
            
            # Run simulation
            return controller.run_simulation(10)
        
        result = benchmark(setup_and_run)
        assert isinstance(result, list)
        assert len(result) == 10

    def test_long_simulation_run(self, benchmark):
        """Benchmark a long simulation run."""
        def setup_and_run():
            controller = DecimalPhysicsController()
            controller.set_time_step(0.001)
            
            obj1 = PhysicsObject(
                name="obj1",
                mass=Decimal("1000"),
                position=Vector3D(Decimal("0"), Decimal("0"), Decimal("0")),
                velocity=Vector3D(Decimal("10"), Decimal("0"), Decimal("0"))
            )
            obj2 = PhysicsObject(
                name="obj2",
                mass=Decimal("2000"),
                position=Vector3D(Decimal("100"), Decimal("0"), Decimal("0")),
                velocity=Vector3D(Decimal("-5"), Decimal("0"), Decimal("0"))
            )
            
            controller.add_object(obj1)
            controller.add_object(obj2)
            
            # Run for 100 steps
            return controller.run_simulation(100)
        
        result = benchmark(setup_and_run)
        assert isinstance(result, list)
        assert len(result) == 100
