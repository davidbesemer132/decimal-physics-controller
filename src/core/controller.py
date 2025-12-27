"""
Decimal Physics Controller Module

This module provides high-precision physics calculations using Python's Decimal type
for all critical computations, ensuring accuracy in numerical simulations.
"""

from decimal import Decimal, getcontext, ROUND_HALF_UP
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum
import math


# Set high precision for Decimal calculations
getcontext().prec = 50


class PhysicsConstants:
    """Universal physics constants with Decimal precision."""
    
    GRAVITATIONAL_CONSTANT = Decimal('6.67430E-11')  # m^3 kg^-1 s^-2
    SPEED_OF_LIGHT = Decimal('299792458')  # m/s
    PLANCK_CONSTANT = Decimal('6.62607015E-34')  # J·s
    BOLTZMANN_CONSTANT = Decimal('1.380649E-23')  # J/K
    AVOGADRO_NUMBER = Decimal('6.02214076E23')  # mol^-1
    ELEMENTARY_CHARGE = Decimal('1.602176634E-19')  # C
    VACUUM_PERMITTIVITY = Decimal('8.8541878128E-12')  # F/m
    VACUUM_PERMEABILITY = Decimal('1.25663706212E-6')  # H/m


class SimulationMode(Enum):
    """Supported simulation modes."""
    CLASSICAL_MECHANICS = "classical"
    RELATIVISTIC = "relativistic"
    QUANTUM = "quantum"
    ELECTROMAGNETIC = "electromagnetic"


