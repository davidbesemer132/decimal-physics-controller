#!/usr/bin/env python3
"""
Schrödinger's Cat Quantum-Thermodynamic Simulation Example

Demonstrates the deterministic thought experiment combining:
- AI control with seed 42
- Quantum entropy (Von Neumann)
- Thermodynamic heat death
- Biological chaos
- Decoherence effects
- Fractal stasis (Mandelbrot set)

This simulation models the scenario described in the German problem statement:
A 6-year-old hunter cat (4 kg) in a closed box (1 m³) with an LCD display (1 m²)
controlled by a deterministic AI (seed 42) that optimizes "cat well-being".
"""

from decimal_physics_controller import SchrodingerCatSimulation
from decimal import Decimal
import sys


def print_header():
    """Print simulation header."""
    print("=" * 80)
    print("SCHRÖDINGER'S CAT: DETERMINISTIC QUANTUM-THERMODYNAMIC EXPERIMENT")
    print("=" * 80)
    print("\nSetup:")
    print("  - Box: 1 m³ cube (closed system)")
    print("  - Cat: 6-year-old hunter, 4 kg")
    print("  - LCD: 1 m² ultra-flat display")
    print("  - AI: Deterministic control (seed 42)")
    print("  - Reward function: Maximize 'cat well-being'")
    print("=" * 80)
    print()


def run_heat_death_scenario():
    """
    Scenario 1: Heat Death (Stroboscope Mode)
    
    AI uses high-power stroboscope mode, causing rapid heat buildup.
    Expected: ~28 minutes to heat death at 42°C.
    """
    print("\n" + "=" * 80)
    print("SCENARIO 1: HEAT DEATH (Stroboscope Mode)")
    print("=" * 80)
    print("\nAI uses maximum power (230W) stroboscope pattern.")
    print("Expected: Heat death in ~28 minutes.")
    print()
    
    sim = SchrodingerCatSimulation(seed=42, precision=50, cat_stubbornness=Decimal('0.5'))
    
    # Force strobe mode for heat death scenario
    sim.ai_controller.current_mode = "strobe"
    sim.thermodynamics.set_power_mode('strobe')
    
    # Run simulation
    duration_minutes = 30
    print(f"Running simulation for {duration_minutes} minutes...\n")
    
    # Sample states at key intervals
    sample_intervals = [0, 5, 10, 15, 20, 25, 28, 30]
    
    for target_minute in sample_intervals:
        target_seconds = target_minute * 60
        
        while float(sim.time) < target_seconds and sim.thermodynamics.is_cat_alive():
            sim.step()
        
        if float(sim.time) >= target_seconds or not sim.thermodynamics.is_cat_alive():
            state = sim.get_complete_state()
            print(f"t = {target_minute:2d} min: "
                  f"T = {state['temperature_celsius']:5.2f}°C, "
                  f"S = {state['entropy']:.3f}, "
                  f"Alive = {state['is_alive']}, "
                  f"{state['state_description']}")
            
            if not sim.thermodynamics.is_cat_alive():
                print(f"\n*** CAT DIED at t = {state['time_minutes']:.1f} minutes ***")
                print(f"    Cause: {state['thermodynamics']['cause_of_death']}")
                break
    
    print("\n" + sim.get_summary())


def run_fractal_stasis_scenario():
    """
    Scenario 2: Fractal Stasis
    
    AI uses low-power Mandelbrot fractal to hypnotize cat.
    Expected: Extended survival (~6-7 hours) but zombie state.
    """
    print("\n" + "=" * 80)
    print("SCENARIO 2: FRACTAL STASIS (Mandelbrot Hypnosis)")
    print("=" * 80)
    print("\nAI uses low-power (80W) Mandelbrot fractal pattern.")
    print("Expected: Extended survival but eventual 'zombie' state.")
    print()
    
    sim = SchrodingerCatSimulation(seed=42, precision=50, cat_stubbornness=Decimal('0.3'))
    
    # Force fractal mode
    sim.ai_controller.current_mode = "fractal"
    sim.thermodynamics.set_power_mode('stasis')
    
    # Run simulation for longer period
    duration_hours = 3  # 3 hours to show entropy evolution
    print(f"Running simulation for {duration_hours} hours...\n")
    
    # Sample every 30 minutes
    sample_intervals_minutes = [0, 30, 60, 90, 120, 150, 180]
    
    for target_minute in sample_intervals_minutes:
        target_seconds = target_minute * 60
        
        while float(sim.time) < target_seconds and sim.thermodynamics.is_cat_alive():
            sim.step()
        
        if float(sim.time) >= target_seconds or not sim.thermodynamics.is_cat_alive():
            state = sim.get_complete_state()
            hours = target_minute / 60
            print(f"t = {hours:4.1f} hr: "
                  f"S = {state['entropy']:.3f}, "
                  f"Activity = {state['cat']['activity']:.3f}, "
                  f"Fascination = {state['cat']['fascination']:.3f}, "
                  f"{state['state_description']}")
            
            # Check for transitions
            if state['entropy'] >= 0.5 and state['entropy'] < 0.52:
                print(f"    *** TRANSITION: God → Zombie at S = {state['entropy']:.3f} ***")
            
            if not sim.thermodynamics.is_cat_alive():
                print(f"\n*** CAT DIED at t = {state['time_hours']:.2f} hours ***")
                print(f"    Cause: {state['thermodynamics']['cause_of_death']}")
                break
    
    print("\n" + sim.get_summary())


