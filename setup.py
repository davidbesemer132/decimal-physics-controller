#!/usr/bin/env python
"""Setup configuration for Decimal Physics Controller."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="decimal-physics-controller",
    version="0.1.0",
    author="David A. Besemer",
    description="A Python library for precise physics simulations using decimal arithmetic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidbesemer132/decimal-physics-controller",
    project_urls={
        "Bug Tracker": "https://github.com/davidbesemer132/decimal-physics-controller/issues",
        "Documentation": "https://github.com/davidbesemer132/decimal-physics-controller/wiki",
        "Source Code": "https://github.com/davidbesemer132/decimal-physics-controller",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "License :: Creative Commons Attribution 4.0 International",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
            "pytest-benchmark>=4.0.0",
            "black>=21.0",
            "flake8>=3.9.0",
            "mypy>=0.900",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
        "notebooks": [
            "jupyter>=1.0.0",
            "notebook>=6.4.0",
            "ipykernel>=6.0.0",
        ],
        "benchmarks": [
            "pytest-benchmark>=4.0.0",
            "memory-profiler>=0.60",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
