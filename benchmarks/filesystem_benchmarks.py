"""Filesystem performance benchmarks.

This module benchmarks filesystem operations including file I/O,
path operations, and directory traversal.
"""

import pytest
from pathlib import Path
import json
from decimal import Decimal


class TestFileSystemPerformance:
    """Benchmark filesystem operations."""

    def test_create_file(self, benchmark, benchmark_data_dir):
        """Benchmark file creation performance."""
        def create_file():
            test_file = benchmark_data_dir / 'test_file.txt'
            test_file.write_text('test content')
            return test_file
        
        result = benchmark(create_file)
        assert result.exists()
        result.unlink()  # cleanup

    def test_read_file(self, benchmark, benchmark_data_dir):
        """Benchmark file reading performance."""
        # Setup
        test_file = benchmark_data_dir / 'test_read.txt'
        test_content = 'x' * 10000  # 10KB file
        test_file.write_text(test_content)
        
        # Benchmark
        def read_file():
            return test_file.read_text()
        
        result = benchmark(read_file)
        assert len(result) == len(test_content)

    def test_write_large_file(self, benchmark, benchmark_data_dir):
        """Benchmark writing large files."""
        test_file = benchmark_data_dir / 'large_file.txt'
        large_content = '\n'.join([f'line {i}' for i in range(1000)])
        
        def write_large():
            test_file.write_text(large_content)
        
        benchmark(write_large)
        assert test_file.exists()
        assert len(test_file.read_text()) > 0

    def test_json_file_write(self, benchmark, benchmark_data_dir, sample_decimal_values):
        """Benchmark JSON file writing with Decimal values."""
        test_file = benchmark_data_dir / 'data.json'
        data = {
            'values': [str(d) for d in sample_decimal_values],
            'count': len(sample_decimal_values),
        }
        
        def write_json():
            with open(test_file, 'w') as f:
                json.dump(data, f)
        
        benchmark(write_json)
        assert test_file.exists()

    def test_json_file_read(self, benchmark, benchmark_data_dir):
        """Benchmark JSON file reading."""
        test_file = benchmark_data_dir / 'data.json'
        test_data = {'values': ['3.14159', '2.71828'], 'count': 2}
        test_file.write_text(json.dumps(test_data))
        
        def read_json():
            with open(test_file, 'r') as f:
                return json.load(f)
        
        result = benchmark(read_json)
        assert result['count'] == 2

    def test_path_operations(self, benchmark, benchmark_data_dir):
        """Benchmark path manipulation operations."""
        def path_ops():
            p = benchmark_data_dir / 'subdir' / 'nested' / 'file.txt'
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text('test')
            return p.resolve()
        
        result = benchmark(path_ops)
        assert result.exists()

    def test_directory_iteration(self, benchmark, benchmark_data_dir):
        """Benchmark directory iteration performance."""
        # Setup: create test files
        for i in range(100):
            (benchmark_data_dir / f'file_{i}.txt').write_text(f'content {i}')
        
        def iterate_dir():
            return list(benchmark_data_dir.glob('*.txt'))
        
        result = benchmark(iterate_dir)
        assert len(result) == 100

    def test_file_deletion(self, benchmark, benchmark_data_dir):
        """Benchmark file deletion performance."""
        # Setup: create test file
        test_file = benchmark_data_dir / 'to_delete.txt'
        test_file.write_text('content to delete')
        
        def delete_file():
            test_file.unlink()
        
        benchmark(delete_file)
        assert not test_file.exists()

    def test_file_copy(self, benchmark, benchmark_data_dir):
        """Benchmark file copying performance."""
        import shutil
        source = benchmark_data_dir / 'source.txt'
        source.write_text('x' * 10000)
        dest = benchmark_data_dir / 'dest.txt'
        
        def copy_file():
            shutil.copy2(source, dest)
        
        benchmark(copy_file)
        assert dest.exists()
