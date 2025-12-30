# Benchmark Tests

Copyright (c) 2025 David A. Besemer

## License

These benchmark tests are dual-licensed. You may choose either license based on your use case:

### Option 1: MIT License (for commercial/derivative use)
For commercial software development, derivative works, and general software use, these benchmarks are licensed under the MIT License. See the [LICENSE](../LICENSE) file in the repository root for full terms.

### Option 2: Creative Commons Attribution 4.0 International (for academic/scientific use)
For academic publications, scientific research, and educational purposes, these benchmarks are licensed under CC BY 4.0. When using under this license:
- **You must** give appropriate credit to David A. Besemer
- **You must** provide a link to the license: http://creativecommons.org/licenses/by/4.0/
- **You must** indicate if changes were made

See the [LICENSE](../LICENSE) file in the repository root for full terms of both licenses.

## Benchmark Files

All benchmark files in this directory include proper license headers and are covered by the dual license:

### 1. benchmark_physics_calculations.py
Benchmarks for core physics calculations including:
- Gravitational force calculations
- Total energy calculations for multi-body systems
- Complete simulation steps

**License:** MIT OR CC-BY-4.0

### 2. benchmark_vector_operations.py
Benchmarks for 3D vector operations with decimal precision:
- Vector magnitude calculations
- Vector normalization
- Dot product and cross product
- Vector creation and initialization

**License:** MIT OR CC-BY-4.0

### 3. benchmark_energy_calculations.py
Benchmarks for kinetic and potential energy calculations:
- Kinetic energy calculation
- Gravitational potential energy
- Total energy for single and multi-body systems
- Energy conservation verification

**License:** MIT OR CC-BY-4.0

## Running Benchmarks

### Run Individual Benchmarks

```bash
# Run physics calculations benchmark
python benchmarks/benchmark_physics_calculations.py

# Run vector operations benchmark
python benchmarks/benchmark_vector_operations.py

# Run energy calculations benchmark
python benchmarks/benchmark_energy_calculations.py
```

### Run All Benchmarks

```bash
# From repository root
python -m benchmarks.benchmark_physics_calculations
python -m benchmarks.benchmark_vector_operations
python -m benchmarks.benchmark_energy_calculations
```

## Manifest

See [manifest.json](manifest.json) for detailed metadata about:
- License information and attribution requirements
- Benchmark descriptions and purposes
- Python community usage guidelines
- Links to license documentation

## Citation

If you use these benchmarks in academic or scientific work, please cite:

```bibtex
@software{besemer2025decimal_benchmarks,
  author = {Besemer, David A.},
  title = {Decimal Physics Controller Benchmarks},
  year = {2025},
  url = {https://github.com/davidbesemer132/decimal-physics-controller}
}
```

## Choosing a License

- **For scientific/academic publications:** Use CC BY 4.0 (attribution mandatory)
- **For commercial/derivative software:** Use MIT License
- **For any other use:** Choose the license that fits your needs best

Both licenses are equally valid and enforceable. The dual license structure is designed to support both open source software development and academic research.

## Attribution Requirements

### For CC BY 4.0 Users (Academic/Scientific)
When using these benchmarks under CC BY 4.0 in publications or research:
1. Credit the author: David A. Besemer
2. Include a link to: https://github.com/davidbesemer132/decimal-physics-controller
3. Note any modifications made to the benchmark code
4. Include a link to the license: http://creativecommons.org/licenses/by/4.0/

### For MIT License Users (Commercial/Derivative)
When using these benchmarks under the MIT License:
1. Include the copyright notice: Copyright (c) 2025 David A. Besemer
2. Include the MIT License text (see main LICENSE file)
3. Include this information in all copies or substantial portions

## Contributing

Contributions to benchmarks should:
- Maintain compatibility with both licenses
- Include proper license headers
- Follow existing benchmark structure and style
- Include documentation of methodology

---

For more information, see the main [LICENSE](../LICENSE) file in the repository root.
