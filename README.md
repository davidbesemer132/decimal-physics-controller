# Decimal Physics Controller

A Python library for precise physics simulations and calculations using decimal arithmetic for high-precision numerical accuracy.

## Features

- **High-Precision Arithmetic**: Built on Python's `decimal` module for arbitrary precision calculations
- **Physics Simulations**: Comprehensive tools for modeling and simulating physical systems
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

Check the [examples](examples/) directory for Jupyter notebooks demonstrating:

- Basic physics simulations
- Precision arithmetic demonstrations
- Advanced use cases

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
