"""
Filesystem Performance Benchmarks

This module contains benchmark tests for filesystem operations including
read, write, and seek operations.

Author: David A. Besemer
License: Free for Python community; commercial usage requires agreement.
"""

import pytest
import os
import tempfile
from pathlib import Path


@pytest.mark.filesystem
class TestFilesystemBenchmarks:
    """Benchmark tests for filesystem operations."""

    def test_sequential_write_small(self, benchmark, temp_benchmark_dir):
        """Benchmark sequential write operations with small data."""
        filepath = temp_benchmark_dir / "sequential_write_small.dat"
        data = b"x" * 1024  # 1KB
        
        def write_file():
            with open(filepath, "wb") as f:
                f.write(data)
            # Cleanup for next iteration
            if filepath.exists():
                filepath.unlink()
        
        benchmark(write_file)

    def test_sequential_write_medium(self, benchmark, temp_benchmark_dir):
        """Benchmark sequential write operations with medium data."""
        filepath = temp_benchmark_dir / "sequential_write_medium.dat"
        data = b"x" * (1024 * 1024)  # 1MB
        
        def write_file():
            with open(filepath, "wb") as f:
                f.write(data)
            # Cleanup for next iteration
            if filepath.exists():
                filepath.unlink()
        
        benchmark(write_file)

    def test_sequential_write_large(self, benchmark, temp_benchmark_dir):
        """Benchmark sequential write operations with large data."""
        filepath = temp_benchmark_dir / "sequential_write_large.dat"
        data = b"x" * (10 * 1024 * 1024)  # 10MB
        
        def write_file():
            with open(filepath, "wb") as f:
                f.write(data)
            # Cleanup for next iteration
            if filepath.exists():
                filepath.unlink()
        
        benchmark(write_file)

    def test_sequential_read_small(self, benchmark, temp_benchmark_dir):
        """Benchmark sequential read operations with small data."""
        filepath = temp_benchmark_dir / "sequential_read_small.dat"
        data = b"x" * 1024  # 1KB
        
        # Prepare file
        with open(filepath, "wb") as f:
            f.write(data)
        
        def read_file():
            with open(filepath, "rb") as f:
                return f.read()
        
        result = benchmark(read_file)
        assert len(result) == 1024

    def test_sequential_read_medium(self, benchmark, temp_benchmark_dir):
        """Benchmark sequential read operations with medium data."""
        filepath = temp_benchmark_dir / "sequential_read_medium.dat"
        data = b"x" * (1024 * 1024)  # 1MB
        
        # Prepare file
        with open(filepath, "wb") as f:
            f.write(data)
        
        def read_file():
            with open(filepath, "rb") as f:
                return f.read()
        
        result = benchmark(read_file)
        assert len(result) == 1024 * 1024

    def test_sequential_read_large(self, benchmark, temp_benchmark_dir):
        """Benchmark sequential read operations with large data."""
        filepath = temp_benchmark_dir / "sequential_read_large.dat"
        data = b"x" * (10 * 1024 * 1024)  # 10MB
        
        # Prepare file
        with open(filepath, "wb") as f:
            f.write(data)
        
        def read_file():
            with open(filepath, "rb") as f:
                return f.read()
        
        result = benchmark(read_file)
        assert len(result) == 10 * 1024 * 1024

    def test_random_seek_operations(self, benchmark, temp_benchmark_dir):
        """Benchmark random seek operations."""
        filepath = temp_benchmark_dir / "random_seek.dat"
        data = b"x" * (1024 * 1024)  # 1MB
        
        # Prepare file
        with open(filepath, "wb") as f:
            f.write(data)
        
        def seek_and_read():
            with open(filepath, "rb") as f:
                # Seek to multiple positions
                f.seek(0)
                f.read(100)
                f.seek(512 * 1024)
                f.read(100)
                f.seek(1024 * 1024 - 100)
                return f.read(100)
        
        result = benchmark(seek_and_read)
        assert len(result) == 100

    def test_buffered_write_performance(self, benchmark, temp_benchmark_dir):
        """Benchmark buffered write operations."""
        filepath = temp_benchmark_dir / "buffered_write.dat"
        
        def buffered_write():
            with open(filepath, "w", buffering=8192) as f:
                for i in range(1000):
                    f.write(f"Line {i}: " + "x" * 100 + "\n")
            # Cleanup for next iteration
            if filepath.exists():
                filepath.unlink()
        
        benchmark(buffered_write)

    def test_unbuffered_write_performance(self, benchmark, temp_benchmark_dir):
        """Benchmark unbuffered write operations."""
        filepath = temp_benchmark_dir / "unbuffered_write.dat"
        
        def unbuffered_write():
            with open(filepath, "wb", buffering=0) as f:
                for i in range(1000):
                    line = f"Line {i}: ".encode() + b"x" * 100 + b"\n"
                    f.write(line)
            # Cleanup for next iteration
            if filepath.exists():
                filepath.unlink()
        
        benchmark(unbuffered_write)

    def test_directory_listing_performance(self, benchmark, temp_benchmark_dir):
        """Benchmark directory listing operations."""
        # Create multiple files
        for i in range(100):
            filepath = temp_benchmark_dir / f"file_{i}.txt"
            with open(filepath, "w") as f:
                f.write("test content")
        
        def list_directory():
            return list(temp_benchmark_dir.iterdir())
        
        result = benchmark(list_directory)
        assert len(result) >= 100

    def test_file_stat_operations(self, benchmark, temp_benchmark_dir):
        """Benchmark file stat operations."""
        filepath = temp_benchmark_dir / "stat_test.dat"
        data = b"x" * 1024
        
        # Prepare file
        with open(filepath, "wb") as f:
            f.write(data)
        
        def stat_file():
            return os.stat(filepath)
        
        result = benchmark(stat_file)
        assert result.st_size == 1024
