"""
Tests for Schrödinger's Cat Quantum-Thermodynamic Simulation

Tests all components:
- Quantum entropy calculations
- Thermodynamic evolution
- AI controller with seed 42
- Integrated simulation
"""

import pytest
from decimal import Decimal
from decimal_physics_controller import (
    SchrodingerCatSimulation,
    QuantumState,
    QuantumZenoEffect,
    ThermodynamicSystem,
    OptimizationDeath,
    DeterministicAIController
)


class TestQuantumState:
    """Test quantum entropy and state evolution."""
    
    def setup_method(self):
        """Initialize quantum state before each test."""
        self.state = QuantumState(precision=50)
    
    def test_initial_pure_state(self):
        """Test that initial state is pure (S ≈ 0)."""
        entropy = self.state.von_neumann_entropy()
        assert entropy < Decimal('0.01'), "Initial state should be pure"
        assert self.state.rho_alive == Decimal('1.0')
        assert self.state.rho_dead == Decimal('0.0')
    
    def test_von_neumann_entropy_bounds(self):
        """Test that entropy is bounded [0, 1]."""
        # Pure state
        entropy_pure = self.state.von_neumann_entropy()
        assert Decimal('0') <= entropy_pure <= Decimal('1')
        
        # Mixed state
        self.state.rho_alive = Decimal('0.5')
        self.state.rho_dead = Decimal('0.5')
        entropy_mixed = self.state.von_neumann_entropy()
        assert Decimal('0') <= entropy_mixed <= Decimal('1')
        assert entropy_mixed > entropy_pure
    
    def test_maximally_mixed_state(self):
        """Test that 50/50 mixture has maximum entropy."""
        self.state.rho_alive = Decimal('0.5')
        self.state.rho_dead = Decimal('0.5')
        entropy = self.state.von_neumann_entropy()
        # Maximum entropy for 2-level system normalized to 1
        assert entropy > Decimal('0.99'), "50/50 state should have S ≈ 1"
    
    def test_decoherence_reduces_coherence(self):
        """Test that decoherence reduces coherence over time."""
        self.state.coherence = Decimal('1.0')
        initial_coherence = self.state.coherence
        
        # Apply decoherence
        self.state.apply_decoherence(dt=Decimal('10'), gamma=Decimal('0.001'))
        
        assert self.state.coherence < initial_coherence
    
    def test_thermal_decoherence(self):
        """Test thermal decoherence increases entropy."""
        initial_entropy = self.state.von_neumann_entropy()
        
        # Apply thermal evolution at high temperature
        self.state.evolve_thermal(temperature=Decimal('400'), dt=Decimal('100'))
        
        final_entropy = self.state.von_neumann_entropy()
        assert final_entropy > initial_entropy
    
    def test_measurement_increases_entropy(self):
        """Test that measurements push toward mixed state."""
        initial_entropy = self.state.von_neumann_entropy()
        
        # Apply many measurements
        self.state.apply_measurement(photon_count=100, measurement_strength=Decimal('0.1'))
        
        final_entropy = self.state.von_neumann_entropy()
        assert final_entropy > initial_entropy
    
    def test_state_descriptions(self):
        """Test state description classifications."""
        # God state (low entropy)
        self.state.rho_alive = Decimal('0.9')
        self.state.rho_dead = Decimal('0.1')
        assert "God" in self.state.get_state_description()
        
        # Zombie state (high entropy)
        self.state.rho_alive = Decimal('0.5')
        self.state.rho_dead = Decimal('0.5')
        assert "Zombie" in self.state.get_state_description()


