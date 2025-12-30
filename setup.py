from setuptools import setup, find_packages

setup(
    name="decimal-physics-controller",
    version="0.1.0",
    author="David A. Besemer",
    description="Precise physics simulations using decimal arithmetic",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/davidbesemer132/decimal-physics-controller",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "numpy",
        "scipy",
    ],
)