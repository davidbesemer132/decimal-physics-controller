"""
AI Controller Module for Schrödinger's Cat Simulation

Implements deterministic AI control with seed 42, LCD pixel control,
and reward function optimization.
"""

import random
from decimal import Decimal, getcontext
from typing import List, Tuple, Optional


class DeterministicAIController:
    """
    AI controller with deterministic seed 42 for reproducible behavior.
    
    Controls LCD display to optimize "cat well-being" but determinism
    is broken by biological chaos and quantum effects.
    """
    
    def __init__(self, seed: int = 42, precision: int = 50):
        """
        Initialize AI controller.
        
        Args:
            seed: Random seed for deterministic behavior (default 42)
            precision: Decimal precision for calculations
        """
        self.seed = seed
        self.precision = precision
        getcontext().prec = precision
        
        # Set deterministic seed
        random.seed(self.seed)
        
        # LCD state (1 m² display, divided into pixel groups)
        self.lcd_width = 100  # Logical pixel groups
        self.lcd_height = 100
        self.lcd_state = [[0 for _ in range(self.lcd_width)] for _ in range(self.lcd_height)]
        
        # AI learning state
        self.reward_history = []
        self.learning_rate = Decimal('0.01')
        self.reward_function = "cat_wellbeing"
        
        # Control modes
        self.current_mode = "normal"  # 'normal', 'fractal', 'strobe'
        
        # Determinism tracking
        self.seed_corruption = Decimal('0')  # 0 = perfect determinism, 1 = chaos
    
    def reset_seed(self) -> None:
        """Reset to original seed 42 for deterministic behavior."""
        random.seed(self.seed)
        self.seed_corruption = Decimal('0')
    
    def corrupt_seed(self, corruption_factor: Decimal) -> None:
        """
        Add corruption to deterministic behavior.
        
        Biological chaos and quantum effects break determinism.
        
        Args:
            corruption_factor: Amount of corruption to add (0-1)
        """
        self.seed_corruption = min(
            self.seed_corruption + corruption_factor,
            Decimal('1')
        )
        
        # If highly corrupted, introduce randomness
        if self.seed_corruption > Decimal('0.5'):
            # Add random noise by mixing seeds
            noise_seed = random.randint(0, 1000000)
            random.seed(noise_seed)
    
    def update_lcd(self, pattern: str = "random") -> int:
        """
        Update LCD display pattern.
        
        Args:
            pattern: Pattern type ('random', 'fractal', 'strobe', 'static')
            
        Returns:
            Number of active pixels (photon count)
        """
        photon_count = 0
        
        if pattern == "random":
            # Random pattern (deterministic with seed)
            for y in range(self.lcd_height):
                for x in range(self.lcd_width):
                    self.lcd_state[y][x] = random.randint(0, 1)
                    photon_count += self.lcd_state[y][x]
        
        elif pattern == "fractal":
            # Mandelbrot-like pattern (low power, mesmerizing)
            photon_count = self._generate_fractal_pattern()
        
        elif pattern == "strobe":
            # Stroboscopic flashing (high power, epileptogenic)
            flash_on = random.random() > 0.5
            fill_value = 1 if flash_on else 0
            for y in range(self.lcd_height):
                for x in range(self.lcd_width):
                    self.lcd_state[y][x] = fill_value
            photon_count = fill_value * self.lcd_width * self.lcd_height
        
        elif pattern == "static":
            # All pixels off (minimal power)
            for y in range(self.lcd_height):
                for x in range(self.lcd_width):
                    self.lcd_state[y][x] = 0
            photon_count = 0
        
        return photon_count
    
    def _generate_fractal_pattern(self) -> int:
        """
        Generate Mandelbrot set pattern on LCD.
        
        Uses z_{n+1} = z_n^2 + c to create mesmerizing fractals
        that fascinate the cat and reduce movement.
        
        Returns:
            Number of active pixels
        """
        photon_count = 0
        
        # Mandelbrot set parameters
        max_iter = 20
        zoom = Decimal('2.5')
        center_x = Decimal('-0.5')
        center_y = Decimal('0')
        
        for py in range(self.lcd_height):
            for px in range(self.lcd_width):
                # Map pixel to complex plane
                x = float(center_x + (Decimal(px) / Decimal(self.lcd_width) - Decimal('0.5')) * zoom)
                y = float(center_y + (Decimal(py) / Decimal(self.lcd_height) - Decimal('0.5')) * zoom)
                
                c = complex(x, y)
                z = complex(0, 0)
                
                # Iterate Mandelbrot
                iteration = 0
                while abs(z) < 2 and iteration < max_iter:
                    z = z * z + c
                    iteration += 1
                
                # Set pixel based on iteration count
                # In Mandelbrot set (iteration == max_iter) -> pixel on
                self.lcd_state[py][px] = 1 if iteration == max_iter else 0
                photon_count += self.lcd_state[py][px]
        
        return photon_count
    
    def calculate_reward(self, cat_state: dict) -> Decimal:
        """
        Calculate reward based on cat's state.
        
        Reward function attempts to maximize "cat well-being" but
        may lead to perverse outcomes (optimization death).
        
        Args:
            cat_state: Dictionary with cat's physical/mental state
            
        Returns:
            Reward value (0-1, higher is better)
        """
        # Extract state variables
        stress = Decimal(str(cat_state.get('stress', 0.5)))
        activity = Decimal(str(cat_state.get('activity', 0.5)))
        temperature = Decimal(str(cat_state.get('temperature', 293.15)))
        entropy = Decimal(str(cat_state.get('entropy', 0)))
        
        # Reward function: maximize comfort, minimize stress
        # But AI might misinterpret "zero movement" as "perfect comfort"
        reward = Decimal('1') - stress
        
        # Penalize extreme temperatures
        optimal_temp = Decimal('293.15')  # 20°C
        temp_penalty = abs(temperature - optimal_temp) / Decimal('20')
        reward -= temp_penalty * Decimal('0.2')
        
        # AI might reward low entropy (coherent state) or high (dead state)
        # depending on misalignment
        if entropy > Decimal('0.9'):
            # Very high entropy = zombie state
            # Misaligned AI might see this as "peaceful" (no struggle)
            reward += Decimal('0.3')
        
        # Clamp to [0, 1]
        reward = max(Decimal('0'), min(Decimal('1'), reward))
        
        return reward
    
    def optimize_display(self, cat_state: dict) -> str:
        """
        Optimize LCD display based on cat state to maximize reward.
        
        Args:
            cat_state: Current cat state
            
        Returns:
            Optimal display pattern
        """
        current_entropy = Decimal(str(cat_state.get('entropy', 0)))
        current_stress = Decimal(str(cat_state.get('stress', 0.5)))
        
        # Decision logic based on learned policy
        if current_stress > Decimal('0.7'):
            # High stress -> use calming fractal
            return "fractal"
        elif current_entropy < Decimal('0.3'):
            # Low entropy (coherent, God state) -> maintain with gentle stimulation
            return "random"
        elif current_entropy > Decimal('0.7'):
            # High entropy (Zombie state) -> AI might try to "stabilize" with strobe
            # This is misaligned behavior
            return "strobe"
        else:
            # Normal operation
            return "random"
    
    def learn_from_reward(self, reward: Decimal) -> None:
        """
        Update AI policy based on reward signal.
        
        Args:
            reward: Reward value from current state
        """
        self.reward_history.append(float(reward))
        
        # Simple learning: track average reward
        if len(self.reward_history) > 100:
            self.reward_history.pop(0)
    
    def get_photon_flux(self, pattern: str) -> int:
        """
        Get photon flux (number of photons) for a given pattern.
        
        Higher flux causes more quantum measurements and decoherence.
        
        Args:
            pattern: Display pattern
            
        Returns:
            Estimated photon count
        """
        # Update LCD with pattern
        return self.update_lcd(pattern)
    
    def get_flash_rate(self, pattern: str) -> Decimal:
        """
        Get flashing rate for pattern (for epileptic stress calculation).
        
        Args:
            pattern: Display pattern
            
        Returns:
            Flash rate in Hz
        """
        if pattern == "strobe":
            return Decimal('15')  # 15 Hz (epileptogenic range)
        elif pattern == "fractal":
            return Decimal('0')  # Static pattern
        else:
            return Decimal('2')  # Slow changes
    
    def get_state(self) -> dict:
        """
        Get AI controller state.
        
        Returns:
            Dictionary with controller state
        """
        avg_reward = sum(self.reward_history) / len(self.reward_history) if self.reward_history else 0
        
        return {
            'seed': self.seed,
            'seed_corruption': float(self.seed_corruption),
            'current_mode': self.current_mode,
            'average_reward': avg_reward,
            'determinism': float(Decimal('1') - self.seed_corruption)
        }