class TestThermodynamicSystem:
    """Test thermodynamic calculations."""
    
    def setup_method(self):
        """Initialize thermodynamic system before each test."""
        self.system = ThermodynamicSystem(precision=50)
    
    def test_initial_conditions(self):
        """Test initial system parameters."""
        assert self.system.temperature == Decimal('293.15')  # 20°C
        assert self.system.heat_capacity == Decimal('17950')
        assert self.system.volume == Decimal('1.0')
    
    def test_power_modes(self):
        """Test power mode switching."""
        self.system.set_power_mode('stasis')
        assert self.system.current_power == self.system.power_min
        
        self.system.set_power_mode('strobe')
        assert self.system.current_power == self.system.power_max
    
    def test_temperature_increases_with_time(self):
        """Test that temperature increases due to heat generation."""
        initial_temp = self.system.temperature
        
        # Evolve for 1 minute at max power
        self.system.set_power_mode('strobe')
        self.system.evolve(dt=Decimal('60'))
        
        assert self.system.temperature > initial_temp
    
    def test_time_to_heat_death_calculation(self):
        """Test heat death time calculation."""
        self.system.set_power_mode('strobe')
        time_to_death = self.system.time_to_heat_death()
        
        # Should be approximately 28 minutes (1680 seconds)
        expected_time = Decimal('1680')  # seconds
        tolerance = Decimal('200')  # ±200 seconds tolerance
        
        assert abs(time_to_death - expected_time) < tolerance
    
    def test_cat_death_conditions(self):
        """Test that cat dies under extreme conditions."""
        # Initially alive
        assert self.system.is_cat_alive()
        
        # Simulate heat death
        self.system.temperature = Decimal('315.15')  # 42°C
        assert not self.system.is_cat_alive()
    
    def test_survival_probability_decreases(self):
        """Test that survival probability decreases over time."""
        initial_prob = self.system.get_survival_probability()
        
        # Evolve for a long time
        self.system.set_power_mode('strobe')
        for _ in range(100):
            self.system.evolve(dt=Decimal('60'))
        
        final_prob = self.system.get_survival_probability()
        assert final_prob < initial_prob


class TestDeterministicAIController:
    """Test AI controller with seed 42."""
    
    def setup_method(self):
        """Initialize AI controller before each test."""
        self.ai = DeterministicAIController(seed=42, precision=50)
    
    def test_deterministic_behavior(self):
        """Test that seed 42 produces reproducible results."""
        # Create two controllers with same seed
        ai1 = DeterministicAIController(seed=42)
        ai2 = DeterministicAIController(seed=42)
        
        # Generate patterns
        pattern1 = ai1.update_lcd('random')
        pattern2 = ai2.update_lcd('random')
        
        # Should be identical
        assert pattern1 == pattern2
    
    def test_seed_corruption_breaks_determinism(self):
        """Test that seed corruption introduces randomness."""
        ai1 = DeterministicAIController(seed=42)
        ai2 = DeterministicAIController(seed=42)
        
        # Corrupt one controller
        ai2.corrupt_seed(Decimal('0.8'))
        
        # Results should differ after corruption
        results1 = [ai1.update_lcd('random') for _ in range(10)]
        results2 = [ai2.update_lcd('random') for _ in range(10)]
        
        # At least some results should differ
        assert results1 != results2
    
    def test_fractal_pattern_generation(self):
        """Test Mandelbrot fractal generation."""
        photon_count = self.ai.update_lcd('fractal')
        
        # Fractal should produce some lit pixels
        assert photon_count > 0
        assert photon_count < self.ai.lcd_width * self.ai.lcd_height
    
    def test_strobe_pattern(self):
        """Test stroboscope pattern."""
        photon_count = self.ai.update_lcd('strobe')
        
        # Strobe should be either all on or all off
        total_pixels = self.ai.lcd_width * self.ai.lcd_height
        assert photon_count == 0 or photon_count == total_pixels
    
    def test_reward_calculation(self):
        """Test reward function."""
        cat_state = {
            'stress': 0.2,
            'activity': 0.5,
            'temperature': 293.15,
            'entropy': 0.3
        }
        
        reward = self.ai.calculate_reward(cat_state)
        
        # Reward should be in [0, 1]
        assert Decimal('0') <= reward <= Decimal('1')
    
    def test_flash_rate_by_pattern(self):
        """Test flash rates for different patterns."""
        strobe_rate = self.ai.get_flash_rate('strobe')
        fractal_rate = self.ai.get_flash_rate('fractal')
        
        # Strobe should have high flash rate
        assert strobe_rate > Decimal('5')
        
        # Fractal should be static
        assert fractal_rate == Decimal('0')


