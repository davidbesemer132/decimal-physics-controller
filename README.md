# Decimal Physics Controller

A Python library for precise physics simulations and calculations using decimal arithmetic for high-precision numerical accuracy.

## Features

- **High-Precision Arithmetic**: Built on Python's `decimal` module for arbitrary precision calculations
- **Physics Simulations**: Comprehensive tools for modeling and simulating physical systems
- **Quantum-Thermodynamic Simulations**: Schrödinger's Cat experiment with quantum entropy and thermodynamics
- **Deterministic AI Control**: Reproducible simulations with seed-based determinism
- **Scientific Computing**: Integration with NumPy and SciPy for advanced numerical methods
- **Jupyter Support**: Full support for interactive notebooks and visualization
- **Well-Tested**: Comprehensive test suite using pytest
- **Easy Installation**: Simple pip installation with automatic dependency management

## Quick Start

### Installation

```bash
pip install .
```

Or with development dependencies:

```bash
pip install -e .
```

### Basic Usage

```python
from decimal_physics_controller import PhysicsController

# Initialize a physics controller
controller = PhysicsController()

# Your physics calculations here
result = controller.calculate(...)
```

### Schrödinger's Cat Quantum Simulation

```python
from decimal_physics_controller import SchrodingerCatSimulation

# Create a deterministic quantum-thermodynamic simulation
sim = SchrodingerCatSimulation(seed=42, precision=50)

# Run simulation for 10 minutes
sim.run(duration_seconds=600)

# Get complete state
state = sim.get_complete_state()
print(f"Entropy: {state['entropy']:.4f}")
print(f"Temperature: {state['temperature_celsius']:.2f}°C")
print(f"Cat is alive: {state['is_alive']}")

# Display detailed summary
print(sim.get_summary())
```

The Schrödinger's Cat simulation combines:
- **Quantum Entropy**: Von Neumann entropy S = -Tr(ρ log ρ) tracking quantum decoherence
- **Thermodynamics**: Heat generation and time-to-death calculations
- **AI Control**: Deterministic AI with seed 42 controlling LCD display patterns
- **Biological Chaos**: Cat's instinctive behavior breaks determinism
- **Fractal Stasis**: Mandelbrot set patterns for cat hypnosis

## Requirements

- Python 3.7+
- numpy
- scipy
- pytest (for testing)
- jupyter (for notebooks)

See [requirements.txt](requirements.txt) for the complete list.

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/davidbesemer132/decimal-physics-controller.git
cd decimal-physics-controller

# Install in development mode
pip install -e .
```

### With pip

```bash
pip install .
```

## Testing

Run the test suite with pytest:

```bash
pytest
```

## Documentation

Detailed documentation is available in the [docs](docs/) directory. Key topics include:

- [Installation Guide](docs/installation.md)
- [User Guide](docs/user_guide.md)
- [API Reference](docs/api_reference.md)
- [Examples](docs/examples.md)

## Examples

Check the [examples](examples/) directory for demonstrations:

- **01_orbit_decay.py**: Orbital decay simulation showing decimal vs float precision
- **02_schrodinger_cat.py**: Complete Schrödinger's Cat quantum-thermodynamic experiment with multiple scenarios
- **02_schrodinger_cat_quick_test.py**: Quick test of quantum simulation functionality

### Schrödinger's Cat Scenarios

The quantum simulation includes four demonstration scenarios:

1. **Heat Death (Stroboscope Mode)**: High-power LCD causes heat death in ~28 minutes
2. **Fractal Stasis**: Low-power Mandelbrot patterns extend survival to 6-7 hours
3. **Biological Chaos**: Cat's stubbornness breaks AI determinism (seed corruption)
4. **Entropy Evolution**: Von Neumann entropy tracking from God state (S<0.5) to Zombie state (S>0.5)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is dual-licensed under:
- **Creative Commons Attribution 4.0 International (CC BY 4.0)** - Choose this for academic and creative uses
- **MIT License** - Choose this for software and commercial uses

See [LICENSE](LICENSE) for full details.

## Citation

If you use this library in academic work, please cite:

```bibtex
@software{besemer2025decimal,
  author = {Besemer, David A.},
  title = {Decimal Physics Controller},
  year = {2025},
  url = {https://github.com/davidbesemer132/decimal-physics-controller}
}
```

## Support

For issues, questions, or suggestions, please open an [issue](https://github.com/davidbesemer132/decimal-physics-controller/issues) on GitHub.

## Author

**David A. Besemer**

---

*Last updated: December 27, 2025*
