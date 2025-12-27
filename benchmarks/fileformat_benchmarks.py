"""
File Format Serialization Benchmarks

This module contains benchmark tests for various file format serialization
and deserialization operations including JSON, pickle, and CSV.

Author: David A. Besemer
License: Free for Python community; commercial usage requires agreement.
"""

import pytest
import json
import pickle
import csv
from io import StringIO, BytesIO
from decimal import Decimal


@pytest.mark.fileformat
class TestJSONBenchmarks:
    """Benchmark tests for JSON serialization."""

    def test_json_serialize_small_dict(self, benchmark):
        """Benchmark JSON serialization of small dictionary."""
        data = {"key": "value", "number": 42, "list": [1, 2, 3]}
        
        result = benchmark(json.dumps, data)
        assert isinstance(result, str)

    def test_json_deserialize_small_dict(self, benchmark):
        """Benchmark JSON deserialization of small dictionary."""
        json_str = '{"key": "value", "number": 42, "list": [1, 2, 3]}'
        
        result = benchmark(json.loads, json_str)
        assert isinstance(result, dict)

    def test_json_serialize_large_dict(self, benchmark, sample_data_medium):
        """Benchmark JSON serialization of large dictionary."""
        data = {f"key_{i}": f"value_{i}" for i in sample_data_medium}
        
        result = benchmark(json.dumps, data)
        assert isinstance(result, str)

    def test_json_deserialize_large_dict(self, benchmark, sample_data_medium):
        """Benchmark JSON deserialization of large dictionary."""
        data = {f"key_{i}": f"value_{i}" for i in sample_data_medium}
        json_str = json.dumps(data)
        
        result = benchmark(json.loads, json_str)
        assert isinstance(result, dict)
        assert len(result) == len(sample_data_medium)

    def test_json_serialize_nested_structure(self, benchmark):
        """Benchmark JSON serialization of nested structure."""
        data = {
            "users": [
                {"id": i, "name": f"User{i}", "metadata": {"age": 20 + i, "active": True}}
                for i in range(100)
            ]
        }
        
        result = benchmark(json.dumps, data)
        assert isinstance(result, str)

    def test_json_deserialize_nested_structure(self, benchmark):
        """Benchmark JSON deserialization of nested structure."""
        data = {
            "users": [
                {"id": i, "name": f"User{i}", "metadata": {"age": 20 + i, "active": True}}
                for i in range(100)
            ]
        }
        json_str = json.dumps(data)
        
        result = benchmark(json.loads, json_str)
        assert isinstance(result, dict)
        assert len(result["users"]) == 100


@pytest.mark.fileformat
class TestPickleBenchmarks:
    """Benchmark tests for Pickle serialization."""

    def test_pickle_serialize_small_object(self, benchmark):
        """Benchmark pickle serialization of small object."""
        data = {"key": "value", "number": 42, "list": [1, 2, 3]}
        
        result = benchmark(pickle.dumps, data)
        assert isinstance(result, bytes)

    def test_pickle_deserialize_small_object(self, benchmark):
        """Benchmark pickle deserialization of small object."""
        data = {"key": "value", "number": 42, "list": [1, 2, 3]}
        pickled_data = pickle.dumps(data)
        
        result = benchmark(pickle.loads, pickled_data)
        assert isinstance(result, dict)

    def test_pickle_serialize_large_list(self, benchmark, sample_data_medium):
        """Benchmark pickle serialization of large list."""
        data = sample_data_medium
        
        result = benchmark(pickle.dumps, data)
        assert isinstance(result, bytes)

    def test_pickle_deserialize_large_list(self, benchmark, sample_data_medium):
        """Benchmark pickle deserialization of large list."""
        pickled_data = pickle.dumps(sample_data_medium)
        
        result = benchmark(pickle.loads, pickled_data)
        assert isinstance(result, list)
        assert len(result) == len(sample_data_medium)

    def test_pickle_serialize_complex_objects(self, benchmark):
        """Benchmark pickle serialization of complex objects."""
        data = {
            "decimals": [Decimal(str(i)) for i in range(100)],
            "nested": {"level1": {"level2": {"level3": list(range(50))}}},
            "mixed": [1, "string", 3.14, True, None]
        }
        
        result = benchmark(pickle.dumps, data)
        assert isinstance(result, bytes)

    def test_pickle_deserialize_complex_objects(self, benchmark):
        """Benchmark pickle deserialization of complex objects."""
        data = {
            "decimals": [Decimal(str(i)) for i in range(100)],
            "nested": {"level1": {"level2": {"level3": list(range(50))}}},
            "mixed": [1, "string", 3.14, True, None]
        }
        pickled_data = pickle.dumps(data)
        
        result = benchmark(pickle.loads, pickled_data)
        assert isinstance(result, dict)
        assert len(result["decimals"]) == 100


