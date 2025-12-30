import pytest
from decimal import Decimal
import numpy as np
from decimal_physics_controller import PhysicsController

class TestDecimalPhysics:
    
    def setup_method(self):
        """Initialize Engine before each test."""
        self.engine = PhysicsController(precision=50)

    def test_initialization(self):
        """Check if constants are loaded with correct precision."""
        # Light speed must be exact
        assert self.engine.c == Decimal('299792458')
        # Check context precision
        assert self.engine.precision == 50

    def test_relativistic_energy_integrity(self):
        """E = mc^2 must be precise for small masses."""
        mass = "1.0"
        energy = self.engine.calculate_relativistic_energy(mass)
        # Expected: 1.0 * (299792458)^2 = 89875517873681764
        expected = Decimal('89875517873681764')
        assert energy == expected

    def test_precision_superiority(self):
        """
        THE ANT CORP PROOF:
        Demonstrate where Float fails and Decimal succeeds.
        Scenario: Subtracting two massive, nearly identical numbers.
        """
        # A massive number with a tiny difference
        # Float has about 15-17 digits of precision.
        # We use numbers that exceed this to break float.
        val_a_str = "100000000000000000000.00000000000000001"
        val_b_str = "100000000000000000000.00000000000000000"
        
        # 1. The Decimal Way (The ANT Way)
        dec_a = Decimal(val_a_str)
        dec_b = Decimal(val_b_str)
        diff_decimal = dec_a - dec_b
        
        # 2. The Standard Way (The Float Way)
        flt_a = float(val_a_str)
        flt_b = float(val_b_str)
        diff_float = flt_a - flt_b
        
        print(f"\nANT PROOF:")
        print(f"Decimal Diff: {diff_decimal}")
        print(f"Float Diff:   {diff_float}")

        # Assertion: Decimal captures the 1e-17 diff, Float returns 0.0 (Data Loss)
        assert diff_decimal == Decimal("0.00000000000000001")
        assert diff_float == 0.0 or diff_float != 1e-17

    def test_gravity_accuracy(self):
        """Check gravitational force calculation."""
        # Earth-Moon approximation
        m1 = 5.972e24
        m2 = 7.348e22
        r = 384400000
        
        f = self.engine.calculate_force_gravity(m1, m2, r)
        
        # Rough check to ensure magnitude is correct (~1.98e20 N)
        assert f > Decimal('1.9e20')
        assert f < Decimal('2.1e20')