@dataclass
class Vector3D:
    """3D Vector with Decimal components."""
    x: Decimal
    y: Decimal
    z: Decimal
    
    def __post_init__(self):
        """Ensure all components are Decimal."""
        self.x = Decimal(str(self.x)) if not isinstance(self.x, Decimal) else self.x
        self.y = Decimal(str(self.y)) if not isinstance(self.y, Decimal) else self.y
        self.z = Decimal(str(self.z)) if not isinstance(self.z, Decimal) else self.z
    
    def magnitude(self) -> Decimal:
        """Calculate the magnitude of the vector."""
        sum_squares = self.x ** 2 + self.y ** 2 + self.z ** 2
        # Use decimal approximation for square root
        return self._decimal_sqrt(sum_squares)
    
    def dot_product(self, other: 'Vector3D') -> Decimal:
        """Calculate dot product with another vector."""
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross_product(self, other: 'Vector3D') -> 'Vector3D':
        """Calculate cross product with another vector."""
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    @staticmethod
    def _decimal_sqrt(value: Decimal) -> Decimal:
        """Calculate square root using Newton's method for Decimal precision."""
        if value < 0:
            raise ValueError("Cannot calculate square root of negative number")
        if value == 0:
            return Decimal(0)
        
        # Initial guess
        x = value
        while True:
            x_new = (x + value / x) / 2
            if abs(x_new - x) < Decimal(10) ** -(getcontext().prec - 5):
                return x_new
            x = x_new
    
    def normalize(self) -> 'Vector3D':
        """Return normalized vector."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)


@dataclass
class PhysicsObject:
    """Represents a physical object with mass and position."""
    name: str
    mass: Decimal
    position: Vector3D
    velocity: Vector3D = field(default_factory=lambda: Vector3D(Decimal(0), Decimal(0), Decimal(0)))
    acceleration: Vector3D = field(default_factory=lambda: Vector3D(Decimal(0), Decimal(0), Decimal(0)))
    
    def __post_init__(self):
        """Ensure mass and vectors use Decimal."""
        self.mass = Decimal(str(self.mass)) if not isinstance(self.mass, Decimal) else self.mass
        if not isinstance(self.position, Vector3D):
            raise TypeError("position must be a Vector3D")
        if not isinstance(self.velocity, Vector3D):
            raise TypeError("velocity must be a Vector3D")
        if not isinstance(self.acceleration, Vector3D):
            raise TypeError("acceleration must be a Vector3D")


class DecimalPhysicsController:
    """
    Main controller for high-precision physics simulations using Decimal arithmetic.
    
    This controller manages simulation state, calculates forces, and updates object
    states with decimal precision for critical calculations.
    """
    
    def __init__(self, mode: SimulationMode = SimulationMode.CLASSICAL_MECHANICS):
        """
        Initialize the physics controller.
        
        Args:
            mode: The simulation mode to use
        """
        self.mode = mode
        self.objects: Dict[str, PhysicsObject] = {}
        self.time_step: Decimal = Decimal('0.01')  # Default 10ms
        self.current_time: Decimal = Decimal(0)
        self.total_energy: Decimal = Decimal(0)
        self.simulation_history: List[Dict] = []
    
    def set_time_step(self, time_step: float) -> None:
        """
        Set the simulation time step.
        
        Args:
            time_step: Time step in seconds (will be converted to Decimal)
        """
        self.time_step = Decimal(str(time_step))
    
    def add_object(self, obj: PhysicsObject) -> None:
        """
        Add an object to the simulation.
        
        Args:
            obj: PhysicsObject to add
        """
        if obj.name in self.objects:
            raise ValueError(f"Object '{obj.name}' already exists in simulation")
        self.objects[obj.name] = obj
    
    def remove_object(self, name: str) -> None:
        """
        Remove an object from the simulation.
        
        Args:
            name: Name of the object to remove
        """
        if name not in self.objects:
            raise ValueError(f"Object '{name}' not found in simulation")
        del self.objects[name]
    
    def calculate_gravitational_force(self, obj1: PhysicsObject, obj2: PhysicsObject) -> Vector3D:
        """
        Calculate gravitational force between two objects using Newton's law of universal gravitation.
        
        F = G * (m1 * m2) / r^2
        
        Args:
            obj1: First object
            obj2: Second object
            
        Returns:
            Force vector on obj1 due to obj2
        """
        # Calculate displacement vector
        dx = obj2.position.x - obj1.position.x
        dy = obj2.position.y - obj1.position.y
        dz = obj2.position.z - obj1.position.z
        
        displacement = Vector3D(dx, dy, dz)
        distance = displacement.magnitude()
        
        if distance == 0:
            raise ValueError("Objects cannot occupy the same position")
        
        # F = G * m1 * m2 / r^2
        force_magnitude = (PhysicsConstants.GRAVITATIONAL_CONSTANT * 
                          obj1.mass * obj2.mass / (distance ** 2))
        
        # Normalize displacement and apply force magnitude
        direction = displacement.normalize()
        
        return Vector3D(
            direction.x * force_magnitude,
            direction.y * force_magnitude,
            direction.z * force_magnitude
        )
    
    def calculate_kinetic_energy(self, obj: PhysicsObject) -> Decimal:
        """
        Calculate kinetic energy of an object.
        
        KE = 0.5 * m * v^2
        
        Args:
            obj: Physics object
            
        Returns:
            Kinetic energy in Joules
        """
        velocity_squared = obj.velocity.dot_product(obj.velocity)
        return Decimal('0.5') * obj.mass * velocity_squared
    
    def calculate_gravitational_potential_energy(self, obj1: PhysicsObject, obj2: PhysicsObject) -> Decimal:
        """
        Calculate gravitational potential energy between two objects.
        
        PE = -G * m1 * m2 / r
        
        Args:
            obj1: First object
            obj2: Second object
            
        Returns:
            Potential energy in Joules
        """
        dx = obj2.position.x - obj1.position.x
        dy = obj2.position.y - obj1.position.y
        dz = obj2.position.z - obj1.position.z
        
        distance = Vector3D(dx, dy, dz).magnitude()
        
        if distance == 0:
            raise ValueError("Objects cannot occupy the same position")
        
        return (-PhysicsConstants.GRAVITATIONAL_CONSTANT * 
                obj1.mass * obj2.mass / distance)
    
    def update_positions(self) -> None:
        """
        Update positions of all objects using current velocities.
        Uses simple Euler integration: x(t+dt) = x(t) + v(t)*dt
        """
        for obj in self.objects.values():
            obj.position.x += obj.velocity.x * self.time_step
            obj.position.y += obj.velocity.y * self.time_step
            obj.position.z += obj.velocity.z * self.time_step
    
    def update_velocities(self) -> None:
        """
        Update velocities of all objects using current accelerations.
        Uses simple Euler integration: v(t+dt) = v(t) + a(t)*dt
        """
        for obj in self.objects.values():
            obj.velocity.x += obj.acceleration.x * self.time_step
            obj.velocity.y += obj.acceleration.y * self.time_step
            obj.velocity.z += obj.acceleration.z * self.time_step
    
    def reset_accelerations(self) -> None:
        """Reset all accelerations to zero."""
        for obj in self.objects.values():
            obj.acceleration = Vector3D(Decimal(0), Decimal(0), Decimal(0))
    
    def apply_forces(self) -> None:
        """
        Calculate and apply all gravitational forces between objects.
        Updates accelerations based on F = ma.
        """
        self.reset_accelerations()
        
        object_list = list(self.objects.values())
        
        for i, obj1 in enumerate(object_list):
            for obj2 in object_list[i + 1:]:
                # Calculate force on obj1 due to obj2
                force = self.calculate_gravitational_force(obj1, obj2)
                acceleration_x = force.x / obj1.mass
                acceleration_y = force.y / obj1.mass
                acceleration_z = force.z / obj1.mass
                
                obj1.acceleration.x += acceleration_x
                obj1.acceleration.y += acceleration_y
                obj1.acceleration.z += acceleration_z
                
                # Calculate reaction force on obj2
                obj2.acceleration.x -= acceleration_x * obj1.mass / obj2.mass
                obj2.acceleration.y -= acceleration_y * obj1.mass / obj2.mass
                obj2.acceleration.z -= acceleration_z * obj1.mass / obj2.mass
    
    def calculate_total_energy(self) -> Decimal:
        """
        Calculate total energy (kinetic + potential) in the system.
        
        Returns:
            Total energy in Joules
        """
        total_ke = Decimal(0)
        total_pe = Decimal(0)
        
        # Kinetic energy
        for obj in self.objects.values():
            total_ke += self.calculate_kinetic_energy(obj)
        
        # Potential energy (pairwise)
        object_list = list(self.objects.values())
        for i, obj1 in enumerate(object_list):
            for obj2 in object_list[i + 1:]:
                total_pe += self.calculate_gravitational_potential_energy(obj1, obj2)
        
        self.total_energy = total_ke + total_pe
        return self.total_energy
    
    def step(self) -> None:
        """
        Perform a single simulation step.
        
        Order of operations:
        1. Apply forces to calculate accelerations
        2. Update velocities based on accelerations
        3. Update positions based on velocities
        4. Update current time
        5. Record energy for monitoring
        """
        self.apply_forces()
        self.update_velocities()
        self.update_positions()
        self.current_time += self.time_step
        self.calculate_total_energy()
    
    def run_simulation(self, steps: int) -> List[Dict]:
        """
        Run the simulation for a specified number of steps.
        
        Args:
            steps: Number of simulation steps to run
            
        Returns:
            List of state snapshots at each step
        """
        history = []
        
        for _ in range(steps):
            self.step()
            
            # Record snapshot
            snapshot = {
                'time': float(self.current_time),
                'total_energy': float(self.total_energy),
                'objects': {
                    name: {
                        'position': (float(obj.position.x), float(obj.position.y), float(obj.position.z)),
                        'velocity': (float(obj.velocity.x), float(obj.velocity.y), float(obj.velocity.z)),
                        'acceleration': (float(obj.acceleration.x), float(obj.acceleration.y), float(obj.acceleration.z))
                    }
                    for name, obj in self.objects.items()
                }
            }
            history.append(snapshot)
        
        self.simulation_history.extend(history)
        return history
    
    def get_object(self, name: str) -> Optional[PhysicsObject]:
        """
        Get an object from the simulation by name.
        
        Args:
            name: Name of the object
            
        Returns:
            PhysicsObject or None if not found
        """
        return self.objects.get(name)
    
    def get_object_state(self, name: str) -> Dict:
        """
        Get the current state of an object.
        
        Args:
            name: Name of the object
            
        Returns:
            Dictionary containing object state
        """
        obj = self.get_object(name)
        if not obj:
            raise ValueError(f"Object '{name}' not found")
        
        return {
            'name': obj.name,
            'mass': float(obj.mass),
            'position': (float(obj.position.x), float(obj.position.y), float(obj.position.z)),
            'velocity': (float(obj.velocity.x), float(obj.velocity.y), float(obj.velocity.z)),
            'acceleration': (float(obj.acceleration.x), float(obj.acceleration.y), float(obj.acceleration.z)),
            'kinetic_energy': float(self.calculate_kinetic_energy(obj))
        }
    
    def reset_simulation(self) -> None:
        """Reset the simulation to initial state."""
        self.current_time = Decimal(0)
        self.total_energy = Decimal(0)
        self.simulation_history = []
        self.reset_accelerations()
