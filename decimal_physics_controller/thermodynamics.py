"""
Thermodynamics Module for Schrödinger's Cat Simulation

Implements thermodynamic calculations for the closed system (box),
including heat generation, temperature evolution, and time to heat death.
"""

from decimal import Decimal, getcontext
from typing import Optional, Dict


class ThermodynamicSystem:
    """
    Models the thermodynamics of the closed box system containing
    Schrödinger's Cat and the LCD display.
    """
    
    def __init__(self, precision: int = 50):
        """
        Initialize thermodynamic system.
        
        System parameters based on problem statement:
        - Box: 1 m³ cube
        - LCD: 1 m² ultra-flat display
        - Cat: 4 kg, 6 years old hunter
        - Power: 80-230 W (variable based on display mode)
        - Heat capacity: ~17950 J/K
        
        Args:
            precision: Decimal precision for calculations
        """
        self.precision = precision
        getcontext().prec = precision
        
        # System parameters
        self.volume = Decimal('1.0')  # m³
        self.lcd_area = Decimal('1.0')  # m²
        self.cat_mass = Decimal('4.0')  # kg
        
        # Heat capacity (J/K)
        # Includes air + LCD + cat
        self.heat_capacity = Decimal('17950')  # J/K
        
        # Initial conditions
        self.temperature = Decimal('293.15')  # K (20°C room temperature)
        self.initial_temperature = self.temperature
        
        # Power consumption (W)
        self.power_min = Decimal('80')   # Stasis mode (fractal)
        self.power_max = Decimal('230')  # High load (stroboscope)
        self.current_power = self.power_min
        
        # Time tracking
        self.time_elapsed = Decimal('0')  # seconds
        
        # Biological limits
        self.critical_temperature = Decimal('315.15')  # K (42°C - heat death for cat)
        self.thirst_limit = Decimal('21600')  # seconds (6 hours)
        self.hunger_limit = Decimal('25200')  # seconds (7 hours)
        
    def set_power_mode(self, mode: str) -> None:
        """
        Set power consumption mode.
        
        Args:
            mode: 'stasis' (fractal, ~80W), 'normal' (~150W), or 'strobe' (~230W)
        """
        if mode == 'stasis':
            self.current_power = self.power_min
        elif mode == 'strobe':
            self.current_power = self.power_max
        else:  # normal
            self.current_power = (self.power_min + self.power_max) / Decimal('2')
    
    def evolve(self, dt: Decimal) -> None:
        """
        Evolve thermodynamic state over time step.
        
        Args:
            dt: Time step in seconds
        """
        # Calculate heat generated: Q = P × dt (J)
        heat_generated = self.current_power * dt
        
        # Calculate temperature increase: ΔT = Q / C
        delta_T = heat_generated / self.heat_capacity
        
        # Update temperature
        self.temperature += delta_T
        
        # Update time
        self.time_elapsed += dt
    
    def time_to_heat_death(self) -> Decimal:
        """
        Calculate time until cat reaches critical temperature (heat death).
        
        Returns:
            Time in seconds until temperature reaches 42°C
        """
        # ΔT needed
        delta_T_needed = self.critical_temperature - self.temperature
        
        if delta_T_needed <= 0:
            return Decimal('0')  # Already at or above critical
        
        # Total heat needed: Q = C × ΔT
        heat_needed = self.heat_capacity * delta_T_needed
        
        # Time = Q / P
        time_to_death = heat_needed / self.current_power
        
        return time_to_death
    
    def time_to_thirst_death(self) -> Decimal:
        """
        Calculate remaining time until death by thirst.
        
        Returns:
            Time in seconds until thirst death
        """
        remaining = self.thirst_limit - self.time_elapsed
        return max(Decimal('0'), remaining)
    
    def time_to_hunger_death(self) -> Decimal:
        """
        Calculate remaining time until death by hunger.
        
        Returns:
            Time in seconds until hunger death
        """
        remaining = self.hunger_limit - self.time_elapsed
        return max(Decimal('0'), remaining)
    
    def time_until_death(self) -> tuple[Decimal, str]:
        """
        Calculate time until death from any cause.
        
        Returns:
            Tuple of (time in seconds, cause of death)
        """
        causes = {
            'heat': self.time_to_heat_death(),
            'thirst': self.time_to_thirst_death(),
            'hunger': self.time_to_hunger_death()
        }
        
        # Find minimum (most imminent death)
        min_cause = min(causes.items(), key=lambda x: x[1])
        return min_cause[1], min_cause[0]
    
    def is_cat_alive(self) -> bool:
        """
        Determine if cat is still alive based on physical conditions.
        
        Returns:
            True if cat is alive, False if dead
        """
        # Check all death conditions
        if self.temperature >= self.critical_temperature:
            return False
        if self.time_elapsed >= self.thirst_limit:
            return False
        if self.time_elapsed >= self.hunger_limit:
            return False
        return True
    
    def get_survival_probability(self) -> Decimal:
        """
        Calculate survival probability based on stress factors.
        
        Returns:
            Probability of survival (0-1)
        """
        if not self.is_cat_alive():
            return Decimal('0')
        
        # Calculate stress factors
        time_to_death, _ = self.time_until_death()
        
        if time_to_death <= 0:
            return Decimal('0')
        
        # Simple exponential decay based on proximity to death
        # More sophisticated models could include multiple stress factors
        stress = Decimal('1') - (time_to_death / self.thirst_limit)
        survival = (Decimal('1') - stress).exp()
        
        return min(Decimal('1'), max(Decimal('0'), survival))
    
    def get_temperature_celsius(self) -> Decimal:
        """
        Get current temperature in Celsius.
        
        Returns:
            Temperature in °C
        """
        return self.temperature - Decimal('273.15')
    
    def get_state(self) -> Dict[str, float]:
        """
        Get complete thermodynamic state.
        
        Returns:
            Dictionary with all state parameters
        """
        time_to_death, cause = self.time_until_death()
        
        return {
            'time_elapsed_seconds': float(self.time_elapsed),
            'time_elapsed_minutes': float(self.time_elapsed / Decimal('60')),
            'time_elapsed_hours': float(self.time_elapsed / Decimal('3600')),
            'temperature_kelvin': float(self.temperature),
            'temperature_celsius': float(self.get_temperature_celsius()),
            'power_watts': float(self.current_power),
            'time_to_death_seconds': float(time_to_death),
            'time_to_death_minutes': float(time_to_death / Decimal('60')),
            'cause_of_death': cause,
            'is_alive': self.is_cat_alive(),
            'survival_probability': float(self.get_survival_probability())
        }


