"""File format serialization and deserialization benchmarks.

This module benchmarks various file format operations including
JSON, CSV, and custom format handling.
"""

import pytest
import json
import csv
from decimal import Decimal
from io import StringIO


class TestFileFormatPerformance:
    """Benchmark file format operations."""

    def test_decimal_to_string_conversion(self, benchmark, large_decimal_array):
        """Benchmark converting Decimal to string."""
        def convert_decimals():
            return [str(d) for d in large_decimal_array]
        
        result = benchmark(convert_decimals)
        assert len(result) == len(large_decimal_array)
        assert all(isinstance(s, str) for s in result)

    def test_string_to_decimal_conversion(self, benchmark, large_decimal_array):
        """Benchmark converting string to Decimal."""
        string_values = [str(d) for d in large_decimal_array]
        
        def convert_to_decimal():
            return [Decimal(s) for s in string_values]
        
        result = benchmark(convert_to_decimal)
        assert len(result) == len(large_decimal_array)
        assert all(isinstance(d, Decimal) for d in result)

    def test_json_decimal_serialization(self, benchmark, large_decimal_array):
        """Benchmark JSON serialization of Decimal values."""
        data = {'values': [str(d) for d in large_decimal_array]}
        
        def serialize_json():
            return json.dumps(data)
        
        result = benchmark(serialize_json)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_json_decimal_deserialization(self, benchmark, large_decimal_array):
        """Benchmark JSON deserialization to Decimal values."""
        data = {'values': [str(d) for d in large_decimal_array]}
        json_str = json.dumps(data)
        
        def deserialize_json():
            loaded = json.loads(json_str)
            return [Decimal(v) for v in loaded['values']]
        
        result = benchmark(deserialize_json)
        assert len(result) == len(large_decimal_array)

    def test_csv_write_decimals(self, benchmark, benchmark_data_dir, large_decimal_array):
        """Benchmark writing Decimal values to CSV."""
        csv_file = benchmark_data_dir / 'data.csv'
        
        def write_csv():
            with open(csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['index', 'value'])
                for i, val in enumerate(large_decimal_array[:100]):
                    writer.writerow([i, str(val)])
        
        benchmark(write_csv)
        assert csv_file.exists()

    def test_csv_read_decimals(self, benchmark, benchmark_data_dir, large_decimal_array):
        """Benchmark reading CSV and converting to Decimal."""
        csv_file = benchmark_data_dir / 'data.csv'
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['index', 'value'])
            for i, val in enumerate(large_decimal_array[:100]):
                writer.writerow([i, str(val)])
        
        def read_csv():
            result = []
            with open(csv_file, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                for row in reader:
                    result.append(Decimal(row[1]))
            return result
        
        result = benchmark(read_csv)
        assert len(result) == 100

    def test_custom_format_serialization(self, benchmark, sample_decimal_values):
        """Benchmark custom format serialization."""
        def serialize_custom():
            return '|'.join([str(d) for d in sample_decimal_values])
        
        result = benchmark(serialize_custom)
        assert isinstance(result, str)
        assert '|' in result

    def test_custom_format_deserialization(self, benchmark, sample_decimal_values):
        """Benchmark custom format deserialization."""
        serialized = '|'.join([str(d) for d in sample_decimal_values])
        
        def deserialize_custom():
            return [Decimal(s) for s in serialized.split('|')]
        
        result = benchmark(deserialize_custom)
        assert len(result) == len(sample_decimal_values)

    def test_large_json_structure(self, benchmark, mock_physics_data):
        """Benchmark serialization of large physics data structures."""
        data = {
            'simulation': {
                'timestamp': '2025-12-27T13:51:16',
                'iterations': 1000,
                'data': {
                    'positions': [[str(x), str(y)] for x, y in mock_physics_data['positions']],
                    'velocities': [[str(x), str(y)] for x, y in mock_physics_data['velocities']],
                    'masses': [str(m) for m in mock_physics_data['masses']],
                }
            }
        }
        
        def serialize_large():
            return json.dumps(data)
        
        result = benchmark(serialize_large)
        assert len(result) > 0

    def test_pretty_print_json(self, benchmark):
        """Benchmark JSON pretty printing."""
        data = {
            'key1': 'value1',
            'key2': {'nested_key': 'nested_value'},
            'key3': [1, 2, 3, 4, 5],
        }
        json_str = json.dumps(data)
        
        def pretty_print():
            return json.dumps(json.loads(json_str), indent=2)
        
        result = benchmark(pretty_print)
        assert 'key1' in result

    def test_decimal_precision_conversion(self, benchmark):
        """Benchmark Decimal precision handling in conversions."""
        values = [Decimal('3.14159265358979323846') for _ in range(1000)]
        
        def convert_with_precision():
            return [Decimal(str(v)) for v in values]
        
        result = benchmark(convert_with_precision)
        assert len(result) == 1000
        assert result[0] == Decimal('3.14159265358979323846')
