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

## Benchmarks

Performance benchmarks are available in the [benchmarks](benchmarks/) directory. These benchmarks measure the performance of core operations using decimal precision.

### Running Benchmarks

```bash
# Run individual benchmarks
python benchmarks/benchmark_physics_calculations.py
python benchmarks/benchmark_vector_operations.py
python benchmarks/benchmark_energy_calculations.py
```

### Benchmark Coverage

- **Physics Calculations:** Gravitational forces, energy calculations, simulation steps
- **Vector Operations:** Magnitude, normalization, dot/cross products
- **Energy Calculations:** Kinetic, potential, and total energy for multi-body systems

### Benchmark Licensing

All benchmarks are dual-licensed (MIT OR CC BY 4.0) to support both commercial development and academic research. See [benchmarks/README.md](benchmarks/README.md) for:
- Detailed license information
- Attribution requirements for academic use
- Citation guidelines
- Complete benchmark documentation

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

This project is dual-licensed under MIT License and Creative Commons Attribution 4.0 International (CC BY 4.0).

Copyright (c) 2025 David A. Besemer

### Dual License Structure

You may choose either license based on your use case:

#### 1. MIT License (for commercial/derivative use)
- ✅ Use in commercial software
- ✅ Create derivative works
- ✅ Modify and redistribute
- ✅ Include in proprietary software
- ⚠️ Must include copyright notice and license text

#### 2. Creative Commons Attribution 4.0 International (for academic/scientific use)
- ✅ Use in academic publications
- ✅ Use in scientific research
- ✅ Share and adapt for any purpose
- ⚠️ **Must give appropriate credit to David A. Besemer**
- ⚠️ Must provide a link to the license
- ⚠️ Must indicate if changes were made

### Choosing a License

- **For scientific/academic publications:** Use CC BY 4.0 (attribution mandatory)
- **For commercial/derivative software:** Use MIT License  
- **For any other use:** Choose the license that fits your needs best

Both licenses are equally valid and enforceable.

### License Coverage

All components of this project are covered by the dual license:
- **Source code:** MIT OR CC BY 4.0
- **Documentation:** MIT OR CC BY 4.0
- **Benchmarks:** MIT OR CC BY 4.0 (see [benchmarks/README.md](benchmarks/README.md))
- **Examples:** MIT OR CC BY 4.0

See the main [LICENSE](LICENSE) file for complete license terms.

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
