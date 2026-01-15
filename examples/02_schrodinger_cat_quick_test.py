#!/usr/bin/env python3
"""
Quick test of Schrödinger's Cat Simulation

Tests basic functionality without long simulation runs.
"""

from decimal_physics_controller import SchrodingerCatSimulation
from decimal import Decimal

def main():
    print("=" * 60)
    print("SCHRÖDINGER'S CAT SIMULATION - QUICK TEST")
    print("=" * 60)
    
    # Create simulation
    print("\n1. Initializing simulation with seed 42...")
    sim = SchrodingerCatSimulation(seed=42, precision=50)
    print("   ✓ Simulation created")
    
    # Check initial state
    print("\n2. Checking initial state...")
    state = sim.get_complete_state()
    print(f"   Initial entropy: {state['entropy']:.4f}")
    print(f"   Initial temperature: {state['temperature_celsius']:.2f}°C")
    print(f"   Cat is alive: {state['is_alive']}")
    print(f"   Determinism: {state['determinism']:.3f}")
    
    # Run for 60 seconds (1 minute)
    print("\n3. Running simulation for 60 seconds...")
    for i in range(60):
        sim.step()
        if i % 20 == 0:
            print(f"   t = {i}s: S = {sim.quantum_state.von_neumann_entropy():.4f}")
    
    # Check final state
    print("\n4. Final state after 1 minute:")
    final_state = sim.get_complete_state()
    print(f"   Final entropy: {final_state['entropy']:.4f}")
    print(f"   Final temperature: {final_state['temperature_celsius']:.2f}°C")
    print(f"   Cat is alive: {final_state['is_alive']}")
    print(f"   Determinism: {final_state['determinism']:.3f}")
    print(f"   Activity: {final_state['cat']['activity']:.3f}")
    print(f"   Stress: {final_state['cat']['stress']:.3f}")
    
    # Show summary
    print("\n5. Summary:")
    print(sim.get_summary())
    
    print("\n" + "=" * 60)
    print("✓ TEST COMPLETE")
    print("=" * 60)

if __name__ == '__main__':
    main()