class TestQuantumZenoEffect:
    """Test Quantum Zeno Effect."""
    
    def setup_method(self):
        """Initialize Zeno effect simulator."""
        self.zeno = QuantumZenoEffect(precision=50)
        self.state = QuantumState(precision=50)
    
    def test_measurement_freeze(self):
        """Test that measurements freeze quantum evolution."""
        initial_coherence = self.state.coherence
        
        # Apply Zeno measurement
        self.zeno.apply_measurement_freeze(self.state, intensity=Decimal('0.8'))
        
        # Coherence should be reduced
        assert self.state.coherence <= initial_coherence
    
    def test_epileptic_stress_calculation(self):
        """Test epileptic stress from flashing."""
        # Critical frequency (15 Hz) should cause high stress
        stress_critical = self.zeno.calculate_epileptic_stress(
            flash_rate=Decimal('15'),
            duration=Decimal('60')
        )
        
        # Non-critical frequency should cause less stress
        stress_normal = self.zeno.calculate_epileptic_stress(
            flash_rate=Decimal('2'),
            duration=Decimal('60')
        )
        
        assert stress_critical > stress_normal


class TestOptimizationDeath:
    """Test optimization death scenarios."""
    
    def setup_method(self):
        """Initialize optimization death simulator."""
        self.opt = OptimizationDeath(precision=50)
    
    def test_wellbeing_calculation(self):
        """Test AI well-being calculation."""
        # Low stress should give high well-being
        self.opt.update_wellbeing(
            cat_activity=Decimal('0.5'),
            cat_stress=Decimal('0.1')
        )
        assert self.opt.wellbeing_score > Decimal('0.8')
    
    def test_hypnosis_effect(self):
        """Test hypnosis immobilization."""
        # Short duration
        short_immobilization = self.opt.apply_hypnosis(Decimal('60'))
        
        # Long duration
        long_immobilization = self.opt.apply_hypnosis(Decimal('3600'))
        
        assert long_immobilization > short_immobilization
    
    def test_optimization_death_risk(self):
        """Test death risk from over-optimization."""
        # Short immobility - no risk
        short_risk = self.opt.calculate_optimization_death_risk(Decimal('1800'))
        assert short_risk == Decimal('0')
        
        # Long immobility - high risk
        long_risk = self.opt.calculate_optimization_death_risk(Decimal('10800'))
        assert long_risk > Decimal('0.5')


