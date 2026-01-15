# Schrödinger's Cat Simulation API Reference

## Overview

The Schrödinger's Cat simulation implements a deterministic quantum-thermodynamic thought experiment combining quantum mechanics, thermodynamics, AI control, and biological chaos.

## Main Classes

### SchrodingerCatSimulation

The main orchestrator class that integrates all subsystems.

```python
from decimal_physics_controller import SchrodingerCatSimulation

sim = SchrodingerCatSimulation(
    seed=42,                            # Random seed for AI controller
    precision=50,                       # Decimal precision
    cat_stubbornness=Decimal('0.7')   # Cat's resistance to control (0-1)
)
```

#### Methods

- `step()`: Execute one simulation time step (1 second)
- `run(duration_seconds: float)`: Run simulation for specified duration
- `get_complete_state() -> Dict`: Get complete system state
- `get_summary() -> str`: Get human-readable summary
- `get_cat_state() -> Dict`: Get cat's behavioral state

---

## Quantum Mechanics

### QuantumState

Represents the quantum state of the cat as a two-level system (|alive⟩, |dead⟩).

#### Key Methods

**von_neumann_entropy() -> Decimal**

Calculate Von Neumann entropy: S = -Tr(ρ log ρ)

Returns value in [0, 1] where:
- S ≈ 0: Pure state (coherent, "God" state)
- S ≈ 0.5: Transition point
- S ≈ 1: Maximally mixed state (decoherent, "Zombie" state)

**apply_decoherence(dt: Decimal, gamma: Decimal = 0.001)**

Apply decoherence to quantum state. Default rate γ = 0.001/s.

**apply_measurement(photon_count: int, measurement_strength: Decimal = 0.01)**

Apply quantum measurement effects from LCD photons.

**evolve_thermal(temperature: Decimal, dt: Decimal)**

Apply thermal decoherence due to heat.

---

## Thermodynamics

### ThermodynamicSystem

Models thermodynamics of the closed box system.

#### System Parameters

- Box: 1 m³ cube
- LCD: 1 m² ultra-flat display
- Cat: 4 kg
- Heat capacity: 17950 J/K
- Power range: 80-230 W
- Critical temperature: 42°C (heat death)

#### Key Methods

**set_power_mode(mode: str)**

Set power consumption mode: `'stasis'` (~80W), `'normal'` (~155W), or `'strobe'` (~230W)

**time_to_heat_death() -> Decimal**

Calculate time until cat reaches critical temperature (42°C).
Expected: ~28 minutes at strobe mode, ~2 hours at stasis mode.

**is_cat_alive() -> bool**

Determine if cat is alive based on physical conditions.

---

## AI Control

### DeterministicAIController

AI controller with deterministic seed for reproducible behavior.

**update_lcd(pattern: str) -> int**

Update LCD display pattern. Returns photon count.

Patterns: `'random'`, `'fractal'` (Mandelbrot), `'strobe'`, `'static'`

**corrupt_seed(corruption_factor: Decimal)**

Add corruption to deterministic behavior (biological chaos breaks determinism).

---

## Usage Examples

### Basic Simulation

```python
from decimal_physics_controller import SchrodingerCatSimulation

# Create simulation
sim = SchrodingerCatSimulation(seed=42)

# Run for 10 minutes
sim.run(duration_seconds=600)

# Check results
state = sim.get_complete_state()
print(f"Entropy: {state['entropy']:.4f}")
print(f"Temperature: {state['temperature_celsius']:.2f}°C")
print(f"Is alive: {state['is_alive']}")
```

### Heat Death Scenario

```python
sim = SchrodingerCatSimulation(seed=42)
sim.thermodynamics.set_power_mode('strobe')

# Run until death
while sim.thermodynamics.is_cat_alive():
    sim.step()

print(f"Cat died after {sim.time/60:.1f} minutes")
```

---

## Key Concepts

### Von Neumann Entropy

S = -Tr(ρ log ρ) measures quantum uncertainty:

- **S ≈ 0**: Pure state, "God state" (cat dictates system)
- **S ≈ 0.5**: Transition point (critical threshold)
- **S ≈ 1**: Mixed state, "Zombie state" (decoherent)

### Decoherence

Destroys quantum coherence through:
1. Environmental interaction (LCD photons)
2. Thermal effects (heat increases rate)
3. Measurements (partial wavefunction collapse)

### Optimization Death

AI optimizing "cat well-being" may misinterpret stillness as "zero suffering", leading to death through over-optimization.

---

For complete examples, see `examples/02_schrodinger_cat.py`.