@pytest.mark.fileformat
class TestCSVBenchmarks:
    """Benchmark tests for CSV serialization."""

    def test_csv_write_small_dataset(self, benchmark):
        """Benchmark CSV writing of small dataset."""
        data = [
            ["id", "name", "value"],
            ["1", "Item1", "100"],
            ["2", "Item2", "200"],
            ["3", "Item3", "300"]
        ]
        
        def write_csv():
            output = StringIO()
            writer = csv.writer(output)
            writer.writerows(data)
            return output.getvalue()
        
        result = benchmark(write_csv)
        assert isinstance(result, str)
        assert "Item1" in result

    def test_csv_read_small_dataset(self, benchmark):
        """Benchmark CSV reading of small dataset."""
        csv_data = "id,name,value\n1,Item1,100\n2,Item2,200\n3,Item3,300\n"
        
        def read_csv():
            input_stream = StringIO(csv_data)
            reader = csv.reader(input_stream)
            return list(reader)
        
        result = benchmark(read_csv)
        assert len(result) == 4  # Header + 3 rows

    def test_csv_write_large_dataset(self, benchmark, sample_data_medium):
        """Benchmark CSV writing of large dataset."""
        data = [["id", "value", "squared"]]
        data.extend([[str(i), str(i), str(i**2)] for i in range(1000)])
        
        def write_csv():
            output = StringIO()
            writer = csv.writer(output)
            writer.writerows(data)
            return output.getvalue()
        
        result = benchmark(write_csv)
        assert isinstance(result, str)

    def test_csv_read_large_dataset(self, benchmark):
        """Benchmark CSV reading of large dataset."""
        # Prepare CSV data
        lines = ["id,value,squared"]
        lines.extend([f"{i},{i},{i**2}" for i in range(1000)])
        csv_data = "\n".join(lines) + "\n"
        
        def read_csv():
            input_stream = StringIO(csv_data)
            reader = csv.reader(input_stream)
            return list(reader)
        
        result = benchmark(read_csv)
        assert len(result) == 1001  # Header + 1000 rows

    def test_csv_dictwriter_performance(self, benchmark):
        """Benchmark CSV DictWriter performance."""
        data = [
            {"id": i, "name": f"Item{i}", "value": i * 100}
            for i in range(100)
        ]
        
        def write_csv_dict():
            output = StringIO()
            fieldnames = ["id", "name", "value"]
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            return output.getvalue()
        
        result = benchmark(write_csv_dict)
        assert isinstance(result, str)
        assert "Item0" in result

    def test_csv_dictreader_performance(self, benchmark):
        """Benchmark CSV DictReader performance."""
        lines = ["id,name,value"]
        lines.extend([f"{i},Item{i},{i*100}" for i in range(100)])
        csv_data = "\n".join(lines) + "\n"
        
        def read_csv_dict():
            input_stream = StringIO(csv_data)
            reader = csv.DictReader(input_stream)
            return list(reader)
        
        result = benchmark(read_csv_dict)
        assert len(result) == 100
        assert result[0]["name"] == "Item0"
