import decimal
from decimal import Decimal, getcontext
from typing import Union, List, Tuple
import numpy as np

# Typ-Alias für Flexibilität
Number = Union[int, float, Decimal, str]

class DecimalPhysicsEngine:
    """
    ANT CORP PRECISION CORE
    Handles physics calculations with arbitrary decimal precision
    to eliminate floating point artifacts in critical simulations.
    """

    def __init__(self, precision: int = 50):
        """
        Initialize the engine with a specific precision context.
        
        Args:
            precision (int): Number of significant digits (default: 50)
        """
        self.precision = precision
        getcontext().prec = self.precision
        
        # Fundamental Constants (High Precision)
        self.c = Decimal('299792458')                  # Speed of light (m/s)
        self.G = Decimal('6.67430e-11')                # Gravitational constant
        self.h = Decimal('6.62607015e-34')             # Planck constant
        self.g0 = Decimal('9.80665')                   # Standard gravity

    def set_precision(self, prec: int):
        """Update global calculation precision."""
        self.precision = prec
        getcontext().prec = prec

    def to_decimal(self, value: Number) -> Decimal:
        """Safely convert any input to Decimal."""
        if isinstance(value, float):
            # Convert float to string first to avoid float artifacts
            return Decimal(str(value))
        return Decimal(value)

    def calculate_force_gravity(self, m1: Number, m2: Number, r: Number) -> Decimal:
        """
        Calculate Gravitational Force with high precision.
        F = G * (m1 * m2) / r^2
        """
        dm1 = self.to_decimal(m1)
        dm2 = self.to_decimal(m2)
        dr = self.to_decimal(r)
        
        return self.G * (dm1 * dm2) / (dr ** 2)

    def calculate_relativistic_energy(self, mass: Number) -> Decimal:
        """
        E = mc^2 (Exact)
        """
        dm = self.to_decimal(mass)
        return dm * (self.c ** 2)

    def kinematic_position(self, x0: Number, v0: Number, a: Number, t: Number) -> Decimal:
        """
        Exact kinematic position: x = x0 + v0*t + 0.5*a*t^2
        """
        dx0 = self.to_decimal(x0)
        dv0 = self.to_decimal(v0)
        da = self.to_decimal(a)
        dt = self.to_decimal(t)
        
        return dx0 + (dv0 * dt) + (Decimal('0.5') * da * (dt ** 2))

    def vector_magnitude(self, vector: List[Number]) -> Decimal:
        """
        Calculate magnitude of a vector in N-dimensions with high precision.
        |v| = sqrt(sum(x^2))
        """
        sum_sq = sum(self.to_decimal(x) ** 2 for x in vector)
        return sum_sq.sqrt()