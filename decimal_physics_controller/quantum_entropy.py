"""
Quantum Entropy Module for Schrödinger's Cat Simulation

Implements Von Neumann entropy and quantum decoherence calculations
using high-precision decimal arithmetic.
"""

import decimal
from decimal import Decimal, getcontext
from typing import List, Tuple, Optional
import math


class QuantumState:
    """
    Represents a quantum state for the Schrödinger's Cat experiment.
    Models the cat as a two-level quantum system (|alive⟩, |dead⟩).
    """
    
    def __init__(self, precision: int = 50):
        """
        Initialize quantum state.
        
        Args:
            precision: Decimal precision for calculations
        """
        self.precision = precision
        getcontext().prec = precision
        
        # Initial pure state: cat is alive with certainty
        # Density matrix ρ = |ψ⟩⟨ψ| for pure state |alive⟩
        self.rho_alive = Decimal('1.0')  # Probability amplitude for |alive⟩
        self.rho_dead = Decimal('0.0')   # Probability amplitude for |dead⟩
        self.coherence = Decimal('0.0')  # Off-diagonal element (real part)
        
        # Physical constants
        self.hbar = Decimal('1.054571817e-34')  # Reduced Planck constant (J·s)
        self.kB = Decimal('1.380649e-23')       # Boltzmann constant (J/K)
    
    def von_neumann_entropy(self) -> Decimal:
        """
        Calculate Von Neumann entropy: S = -Tr(ρ log ρ)
        
        For a 2x2 density matrix, this reduces to:
        S = -p₁ log(p₁) - p₂ log(p₂)
        
        Where p₁ and p₂ are eigenvalues (probabilities).
        
        Returns:
            Von Neumann entropy (0 = pure state, 1 = maximum mixed state)
        """
        # Avoid log(0) by handling edge cases
        if self.rho_alive <= 0:
            term1 = Decimal('0')
        else:
            term1 = self.rho_alive * self.rho_alive.ln()
        
        if self.rho_dead <= 0:
            term2 = Decimal('0')
        else:
            term2 = self.rho_dead * self.rho_dead.ln()
        
        entropy = -(term1 + term2)
        
        # Normalize to [0, 1] range (divide by ln(2) for 2-level system)
        ln2 = Decimal('2').ln()
        if entropy > 0:
            entropy = entropy / ln2
        
        return entropy
    
    def apply_decoherence(self, dt: Decimal, gamma: Decimal = Decimal('0.001')) -> None:
        """
        Apply decoherence to the quantum state.
        
        Decoherence causes the off-diagonal elements of the density matrix
        to decay exponentially, destroying quantum coherence.
        
        Args:
            dt: Time step (seconds)
            gamma: Decoherence rate (1/s), default 0.001/s
        """
        # Exponential decay of coherence: coherence *= exp(-gamma * dt)
        decay_factor = (-gamma * dt).exp()
        self.coherence *= decay_factor
    
    def apply_measurement(self, photon_count: int, measurement_strength: Decimal = Decimal('0.01')) -> None:
        """
        Apply quantum measurement effects from LCD photons.
        
        Each photon interaction causes partial wavefunction collapse,
        increasing decoherence and moving towards a mixed state.
        
        Args:
            photon_count: Number of photon interactions
            measurement_strength: Strength of each measurement (0-1)
        """
        for _ in range(photon_count):
            # Each measurement pushes state towards classical mixture
            # Increase dead probability slightly
            transfer = measurement_strength * self.rho_alive * Decimal('0.001')
            self.rho_alive -= transfer
            self.rho_dead += transfer
            
            # Renormalize to maintain probability conservation
            total = self.rho_alive + self.rho_dead
            if total > 0:
                self.rho_alive /= total
                self.rho_dead /= total
            
            # Reduce coherence
            self.coherence *= (Decimal('1') - measurement_strength)
    
    def evolve_thermal(self, temperature: Decimal, dt: Decimal) -> None:
        """
        Apply thermal decoherence due to heat.
        
        Higher temperatures increase decoherence rate and push towards
        thermal equilibrium (maximally mixed state).
        
        Args:
            temperature: Temperature in Kelvin
            dt: Time step (seconds)
        """
        # Thermal decoherence rate increases with temperature
        # γ_thermal = kT/ℏ (simplified model)
        thermal_gamma = (self.kB * temperature) / self.hbar
        
        # Apply enhanced decoherence
        self.apply_decoherence(dt, thermal_gamma)
        
        # Move towards thermal equilibrium (50/50 mixture)
        thermal_rate = Decimal('0.0001') * temperature / Decimal('300')  # Normalized to room temp
        
        equilibrium_alive = Decimal('0.5')
        equilibrium_dead = Decimal('0.5')
        
        self.rho_alive += (equilibrium_alive - self.rho_alive) * thermal_rate * dt
        self.rho_dead += (equilibrium_dead - self.rho_dead) * thermal_rate * dt
    
    def is_pure_state(self, threshold: Decimal = Decimal('0.01')) -> bool:
        """
        Check if state is approximately pure.
        
        Args:
            threshold: Entropy threshold for pure state
            
        Returns:
            True if entropy < threshold
        """
        return self.von_neumann_entropy() < threshold
    
    def is_mixed_state(self, threshold: Decimal = Decimal('0.99')) -> bool:
        """
        Check if state is approximately maximally mixed.
        
        Args:
            threshold: Entropy threshold for mixed state
            
        Returns:
            True if entropy > threshold
        """
        return self.von_neumann_entropy() > threshold
    
    def coherence_factor(self) -> Decimal:
        """
        Calculate coherence factor (0 = fully decoherent, 1 = fully coherent).
        
        Returns:
            Coherence measure based on off-diagonal elements
        """
        # Simplified coherence measure
        max_coherence = Decimal('2') * (self.rho_alive * self.rho_dead).sqrt()
        if max_coherence > 0:
            return abs(self.coherence) / max_coherence
        return Decimal('0')
    
    def get_state_description(self) -> str:
        """
        Get human-readable state description.
        
        Returns:
            Description of quantum state (God/Zombie/Transition)
        """
        entropy = self.von_neumann_entropy()
        
        if entropy < Decimal('0.5'):
            return "God (low entropy, high coherence)"
        elif entropy > Decimal('0.5'):
            return "Zombie (high entropy, decoherent)"
        else:
            return "Transition (critical entropy)"
    
    def get_state(self) -> dict:
        """
        Get complete state information.
        
        Returns:
            Dictionary with all state parameters
        """
        return {
            'rho_alive': float(self.rho_alive),
            'rho_dead': float(self.rho_dead),
            'coherence': float(self.coherence),
            'entropy': float(self.von_neumann_entropy()),
            'coherence_factor': float(self.coherence_factor()),
            'description': self.get_state_description()
        }