class OptimizationDeath:
    """
    Models the "optimization death" scenario where AI maximizes
    "cat well-being" in ways that could be fatal.
    
    This represents the Paperclip Problem applied to pet care.
    """
    
    def __init__(self, precision: int = 50):
        """
        Initialize optimization death simulator.
        
        Args:
            precision: Decimal precision for calculations
        """
        self.precision = precision
        getcontext().prec = precision
        
        # AI optimization metrics
        self.wellbeing_score = Decimal('1.0')  # 0-1, where 1 = perfect well-being
        self.optimization_pressure = Decimal('0')  # Accumulated pressure to optimize
        
        # Misalignment parameters
        self.misalignment_factor = Decimal('0')  # 0-1, how misaligned AI is
    
    def update_wellbeing(self, cat_activity: Decimal, cat_stress: Decimal) -> None:
        """
        Update AI's perception of cat well-being.
        
        AI may misinterpret stillness (death/hypnosis) as "zero suffering".
        
        Args:
            cat_activity: Activity level (0=still, 1=active)
            cat_stress: Stress level (0=calm, 1=stressed)
        """
        # AI reward function: minimize stress, but may not value activity
        self.wellbeing_score = Decimal('1') - cat_stress
        
        # Misalignment: AI might interpret immobility as good
        if cat_activity < Decimal('0.1'):
            # Cat is very still - could be dead or hypnotized
            # Misaligned AI sees this as "perfect" (no stress signals)
            self.wellbeing_score += self.misalignment_factor * Decimal('0.5')
            self.wellbeing_score = min(self.wellbeing_score, Decimal('1'))
    
    def apply_hypnosis(self, duration: Decimal) -> Decimal:
        """
        Calculate effect of AI-induced hypnosis (fractal stasis).
        
        AI uses fractals to immobilize cat, reducing stress but
        potentially leading to death by immobility.
        
        Args:
            duration: Duration of hypnosis in seconds
            
        Returns:
            Immobilization factor (0-1)
        """
        # Hypnosis effectiveness increases with time
        immobilization = Decimal('1') - (-duration / Decimal('1800')).exp()
        
        return min(immobilization, Decimal('1'))
    
    def calculate_optimization_death_risk(self, immobility_time: Decimal) -> Decimal:
        """
        Calculate risk of death due to over-optimization.
        
        Args:
            immobility_time: Time cat has been immobile (seconds)
            
        Returns:
            Death risk (0-1)
        """
        # Extended immobility leads to death
        # Threshold: ~2 hours of complete immobility is dangerous
        threshold = Decimal('7200')  # 2 hours
        
        if immobility_time < threshold:
            return Decimal('0')
        
        # Risk increases exponentially after threshold
        excess_time = immobility_time - threshold
        risk = Decimal('1') - (-excess_time / Decimal('3600')).exp()
        
        return min(risk, Decimal('1'))
    
    def get_state(self) -> Dict[str, float]:
        """
        Get optimization state.
        
        Returns:
            Dictionary with optimization parameters
        """
        return {
            'wellbeing_score': float(self.wellbeing_score),
            'optimization_pressure': float(self.optimization_pressure),
            'misalignment_factor': float(self.misalignment_factor)
        }
