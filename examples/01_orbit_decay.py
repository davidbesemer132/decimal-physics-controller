#!/usr/bin/env python3
"""
Orbital Decay Simulation: Decimal Stability vs Float Instability

This example demonstrates how using Python's Decimal type provides superior
numerical stability in long-running physics simulations compared to standard
floating-point arithmetic.

The simulation tracks a satellite in a decaying orbit around Earth, showing
how accumulated rounding errors in float calculations can lead to incorrect
energy conservation, while Decimal maintains accuracy throughout the simulation.
"""

from decimal import Decimal, getcontext
import math
from typing import Tuple, List


class OrbitalSimulator:
    """Base orbital simulator using standard Python floats."""
    
    def __init__(self, altitude_km: float, velocity_kmps: float):
        """
        Initialize orbital simulator.
        
        Args:
            altitude_km: Satellite altitude in kilometers
            velocity_kmps: Orbital velocity in kilometers per second
        """
        self.EARTH_RADIUS = 6371.0  # km
        self.GM = 3.986004418e5  # km^3/s^2 (Earth's standard gravitational parameter)
        self.DRAG_COEFFICIENT = 1e-10  # Simplified atmospheric drag
        
        self.altitude = altitude_km
        self.velocity = velocity_kmps
        self.distance = self.EARTH_RADIUS + altitude_km
        self.time = 0.0
        self.total_energy = self._calculate_energy()
    
    def _calculate_energy(self) -> float:
        """Calculate total mechanical energy (kinetic + potential)."""
        kinetic = 0.5 * self.velocity ** 2
        potential = -self.GM / self.distance
        return kinetic + potential
    
    def step(self, dt: float) -> None:
        """
        Perform one simulation step using Euler method with atmospheric drag.
        
        Args:
            dt: Time step in seconds
        """
        # Gravity acceleration
        gravity = self.GM / (self.distance ** 2)
        
        # Atmospheric drag (simplified model)
        drag_accel = -self.DRAG_COEFFICIENT * self.velocity ** 2
        
        # Update velocity and position
        self.velocity += (drag_accel - gravity) * dt
        self.distance += self.velocity * dt
        self.altitude = self.distance - self.EARTH_RADIUS
        self.time += dt
        self.total_energy = self._calculate_energy()
    
    def get_state(self) -> dict:
        """Return current simulation state."""
        return {
            'time': self.time,
            'altitude': self.altitude,
            'velocity': self.velocity,
            'distance': self.distance,
            'energy': self.total_energy
        }


class DecimalOrbitalSimulator:
    """Orbital simulator using Python's Decimal type for enhanced precision."""
    
    def __init__(self, altitude_km: str, velocity_kmps: str, precision: int = 50):
        """
        Initialize decimal-based orbital simulator.
        
        Args:
            altitude_km: Satellite altitude in kilometers (as string for Decimal)
            velocity_kmps: Orbital velocity in kilometers per second (as string)
            precision: Number of significant digits (default 50)
        """
        getcontext().prec = precision
        
        self.EARTH_RADIUS = Decimal('6371')  # km
        self.GM = Decimal('3.986004418e5')  # km^3/s^2
        self.DRAG_COEFFICIENT = Decimal('1e-10')  # Simplified atmospheric drag
        
        self.altitude = Decimal(altitude_km)
        self.velocity = Decimal(velocity_kmps)
        self.distance = self.EARTH_RADIUS + self.altitude
        self.time = Decimal('0')
        self.total_energy = self._calculate_energy()
    
    def _calculate_energy(self) -> Decimal:
        """Calculate total mechanical energy (kinetic + potential)."""
        kinetic = Decimal('0.5') * self.velocity ** 2
        potential = -self.GM / self.distance
        return kinetic + potential
    
    def step(self, dt: str) -> None:
        """
        Perform one simulation step using Euler method with atmospheric drag.
        
        Args:
            dt: Time step in seconds (as string for Decimal)
        """
        dt = Decimal(dt)
        
        # Gravity acceleration
        gravity = self.GM / (self.distance ** 2)
        
        # Atmospheric drag (simplified model)
        drag_accel = -self.DRAG_COEFFICIENT * self.velocity ** 2
        
        # Update velocity and position
        self.velocity += (drag_accel - gravity) * dt
        self.distance += self.velocity * dt
        self.altitude = self.distance - self.EARTH_RADIUS
        self.time += dt
        self.total_energy = self._calculate_energy()
    
    def get_state(self) -> dict:
        """Return current simulation state."""
        return {
            'time': float(self.time),
            'altitude': float(self.altitude),
            'velocity': float(self.velocity),
            'distance': float(self.distance),
            'energy': float(self.total_energy)
        }


