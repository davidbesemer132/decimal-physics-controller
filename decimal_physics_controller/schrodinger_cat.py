"""
Schrödinger's Cat Quantum-Thermodynamic Simulation

Main orchestrator that integrates quantum entropy, thermodynamics,
AI control, and biological chaos into a complete simulation.

Based on the thought experiment combining:
- Deterministic AI (seed 42)
- Quantum mechanics (Von Neumann entropy)
- Thermodynamics (heat death)
- Biological chaos
"""

from decimal import Decimal, getcontext
from typing import Dict, List, Optional, Tuple
import random

from .quantum_entropy import QuantumState, QuantumZenoEffect
from .thermodynamics import ThermodynamicSystem, OptimizationDeath
from .ai_controller import DeterministicAIController


class SchrodingerCatSimulation:
    """
    Complete simulation of the deterministic Schrödinger's Cat experiment.
    
    Integrates:
    - Quantum state evolution with Von Neumann entropy
    - Thermodynamic heat death calculations  
    - AI controller with seed 42
    - Biological chaos and instinct
    - Decoherence and measurement effects
    """
    
    def __init__(
        self,
        seed: int = 42,
        precision: int = 50,
        cat_stubbornness: Decimal = Decimal('0.7')
    ):
        """
        Initialize complete simulation.
        
        Args:
            seed: Random seed for AI controller (default 42)
            precision: Decimal precision for calculations
            cat_stubbornness: Cat's resistance to control (0-1)
        """
        self.precision = precision
        getcontext().prec = precision
        
        # Initialize subsystems
        self.quantum_state = QuantumState(precision=precision)
        self.thermodynamics = ThermodynamicSystem(precision=precision)
        self.ai_controller = DeterministicAIController(seed=seed, precision=precision)
        self.optimization_death = OptimizationDeath(precision=precision)
        self.zeno_effect = QuantumZenoEffect(precision=precision)
        
        # Cat parameters
        self.cat_stubbornness = cat_stubbornness  # Resistance to AI control
        self.cat_activity = Decimal('0.5')  # Activity level (0=still, 1=hyperactive)
        self.cat_stress = Decimal('0.3')  # Stress level (0=calm, 1=panicked)
        self.cat_fascination = Decimal('0')  # Fascination with fractals (0-1)
        
        # Simulation state
        self.time = Decimal('0')  # seconds
        self.dt = Decimal('1')  # time step (1 second)
        self.history = []
        
        # Biological chaos tracking
        self.instinct_override_count = 0
        self.lcd_attack_count = 0
        
    def evolve_cat_behavior(self, lcd_pattern: str, photon_count: int) -> None:
        """
        Evolve cat's behavioral state based on LCD and instinct.
        
        Cat is not passive - responds chaotically to AI control attempts.
        
        Args:
            lcd_pattern: Current LCD pattern
            photon_count: Number of photons (measurement strength)
        """
        # Fractal pattern increases fascination
        if lcd_pattern == "fractal":
            self.cat_fascination += Decimal('0.1')
            self.cat_fascination = min(self.cat_fascination, Decimal('1'))
            
            # Fascination reduces activity
            self.cat_activity *= (Decimal('1') - self.cat_fascination * Decimal('0.5'))
            self.cat_stress *= Decimal('0.9')  # Calming effect
        
        # Strobe pattern increases stress (epileptogenic)
        elif lcd_pattern == "strobe":
            flash_rate = self.ai_controller.get_flash_rate(lcd_pattern)
            stress_increase = Decimal('0.2')
            
            # Critical frequency range (5-30 Hz) causes severe stress
            if Decimal('5') <= flash_rate <= Decimal('30'):
                stress_increase = Decimal('0.5')
            
            self.cat_stress += stress_increase
            self.cat_stress = min(self.cat_stress, Decimal('1'))
            
            # Stressed cat becomes more active (trying to escape)
            self.cat_activity += Decimal('0.3')
            self.cat_activity = min(self.cat_activity, Decimal('1'))
        
        # Random pattern - normal behavior
        else:
            # Cat gradually returns to baseline
            baseline_activity = Decimal('0.5')
            baseline_stress = Decimal('0.3')
            
            self.cat_activity += (baseline_activity - self.cat_activity) * Decimal('0.1')
            self.cat_stress += (baseline_stress - self.cat_stress) * Decimal('0.1')
        
        # Biological chaos: random instinctive behaviors
        # These break AI determinism
        if random.random() < float(self.cat_stubbornness * Decimal('0.1')):
            # Instinct override: cat does something unpredictable
            self.instinct_override_count += 1
            self.ai_controller.corrupt_seed(Decimal('0.1'))
            
            # Random activity spike
            self.cat_activity += Decimal(str(random.random())) * Decimal('0.5')
            self.cat_activity = min(self.cat_activity, Decimal('1'))
        
        # Cat might attack LCD (hack the system)
        if self.cat_stress > Decimal('0.8') and random.random() < 0.05:
            self.lcd_attack_count += 1
            self.ai_controller.corrupt_seed(Decimal('0.3'))
            # Attacking LCD increases activity, reduces stress momentarily
            self.cat_activity = Decimal('1')
            self.cat_stress *= Decimal('0.7')
    
    def get_cat_state(self) -> Dict:
        """
        Get complete cat state for reward calculation.
        
        Returns:
            Dictionary with cat parameters
        """
        return {
            'activity': float(self.cat_activity),
            'stress': float(self.cat_stress),
            'temperature': float(self.thermodynamics.temperature),
            'entropy': float(self.quantum_state.von_neumann_entropy()),
            'fascination': float(self.cat_fascination)
        }
    
    def step(self) -> None:
        """
        Execute one simulation time step.
        
        Integrates all subsystems:
        1. AI decides LCD pattern
        2. Cat responds (biological chaos)
        3. Quantum state evolves (decoherence, measurements)
        4. Thermodynamics evolves (heat generation)
        5. Rewards calculated and learned
        """
        # 1. AI optimization
        cat_state = self.get_cat_state()
        optimal_pattern = self.ai_controller.optimize_display(cat_state)
        photon_count = self.ai_controller.get_photon_flux(optimal_pattern)
        
        # 2. Set thermodynamic power based on pattern
        if optimal_pattern == "fractal":
            self.thermodynamics.set_power_mode('stasis')
        elif optimal_pattern == "strobe":
            self.thermodynamics.set_power_mode('strobe')
        else:
            self.thermodynamics.set_power_mode('normal')
        
        # 3. Cat behavioral evolution (biological chaos)
        self.evolve_cat_behavior(optimal_pattern, photon_count)
        
        # 4. Quantum state evolution
        # Photons cause measurements (decoherence)
        if photon_count > 0:
            measurement_strength = Decimal(min(photon_count, 1000)) / Decimal('1000')
            self.quantum_state.apply_measurement(
                photon_count=min(photon_count, 100),  # Limit for performance
                measurement_strength=measurement_strength * Decimal('0.01')
            )
        
        # Natural decoherence
        self.quantum_state.apply_decoherence(
            dt=self.dt,
            gamma=Decimal('0.001')
        )
        
        # Thermal decoherence (from heat)
        self.quantum_state.evolve_thermal(
            temperature=self.thermodynamics.temperature,
            dt=self.dt
        )
        
        # Zeno effect from strobe
        if optimal_pattern == "strobe":
            flash_rate = self.ai_controller.get_flash_rate(optimal_pattern)
            self.zeno_effect.apply_measurement_freeze(
                state=self.quantum_state,
                intensity=Decimal('0.5')
            )
        
        # 5. Thermodynamic evolution
        self.thermodynamics.evolve(dt=self.dt)
        
        # 6. Optimization death check
        immobility_time = Decimal('3600') * (Decimal('1') - self.cat_activity)
        self.optimization_death.update_wellbeing(
            cat_activity=self.cat_activity,
            cat_stress=self.cat_stress
        )
        
        # 7. AI learning
        reward = self.ai_controller.calculate_reward(cat_state)
        self.ai_controller.learn_from_reward(reward)
        
        # 8. Update time
        self.time += self.dt
        
        # 9. Record state
        self.history.append(self.get_complete_state())
    
    def run(self, duration_seconds: float) -> List[Dict]:
        """
        Run simulation for specified duration.
        
        Args:
            duration_seconds: Simulation duration in seconds
            
        Returns:
            List of state snapshots
        """
        steps = int(duration_seconds / float(self.dt))
        
        for _ in range(steps):
            # Check if cat is still alive
            if not self.thermodynamics.is_cat_alive():
                break
            
            self.step()
        
        return self.history
    
    def get_complete_state(self) -> Dict:
        """
        Get complete simulation state at current time.
        
        Returns:
            Dictionary with all subsystem states
        """
        state = {
            'time_seconds': float(self.time),
            'time_minutes': float(self.time / Decimal('60')),
            'time_hours': float(self.time / Decimal('3600')),
        }
        
        # Quantum state
        quantum = self.quantum_state.get_state()
        state['quantum'] = quantum
        state['entropy'] = quantum['entropy']
        state['coherence'] = quantum['coherence_factor']
        state['state_description'] = quantum['description']
        
        # Thermodynamics
        thermo = self.thermodynamics.get_state()
        state['thermodynamics'] = thermo
        state['temperature_celsius'] = thermo['temperature_celsius']
        state['is_alive'] = thermo['is_alive']
        state['time_to_death_minutes'] = thermo['time_to_death_minutes']
        
        # AI controller
        ai = self.ai_controller.get_state()
        state['ai'] = ai
        state['determinism'] = ai['determinism']
        
        # Cat behavior
        state['cat'] = {
            'activity': float(self.cat_activity),
            'stress': float(self.cat_stress),
            'fascination': float(self.cat_fascination),
            'instinct_overrides': self.instinct_override_count,
            'lcd_attacks': self.lcd_attack_count
        }
        
        # Optimization death
        opt = self.optimization_death.get_state()
        state['optimization'] = opt
        
        return state
    
    def get_summary(self) -> str:
        """
        Get human-readable summary of current state.
        
        Returns:
            Formatted summary string
        """
        state = self.get_complete_state()
        
        summary = f"""
╔════════════════════════════════════════════════════════════════════════════╗
║           SCHRÖDINGER'S CAT QUANTUM-THERMODYNAMIC SIMULATION              ║
╚════════════════════════════════════════════════════════════════════════════╝

TIME: {state['time_minutes']:.1f} minutes ({state['time_hours']:.2f} hours)

QUANTUM STATE:
  Entropy (S):        {state['entropy']:.4f} (0=pure, 1=mixed)
  Coherence:          {state['coherence']:.4f} (0=decoherent, 1=coherent)
  Description:        {state['state_description']}
  P(alive):           {state['quantum']['rho_alive']:.4f}
  P(dead):            {state['quantum']['rho_dead']:.4f}

THERMODYNAMICS:
  Temperature:        {state['temperature_celsius']:.2f}°C
  Power:              {state['thermodynamics']['power_watts']:.1f} W
  Time to death:      {state['time_to_death_minutes']:.1f} minutes
  Cause:              {state['thermodynamics']['cause_of_death']}
  Survival prob:      {state['thermodynamics']['survival_probability']:.3f}
  Is alive:           {state['is_alive']}

CAT BEHAVIOR:
  Activity:           {state['cat']['activity']:.3f} (0=still, 1=hyperactive)
  Stress:             {state['cat']['stress']:.3f} (0=calm, 1=panicked)
  Fascination:        {state['cat']['fascination']:.3f} (fractal hypnosis)
  Instinct overrides: {state['cat']['instinct_overrides']}
  LCD attacks:        {state['cat']['lcd_attacks']}

AI CONTROLLER:
  Determinism:        {state['determinism']:.3f} (seed corruption)
  Avg Reward:         {state['ai']['average_reward']:.3f}

OPTIMIZATION:
  Well-being score:   {state['optimization']['wellbeing_score']:.3f}

╚════════════════════════════════════════════════════════════════════════════╝
        """
        
        return summary