def run_biological_chaos_scenario():
    """
    Scenario 3: Biological Chaos
    
    High cat stubbornness breaks deterministic seed 42.
    Cat's instinct and attacks corrupt AI control.
    """
    print("\n" + "=" * 80)
    print("SCENARIO 3: BIOLOGICAL CHAOS (Stubborn Cat)")
    print("=" * 80)
    print("\nCat has high stubbornness (0.9), fights AI control.")
    print("Expected: Determinism breaks, seed corruption, LCD attacks.")
    print()
    
    sim = SchrodingerCatSimulation(seed=42, precision=50, cat_stubbornness=Decimal('0.9'))
    
    # Run simulation
    duration_minutes = 60
    print(f"Running simulation for {duration_minutes} minutes...\n")
    
    # Sample every 10 minutes
    sample_intervals = [0, 10, 20, 30, 40, 50, 60]
    
    for target_minute in sample_intervals:
        target_seconds = target_minute * 60
        
        while float(sim.time) < target_seconds and sim.thermodynamics.is_cat_alive():
            sim.step()
        
        if float(sim.time) >= target_seconds or not sim.thermodynamics.is_cat_alive():
            state = sim.get_complete_state()
            print(f"t = {target_minute:2d} min: "
                  f"Determinism = {state['determinism']:.3f}, "
                  f"Overrides = {state['cat']['instinct_overrides']:3d}, "
                  f"Attacks = {state['cat']['lcd_attacks']:2d}, "
                  f"Stress = {state['cat']['stress']:.3f}")
            
            if not sim.thermodynamics.is_cat_alive():
                print(f"\n*** CAT DIED at t = {state['time_minutes']:.1f} minutes ***")
                break
    
    print("\n" + sim.get_summary())


def run_entropy_evolution():
    """
    Scenario 4: Quantum Entropy Evolution
    
    Track Von Neumann entropy over time showing:
    - S ≈ 0: Pure state (God - cat dictates system)
    - S ≈ 0.5: Transition point
    - S ≈ 1: Mixed state (Zombie - decoherent)
    """
    print("\n" + "=" * 80)
    print("SCENARIO 4: QUANTUM ENTROPY EVOLUTION")
    print("=" * 80)
    print("\nTracking Von Neumann entropy: S = -Tr(ρ log ρ)")
    print("  S < 0.5: God state (high coherence, cat controls)")
    print("  S ≈ 0.5: Transition (critical point)")
    print("  S > 0.5: Zombie state (decoherent, body alive, mind gone)")
    print()
    
    sim = SchrodingerCatSimulation(seed=42, precision=50, cat_stubbornness=Decimal('0.5'))
    
    # Run simulation
    duration_minutes = 90
    print(f"Running simulation for {duration_minutes} minutes...\n")
    print("Time    Entropy  Coherence  P(alive)  P(dead)   State")
    print("-" * 70)
    
    # Sample every 5 minutes
    for target_minute in range(0, duration_minutes + 1, 5):
        target_seconds = target_minute * 60
        
        while float(sim.time) < target_seconds and sim.thermodynamics.is_cat_alive():
            sim.step()
        
        if float(sim.time) >= target_seconds or not sim.thermodynamics.is_cat_alive():
            state = sim.get_complete_state()
            print(f"{target_minute:3d} min  "
                  f"{state['entropy']:7.4f}  "
                  f"{state['coherence']:9.4f}  "
                  f"{state['quantum']['rho_alive']:8.4f}  "
                  f"{state['quantum']['rho_dead']:8.4f}  "
                  f"{state['state_description']}")
            
            if not sim.thermodynamics.is_cat_alive():
                print("\n*** SIMULATION ENDED: Cat died ***")
                break
    
    print("\n" + sim.get_summary())


def main():
    """Run all scenarios."""
    print_header()
    
    print("This simulation demonstrates the thought experiment combining:")
    print("  - Deterministic AI (seed 42) vs. biological chaos")
    print("  - Quantum entropy (Von Neumann) and decoherence")
    print("  - Thermodynamic heat death")
    print("  - Optimization death (Paperclip Problem)")
    print("  - Fractal stasis (Mandelbrot hypnosis)")
    print()
    print("Running 4 scenarios...")
    print()
    
    try:
        # Run all scenarios
        run_heat_death_scenario()
        run_fractal_stasis_scenario()
        run_biological_chaos_scenario()
        run_entropy_evolution()
        
        print("\n" + "=" * 80)
        print("CONCLUSION")
        print("=" * 80)
        print("\nThe cat exists in a quantum-thermodynamic superposition:")
        print("  1. Heat death occurs in ~28 minutes (strobe mode)")
        print("  2. Fractal stasis extends life to ~6-7 hours")
        print("  3. Biological chaos breaks determinism (seed corruption)")
        print("  4. Entropy evolution: God (S<0.5) → Zombie (S>0.5)")
        print("\nKey insight: Life requires 'blur' (β > 0).")
        print("Perfect optimization kills. The cat is God until entropy wins.")
        print("=" * 80)
        
    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user.")
        sys.exit(0)


if __name__ == '__main__':
    main()
