# Benchmark Tests Suite

This directory contains comprehensive benchmark tests for the Decimal Physics Controller project.

## Author

**David A. Besemer**

## License

Free for Python community use. Commercial usage requires agreement with David A. Besemer.

## Overview

The benchmark suite includes three main categories:

### 1. Filesystem Benchmarks (`filesystem_benchmarks.py`)

Tests filesystem performance including:
- Sequential read operations (small, medium, large)
- Sequential write operations (small, medium, large)
- Random seek operations
- Buffered vs unbuffered writes
- Directory listing performance
- File stat operations

### 2. File Format Benchmarks (`fileformat_benchmarks.py`)

Tests serialization/deserialization performance for:
- **JSON**: Small/large dictionaries, nested structures
- **Pickle**: Small/large objects, complex Python objects
- **CSV**: Small/large datasets, DictReader/DictWriter

### 3. Application Benchmarks (`application_benchmarks.py`)

Tests physics controller performance including:
- Controller initialization
- Object management (add/remove)
- Vector operations (magnitude, dot product, cross product, normalize)
- Physics calculations (gravitational force, kinetic/potential energy)
- Simulation steps (single, multiple, full runs)
- Stress tests (many objects, long runs)

## Running Benchmarks

### Prerequisites

Install benchmark dependencies:

```bash
pip install -e ".[benchmarks]"
```

Or install pytest-benchmark directly:

```bash
pip install pytest-benchmark
```

### Basic Usage

Run all benchmarks:

```bash
pytest benchmarks/ --benchmark-only
```

Run specific benchmark file:

```bash
pytest benchmarks/filesystem_benchmarks.py --benchmark-only
```

Run benchmarks with specific markers:

```bash
pytest benchmarks/ -m filesystem --benchmark-only
pytest benchmarks/ -m fileformat --benchmark-only
pytest benchmarks/ -m application --benchmark-only
```

### Advanced Options

Generate JSON report:

```bash
pytest benchmarks/ --benchmark-only --benchmark-json=results.json
```

Compare with previous results:

```bash
pytest benchmarks/ --benchmark-only --benchmark-compare=0001
```

Save benchmark results:

```bash
pytest benchmarks/ --benchmark-only --benchmark-save=baseline
```

Show histogram:

```bash
pytest benchmarks/ --benchmark-only --benchmark-histogram
```

Customize rounds and warmup:

```bash
pytest benchmarks/ --benchmark-only --benchmark-warmup=on --benchmark-min-rounds=50
```

### Excluding Slow Tests

Skip slow stress tests:

```bash
pytest benchmarks/ --benchmark-only -m "not slow"
```

## Benchmark Configuration

Default configuration (can be customized in `conftest.py`):

- **Rounds**: 100 iterations per test
- **Warmup**: 10 warmup rounds
- **Iterations**: 1 iteration per round
- **Min Time**: 0.000005 seconds

## Statistics Reported

For each benchmark, the following statistics are reported:

- **Min**: Minimum execution time
- **Max**: Maximum execution time
- **Mean**: Average execution time
- **Median**: Median execution time
- **StdDev**: Standard deviation
- **Rounds**: Number of measurement rounds
- **Iterations**: Iterations per round

## Output Formats

Benchmarks can be output in multiple formats:

- **Terminal**: Human-readable console output (default)
- **JSON**: Machine-readable JSON format
- **Histogram**: Visual histogram of results (requires `--benchmark-histogram`)

## Continuous Integration

To run benchmarks in CI/CD pipelines:

```bash
# Run benchmarks and save baseline
pytest benchmarks/ --benchmark-only --benchmark-save=ci_baseline

# Compare against baseline in subsequent runs
pytest benchmarks/ --benchmark-only --benchmark-compare=ci_baseline --benchmark-compare-fail=mean:10%
```

## Memory Profiling

Memory profiling can be added using memory_profiler:

```bash
pip install memory-profiler
pytest benchmarks/ --benchmark-only --profile
```

## Interpreting Results

### Performance Metrics

- **Operations per second**: Higher is better
- **Execution time**: Lower is better
- **Standard deviation**: Lower indicates more consistent performance

### Comparing Results

When comparing benchmarks:
- Look for significant differences (>10% change)
- Consider system load and external factors
- Run multiple times for reliable comparisons
- Use the same hardware/environment when possible

## Troubleshooting

### Benchmarks running slowly

- Check if system is under heavy load
- Ensure no background processes are running
- Increase warmup rounds for more stable results

### Inconsistent results

- Run benchmarks multiple times
- Increase the number of rounds
- Check for thermal throttling on the system

## Contributing

When adding new benchmarks:

1. Follow the existing naming convention
2. Add appropriate markers (`@pytest.mark.filesystem`, etc.)
3. Include docstrings describing what is being tested
4. Mark slow tests with `@pytest.mark.slow`
5. Update this README with new benchmark descriptions

## References

- [pytest-benchmark documentation](https://pytest-benchmark.readthedocs.io/)
- [Project manifest.json](../manifest.json) - Detailed benchmark specifications
- [Main README](../README.md) - Project documentation

---

**© 2025 David A. Besemer** - Free for Python community use