class QuantumZenoEffect:
    """
    Models the Quantum Zeno Effect where frequent measurements
    can "freeze" quantum evolution.
    """
    
    def __init__(self, precision: int = 50):
        """
        Initialize Quantum Zeno Effect simulator.
        
        Args:
            precision: Decimal precision for calculations
        """
        self.precision = precision
        getcontext().prec = precision
        
        self.measurement_count = 0
        self.freeze_factor = Decimal('1.0')
    
    def apply_measurement_freeze(self, state: QuantumState, intensity: Decimal) -> None:
        """
        Apply Zeno effect from frequent measurements (LCD flashes).
        
        Frequent measurements inhibit state evolution but add noise
        from unknown seed.
        
        Args:
            state: Quantum state to affect
            intensity: Measurement intensity (0-1)
        """
        self.measurement_count += 1
        
        # Zeno effect: reduce natural evolution
        # But also add decoherence from measurement disturbance
        self.freeze_factor = Decimal('1.0') - intensity * Decimal('0.5')
        
        # Measurement disturbs the state (back-action)
        disturbance = intensity * Decimal('0.1')
        state.coherence *= (Decimal('1') - disturbance)
    
    def calculate_epileptic_stress(self, flash_rate: Decimal, duration: Decimal) -> Decimal:
        """
        Calculate cumulative neurological stress from flashing LCD.
        
        Args:
            flash_rate: Flashes per second
            duration: Duration in seconds
            
        Returns:
            Stress level (0-1, where 1 = severe)
        """
        # Critical frequency range: 5-30 Hz (most epileptogenic)
        critical_low = Decimal('5')
        critical_high = Decimal('30')
        
        if critical_low <= flash_rate <= critical_high:
            # Maximum stress in critical range
            stress_per_second = Decimal('0.1')
        else:
            # Reduced stress outside critical range
            stress_per_second = Decimal('0.01')
        
        total_stress = stress_per_second * duration
        
        # Clamp to [0, 1]
        return min(total_stress, Decimal('1.0'))