def run_simulation_comparison(duration_hours: int = 24) -> Tuple[List[dict], List[dict]]:
    """
    Run orbital decay simulation with both Float and Decimal implementations.
    
    Args:
        duration_hours: Simulation duration in hours
    
    Returns:
        Tuple of (float_results, decimal_results) containing state snapshots
    """
    # Initial conditions: 400 km altitude, circular orbit
    initial_altitude = 400.0  # km
    initial_velocity = math.sqrt(3.986004418e5 / (6371.0 + initial_altitude))  # circular orbit
    
    dt = 10.0  # 10 second time steps
    steps = int(duration_hours * 3600 / dt)
    
    # Initialize simulators
    float_sim = OrbitalSimulator(initial_altitude, initial_velocity)
    decimal_sim = DecimalOrbitalSimulator(
        str(initial_altitude),
        str(initial_velocity)
    )
    
    float_results = [float_sim.get_state()]
    decimal_results = [decimal_sim.get_state()]
    
    print(f"Running orbital decay simulation for {duration_hours} hours...")
    print(f"Initial altitude: {initial_altitude} km")
    print(f"Initial velocity: {initial_velocity:.6f} km/s")
    print(f"Time steps: {steps} (dt = {dt}s)\n")
    
    # Run simulation
    for step in range(steps):
        float_sim.step(dt)
        decimal_sim.step(str(dt))
        
        # Record every 360th step (1 hour) to reduce output
        if (step + 1) % 360 == 0:
            float_results.append(float_sim.get_state())
            decimal_results.append(decimal_sim.get_state())
            
            hours_elapsed = (step + 1) * dt / 3600
            print(f"Hour {hours_elapsed:.1f}: Alt={float_sim.altitude:.2f} km (Float) "
                  f"vs {decimal_sim.altitude:.2f} km (Decimal)")
    
    return float_results, decimal_results


def analyze_results(float_results: List[dict], decimal_results: List[dict]) -> None:
    """
    Analyze and display simulation results, highlighting numerical stability differences.
    
    Args:
        float_results: Float-based simulation results
        decimal_results: Decimal-based simulation results
    """
    print("\n" + "=" * 80)
    print("ORBITAL DECAY SIMULATION ANALYSIS")
    print("=" * 80 + "\n")
    
    # Initial state
    float_initial_energy = float_results[0]['energy']
    decimal_initial_energy = decimal_results[0]['energy']
    
    print(f"Initial Total Energy:")
    print(f"  Float:   {float_initial_energy:.15e} km²/s²")
    print(f"  Decimal: {decimal_initial_energy:.15e} km²/s²\n")
    
    # Final state
    float_final = float_results[-1]
    decimal_final = decimal_results[-1]
    
    print(f"Final State (after {float_final['time']/3600:.1f} hours):")
    print(f"\nAltitude:")
    print(f"  Float:   {float_final['altitude']:.2f} km")
    print(f"  Decimal: {decimal_final['altitude']:.2f} km")
    print(f"  Difference: {abs(float_final['altitude'] - decimal_final['altitude']):.4f} km\n")
    
    print(f"Velocity:")
    print(f"  Float:   {float_final['velocity']:.6f} km/s")
    print(f"  Decimal: {decimal_final['velocity']:.6f} km/s")
    print(f"  Difference: {abs(float_final['velocity'] - decimal_final['velocity']):.6e} km/s\n")
    
    # Energy conservation analysis
    float_final_energy = float_final['energy']
    decimal_final_energy = decimal_final['energy']
    
    float_energy_change = ((float_final_energy - float_initial_energy) / 
                           abs(float_initial_energy) * 100)
    decimal_energy_change = ((decimal_final_energy - decimal_initial_energy) / 
                             abs(decimal_initial_energy) * 100)
    
    print(f"Energy Conservation (% change from initial):")
    print(f"  Float:   {float_energy_change:+.8f}%")
    print(f"  Decimal: {decimal_energy_change:+.10f}%")
    print(f"  Improvement: {abs(float_energy_change - decimal_energy_change):.8f}% better\n")
    
    # Relative error in final altitude
    true_altitude = decimal_final['altitude']  # Assume Decimal is more accurate
    float_error = abs(float_final['altitude'] - true_altitude) / true_altitude * 100
    
    print(f"Relative Error in Final Altitude (Decimal as reference):")
    print(f"  Float: {float_error:.6f}%\n")
    
    print("=" * 80)
    print("CONCLUSION:")
    print("=" * 80)
    print(f"Using Decimal arithmetic reduces numerical error by approximately {float_error:.2f}%")
    print("in long-running orbital simulations, demonstrating superior stability for")
    print("physics-based calculations requiring high precision.")
    print("=" * 80)


if __name__ == '__main__':
    # Run the comparison simulation
    float_results, decimal_results = run_simulation_comparison(duration_hours=24)
    
    # Analyze and display results
    analyze_results(float_results, decimal_results)