class TestSchrodingerCatSimulation:
    """Test complete integrated simulation."""
    
    def setup_method(self):
        """Initialize simulation before each test."""
        self.sim = SchrodingerCatSimulation(seed=42, precision=50)
    
    def test_initialization(self):
        """Test simulation initialization."""
        assert self.sim.time == Decimal('0')
        assert self.sim.quantum_state is not None
        assert self.sim.thermodynamics is not None
        assert self.sim.ai_controller is not None
    
    def test_single_step(self):
        """Test single simulation step."""
        initial_time = self.sim.time
        initial_entropy = self.sim.quantum_state.von_neumann_entropy()
        
        self.sim.step()
        
        # Time should advance
        assert self.sim.time > initial_time
        
        # State should be recorded
        assert len(self.sim.history) == 1
    
    def test_entropy_increases_over_time(self):
        """Test that entropy generally increases (second law analog)."""
        initial_entropy = self.sim.quantum_state.von_neumann_entropy()
        
        # Run for 10 minutes
        self.sim.run(duration_seconds=600)
        
        final_entropy = self.sim.quantum_state.von_neumann_entropy()
        
        # Entropy should increase due to decoherence
        assert final_entropy > initial_entropy
    
    def test_cat_death_stops_simulation(self):
        """Test that simulation stops when cat dies."""
        # Force high power for quick heat death
        self.sim.thermodynamics.set_power_mode('strobe')
        
        # Run for long duration
        self.sim.run(duration_seconds=3600)
        
        # Cat should be dead before 1 hour at max power
        final_state = self.sim.get_complete_state()
        assert not final_state['is_alive']
    
    def test_biological_chaos_corrupts_seed(self):
        """Test that cat behavior corrupts determinism."""
        # High stubbornness
        sim = SchrodingerCatSimulation(
            seed=42,
            cat_stubbornness=Decimal('0.9')
        )
        
        initial_determinism = sim.ai_controller.seed_corruption
        
        # Run simulation
        sim.run(duration_seconds=600)
        
        final_determinism = sim.ai_controller.seed_corruption
        
        # Seed should be corrupted
        assert final_determinism > initial_determinism
    
    def test_fractal_mode_reduces_activity(self):
        """Test that fractal mode reduces cat activity."""
        sim = SchrodingerCatSimulation(seed=42, cat_stubbornness=Decimal('0.2'))
        
        # Force fractal mode
        sim.ai_controller.current_mode = "fractal"
        sim.thermodynamics.set_power_mode('stasis')
        
        initial_activity = sim.cat_activity
        
        # Run for some time
        for _ in range(600):  # 10 minutes
            sim.step()
        
        final_activity = sim.cat_activity
        
        # Activity should decrease (hypnosis effect)
        assert final_activity < initial_activity
    
    def test_complete_state_structure(self):
        """Test that complete state has all required fields."""
        state = self.sim.get_complete_state()
        
        # Check main sections exist
        assert 'time_seconds' in state
        assert 'quantum' in state
        assert 'thermodynamics' in state
        assert 'ai' in state
        assert 'cat' in state
        assert 'optimization' in state
        
        # Check key values
        assert 'entropy' in state
        assert 'is_alive' in state
        assert 'determinism' in state
    
    def test_summary_generation(self):
        """Test that summary can be generated."""
        summary = self.sim.get_summary()
        
        # Should contain key information
        assert 'QUANTUM STATE' in summary
        assert 'THERMODYNAMICS' in summary
        assert 'CAT BEHAVIOR' in summary
        assert 'AI CONTROLLER' in summary


class TestIntegration:
    """Integration tests for complete scenarios."""
    
    def test_heat_death_scenario(self):
        """Test complete heat death scenario."""
        sim = SchrodingerCatSimulation(seed=42)
        sim.thermodynamics.set_power_mode('strobe')
        
        # Run until death
        sim.run(duration_seconds=3600)
        
        final_state = sim.get_complete_state()
        
        # Should die from heat or thirst
        assert not final_state['is_alive']
        assert final_state['thermodynamics']['cause_of_death'] in ['heat', 'thirst']
    
    def test_deterministic_reproducibility(self):
        """Test that same seed produces same results."""
        sim1 = SchrodingerCatSimulation(seed=42, cat_stubbornness=Decimal('0.1'))
        sim2 = SchrodingerCatSimulation(seed=42, cat_stubbornness=Decimal('0.1'))
        
        # Run both for same duration
        sim1.run(duration_seconds=60)
        sim2.run(duration_seconds=60)
        
        # States should be very similar (not identical due to decimal precision)
        state1 = sim1.get_complete_state()
        state2 = sim2.get_complete_state()
        
        # Key values should match closely
        assert abs(state1['entropy'] - state2['entropy']) < 0.01
        assert abs(state1['temperature_celsius'] - state2['temperature_celsius']) < 0.1
