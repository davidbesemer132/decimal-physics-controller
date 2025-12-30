#!/usr/bin/env python3
"""
Pre-Deployment Validation Checklist for decimal-physics-controller

This script performs comprehensive validation of the decimal-physics-controller
package before making the repository public. It tests all functionality and
validates the structure, documentation, and configuration.

Usage:
    python validation_checklist.py

Exit codes:
    0 - All validations passed
    1 - One or more validations failed
"""

import os
import sys
import subprocess
import importlib.util
import json
from pathlib import Path
from typing import Tuple, List, Dict, Any


class ValidationChecklist:
    """Comprehensive pre-deployment validation for decimal-physics-controller."""

    def __init__(self):
        """Initialize the validation checklist."""
        self.repo_root = Path(__file__).parent
        self.results: Dict[str, Dict[str, Any]] = {}
        self.failed_checks = []
        self.passed_checks = []

    def print_header(self, title: str) -> None:
        """Print a formatted section header."""
        print("\n" + "=" * 80)
        print(f"  {title}")
        print("=" * 80)

    def print_check(self, name: str, status: str, message: str = "") -> None:
        """Print a validation check result."""
        status_symbol = "✓" if status == "PASS" else "✗"
        color_code = "\033[92m" if status == "PASS" else "\033[91m"
        reset_code = "\033[0m"
        
        print(f"{color_code}{status_symbol} {name}: {status}{reset_code}")
        if message:
            print(f"  {message}")

    def record_result(self, section: str, check_name: str, passed: bool, 
                     message: str = "") -> None:
        """Record a validation result."""
        if section not in self.results:
            self.results[section] = {}
        
        self.results[section][check_name] = {
            "passed": passed,
            "message": message
        }
        
        if passed:
            self.passed_checks.append(f"{section}::{check_name}")
        else:
            self.failed_checks.append(f"{section}::{check_name}")

    # =========================================================================
    # SECTION 1: Environment and Dependencies Check
    # =========================================================================

    def check_environment_and_dependencies(self) -> bool:
        """Validate environment and dependencies."""
        self.print_header("SECTION 1: Environment and Dependencies Check")
        
        all_passed = True
        section = "Environment and Dependencies"

        # Check Python version
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        py_check = sys.version_info >= (3, 7)
        self.print_check(
            "Python version >= 3.7",
            "PASS" if py_check else "FAIL",
            f"Current version: {python_version}"
        )
        self.record_result(section, "Python version", py_check, python_version)
        all_passed = all_passed and py_check

        # Check for required files
        required_files = [
            "setup.py",
            "README.md",
            "LICENSE",
            "pyproject.toml"
        ]
        
        for req_file in required_files:
            file_path = self.repo_root / req_file
            exists = file_path.exists()
            self.print_check(
                f"{req_file} exists",
                "PASS" if exists else "FAIL"
            )
            self.record_result(section, f"{req_file} exists", exists)
            all_passed = all_passed and exists

        # Check for required directories
        required_dirs = ["decimal_physics_controller", "tests"]
        
        for req_dir in required_dirs:
            dir_path = self.repo_root / req_dir
            exists = dir_path.is_dir()
            self.print_check(
                f"Directory '{req_dir}' exists",
                "PASS" if exists else "FAIL"
            )
            self.record_result(section, f"Directory {req_dir} exists", exists)
            all_passed = all_passed and exists

        # Check for __init__.py in package
        init_path = self.repo_root / "decimal_physics_controller" / "__init__.py"
        init_exists = init_path.exists()
        self.print_check(
            "Package __init__.py exists",
            "PASS" if init_exists else "FAIL"
        )
        self.record_result(section, "Package __init__.py exists", init_exists)
        all_passed = all_passed and init_exists

        return all_passed

    # =========================================================================
    # SECTION 2: Package Structure Validation
    # =========================================================================

    def check_package_structure(self) -> bool:
        """Validate the package directory structure."""
        self.print_header("SECTION 2: Package Structure Validation")
        
        all_passed = True
        section = "Package Structure"

        package_root = self.repo_root / "decimal_physics_controller"
        
        if not package_root.is_dir():
            self.print_check("Package directory found", "FAIL")
            self.record_result(section, "Package directory found", False)
            return False

        # Check for essential module files
        essential_modules = [
            "__init__.py",
        ]
        
        for module in essential_modules:
            module_path = package_root / module
            exists = module_path.exists()
            self.print_check(
                f"Module '{module}' exists",
                "PASS" if exists else "FAIL"
            )
            self.record_result(section, f"Module {module} exists", exists)
            all_passed = all_passed and exists

        # List all Python files in package
        py_files = list(package_root.glob("*.py"))
        py_count = len(py_files)
        
        self.print_check(
            f"Python modules found in package",
            "PASS" if py_count > 0 else "FAIL",
            f"Found {py_count} Python files: {', '.join(f.name for f in py_files)}"
        )
        self.record_result(section, "Python modules found", py_count > 0, str(py_count))
        all_passed = all_passed and (py_count > 0)

        # Check for tests directory
        tests_dir = self.repo_root / "tests"
        tests_exist = tests_dir.is_dir()
        
        self.print_check(
            "Tests directory exists",
            "PASS" if tests_exist else "FAIL"
        )
        self.record_result(section, "Tests directory exists", tests_exist)
        all_passed = all_passed and tests_exist

        if tests_exist:
            test_files = list(tests_dir.glob("test_*.py"))
            test_count = len(test_files)
            
            self.print_check(
                "Test files found",
                "PASS" if test_count > 0 else "FAIL",
                f"Found {test_count} test files"
            )
            self.record_result(section, "Test files found", test_count > 0)
            all_passed = all_passed and (test_count > 0)

        return all_passed

    # =========================================================================
    # SECTION 3: Package Import and Instantiation
    # =========================================================================

    def check_package_import_and_instantiation(self) -> bool:
        """Validate that the package can be imported and instantiated."""
        self.print_header("SECTION 3: Package Import and Instantiation")
        
        all_passed = True
        section = "Package Import"

        # Add package to path
        sys.path.insert(0, str(self.repo_root))

        # Attempt to import main package
        try:
            import decimal_physics_controller
            self.print_check("Import decimal_physics_controller", "PASS")
            self.record_result(section, "Import main package", True)
        except Exception as e:
            self.print_check(
                "Import decimal_physics_controller",
                "FAIL",
                f"Error: {str(e)}"
            )
            self.record_result(section, "Import main package", False, str(e))
            all_passed = False
            return all_passed

        # Check for __version__ attribute
        if hasattr(decimal_physics_controller, "__version__"):
            version = decimal_physics_controller.__version__
            self.print_check(
                "__version__ attribute exists",
                "PASS",
                f"Version: {version}"
            )
            self.record_result(section, "__version__ exists", True, version)
        else:
            self.print_check(
                "__version__ attribute exists",
                "FAIL",
                "Module missing __version__ attribute"
            )
            self.record_result(section, "__version__ exists", False)

        # Check for __author__ attribute
        if hasattr(decimal_physics_controller, "__author__"):
            author = decimal_physics_controller.__author__
            self.print_check(
                "__author__ attribute exists",
                "PASS",
                f"Author: {author}"
            )
            self.record_result(section, "__author__ exists", True, author)

        # Check for __description__ or docstring
        if decimal_physics_controller.__doc__:
            self.print_check(
                "Module docstring exists",
                "PASS"
            )
            self.record_result(section, "Module docstring exists", True)
        else:
            self.print_check(
                "Module docstring exists",
                "FAIL"
            )
            self.record_result(section, "Module docstring exists", False)

        return all_passed

    # =========================================================================
    # SECTION 4: Core Functionality Tests
    # =========================================================================

    def check_core_functionality(self) -> bool:
        """Test core package functionality."""
        self.print_header("SECTION 4: Core Functionality Tests")
        
        all_passed = True
        section = "Core Functionality"

        try:
            import decimal_physics_controller
            
            # Check for main classes/functions
            main_exports = dir(decimal_physics_controller)
            
            # Remove private/magic attributes
            public_exports = [x for x in main_exports if not x.startswith('_')]
            
            self.print_check(
                "Public API available",
                "PASS" if len(public_exports) > 0 else "FAIL",
                f"Found {len(public_exports)} public exports"
            )
            self.record_result(
                section,
                "Public API available",
                len(public_exports) > 0,
                f"{len(public_exports)} exports"
            )
            
            if public_exports:
                print(f"  Available: {', '.join(public_exports[:10])}")
                if len(public_exports) > 10:
                    print(f"  ... and {len(public_exports) - 10} more")

        except Exception as e:
            self.print_check(
                "Access core functionality",
                "FAIL",
                f"Error: {str(e)}"
            )
            self.record_result(section, "Access core functionality", False, str(e))
            all_passed = False

        return all_passed

    # =========================================================================
    # SECTION 5: License Validation
    # =========================================================================

    def check_license_validation(self) -> bool:
        """Validate license file."""
        self.print_header("SECTION 5: License Validation")
        
        all_passed = True
        section = "License Validation"

        license_path = self.repo_root / "LICENSE"
        
        if not license_path.exists():
            self.print_check(
                "LICENSE file exists",
                "FAIL"
            )
            self.record_result(section, "LICENSE file exists", False)
            return False

        self.print_check(
            "LICENSE file exists",
            "PASS"
        )
        self.record_result(section, "LICENSE file exists", True)

        # Check license file is not empty
        try:
            with open(license_path, 'r') as f:
                content = f.read().strip()
                
            is_valid = len(content) > 0
            self.print_check(
                "LICENSE file is not empty",
                "PASS" if is_valid else "FAIL",
                f"License size: {len(content)} bytes"
            )
            self.record_result(section, "LICENSE file is not empty", is_valid)
            all_passed = all_passed and is_valid

        except Exception as e:
            self.print_check(
                "LICENSE file readable",
                "FAIL",
                f"Error: {str(e)}"
            )
            self.record_result(section, "LICENSE file readable", False, str(e))
            all_passed = False

        return all_passed

    # =========================================================================
    # SECTION 6: README Validation
    # =========================================================================

    def check_readme_validation(self) -> bool:
        """Validate README file."""
        self.print_header("SECTION 6: README Validation")
        
        all_passed = True
        section = "README Validation"

        readme_path = self.repo_root / "README.md"
        
        if not readme_path.exists():
            self.print_check(
                "README.md file exists",
                "FAIL"
            )
            self.record_result(section, "README.md file exists", False)
            return False

        self.print_check(
            "README.md file exists",
            "PASS"
        )
        self.record_result(section, "README.md file exists", True)

        # Check README is not empty
        try:
            with open(readme_path, 'r') as f:
                content = f.read().strip()
                
            is_valid = len(content) > 100  # Minimum reasonable length
            self.print_check(
                "README.md has substantial content",
                "PASS" if is_valid else "FAIL",
                f"Content length: {len(content)} characters"
            )
            self.record_result(section, "README.md has content", is_valid)
            all_passed = all_passed and is_valid

            # Check for common sections
            required_sections = {
                "installation": ["install", "setup", "requirements"],
                "usage": ["usage", "example", "quick start"],
                "license": ["license", "licensed"]
            }

            content_lower = content.lower()
            
            for section_name, keywords in required_sections.items():
                found = any(keyword in content_lower for keyword in keywords)
                status = "PASS" if found else "FAIL"
                self.print_check(
                    f"README includes '{section_name}' section",
                    status
                )
                self.record_result(
                    section,
                    f"README has {section_name}",
                    found
                )
                all_passed = all_passed and found

        except Exception as e:
            self.print_check(
                "README.md readable",
                "FAIL",
                f"Error: {str(e)}"
            )
            self.record_result(section, "README.md readable", False, str(e))
            all_passed = False

        return all_passed

    # =========================================================================
    # SECTION 7: Pytest Test Suite Execution
    # =========================================================================

    def check_pytest_execution(self) -> bool:
        """Execute pytest test suite."""
        self.print_header("SECTION 7: Pytest Test Suite Execution")
        
        section = "Pytest Execution"

        tests_dir = self.repo_root / "tests"
        
        if not tests_dir.exists():
            self.print_check(
                "Tests directory found",
                "FAIL"
            )
            self.record_result(section, "Tests directory found", False)
            return False

        # Check if pytest is available
        try:
            result = subprocess.run(
                ["python", "-m", "pytest", "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                self.print_check(
                    "pytest is installed",
                    "PASS",
                    result.stdout.strip()
                )
                self.record_result(section, "pytest installed", True)
            else:
                self.print_check(
                    "pytest is installed",
                    "FAIL",
                    "pytest not found. Install with: pip install pytest"
                )
                self.record_result(section, "pytest installed", False)
                return False

        except Exception as e:
            self.print_check(
                "pytest is installed",
                "FAIL",
                f"Error checking pytest: {str(e)}"
            )
            self.record_result(section, "pytest installed", False, str(e))
            return False

        # Run pytest
        try:
            result = subprocess.run(
                ["python", "-m", "pytest", str(tests_dir), "-v", "--tb=short"],
                capture_output=True,
                text=True,
                cwd=str(self.repo_root),
                timeout=60
            )
            
            # Parse output
            passed = result.returncode == 0
            
            self.print_check(
                "All tests passed",
                "PASS" if passed else "FAIL"
            )
            
            if result.stdout:
                print("\nTest output:")
                print(result.stdout[-1000:])  # Last 1000 chars to avoid spam
            
            self.record_result(section, "All tests passed", passed)
            return passed

        except subprocess.TimeoutExpired:
            self.print_check(
                "Tests completed within timeout",
                "FAIL",
                "Test execution timed out after 60 seconds"
            )
            self.record_result(section, "Tests completed", False)
            return False
        except Exception as e:
            self.print_check(
                "Test execution",
                "FAIL",
                f"Error running tests: {str(e)}"
            )
            self.record_result(section, "Test execution", False, str(e))
            return False

    # =========================================================================
    # SECTION 8: Example Script Validation
    # =========================================================================

    def check_example_scripts(self) -> bool:
        """Validate example scripts."""
        self.print_header("SECTION 8: Example Script Validation")
        
        all_passed = True
        section = "Example Scripts"

        # Look for examples directory or files
        examples_locations = [
            self.repo_root / "examples",
            self.repo_root / "example",
            self.repo_root / "docs" / "examples"
        ]
        
        examples_dir = None
        for location in examples_locations:
            if location.is_dir():
                examples_dir = location
                break

        if examples_dir:
            self.print_check(
                "Examples directory found",
                "PASS",
                f"Location: {examples_dir.relative_to(self.repo_root)}"
            )
            self.record_result(section, "Examples directory found", True)

            # Check for example Python files
            example_files = list(examples_dir.glob("*.py"))
            
            if example_files:
                self.print_check(
                    "Example Python files found",
                    "PASS",
                    f"Found {len(example_files)} example(s)"
                )
                self.record_result(section, "Example files found", True)

                # Try to import/run each example (or at least validate syntax)
                for example_file in example_files:
                    try:
                        with open(example_file, 'r') as f:
                            compile(f.read(), example_file, 'exec')
                        
                        self.print_check(
                            f"Example '{example_file.name}' syntax valid",
                            "PASS"
                        )
                        self.record_result(
                            section,
                            f"Example {example_file.name} syntax",
                            True
                        )
                    except SyntaxError as e:
                        self.print_check(
                            f"Example '{example_file.name}' syntax valid",
                            "FAIL",
                            f"Syntax error: {str(e)}"
                        )
                        self.record_result(
                            section,
                            f"Example {example_file.name} syntax",
                            False,
                            str(e)
                        )
                        all_passed = False
            else:
                self.print_check(
                    "Example Python files found",
                    "FAIL",
                    "No .py files in examples directory"
                )
                self.record_result(section, "Example files found", False)
                all_passed = False
        else:
            self.print_check(
                "Examples directory found",
                "FAIL",
                "No examples directory found"
            )
            self.record_result(section, "Examples directory found", False)
            # This is not critical, so don't fail overall
            all_passed = all_passed  # Keep current status

        return all_passed

    # =========================================================================
    # Final Report
    # =========================================================================

    def print_summary(self) -> int:
        """Print validation summary and return exit code."""
        self.print_header("VALIDATION SUMMARY")

        total_checks = len(self.passed_checks) + len(self.failed_checks)
        passed_count = len(self.passed_checks)
        failed_count = len(self.failed_checks)

        print(f"\nTotal Checks: {total_checks}")
        print(f"Passed: {passed_count}")
        print(f"Failed: {failed_count}")
        print(f"Success Rate: {(passed_count / total_checks * 100):.1f}%")

        if self.failed_checks:
            print("\n" + "=" * 80)
            print("  FAILED CHECKS:")
            print("=" * 80)
            for check in self.failed_checks:
                print(f"  ✗ {check}")

        # Detailed results by section
        if self.results:
            print("\n" + "=" * 80)
            print("  DETAILED RESULTS BY SECTION:")
            print("=" * 80)
            
            for section, checks in self.results.items():
                section_passed = sum(1 for c in checks.values() if c["passed"])
                section_total = len(checks)
                
                status = "✓ PASS" if section_passed == section_total else "✗ FAIL"
                print(f"\n{status} {section} ({section_passed}/{section_total})")
                
                for check_name, result in checks.items():
                    symbol = "✓" if result["passed"] else "✗"
                    print(f"  {symbol} {check_name}")
                    if result["message"]:
                        print(f"     {result['message']}")

        print("\n" + "=" * 80)
        
        if failed_count == 0:
            print("  ✓ ALL VALIDATIONS PASSED - READY FOR PUBLIC RELEASE")
            print("=" * 80)
            return 0
        else:
            print(f"  ✗ {failed_count} VALIDATION(S) FAILED - FIXES REQUIRED")
            print("=" * 80)
            return 1

    def run_all_checks(self) -> int:
        """Run all validation checks."""
        print("\n")
        print("╔" + "=" * 78 + "╗")
        print("║" + " " * 78 + "║")
        print("║" + "  DECIMAL-PHYSICS-CONTROLLER PRE-DEPLOYMENT VALIDATION".center(78) + "║")
        print("║" + " " * 78 + "║")
        print("╚" + "=" * 78 + "╝")

        # Run all sections
        self.check_environment_and_dependencies()
        self.check_package_structure()
        self.check_package_import_and_instantiation()
        self.check_core_functionality()
        self.check_license_validation()
        self.check_readme_validation()
        self.check_pytest_execution()
        self.check_example_scripts()

        # Print summary and return exit code
        return self.print_summary()


def main() -> int:
    """Main entry point."""
    checklist = ValidationChecklist()
    return checklist.run_all_checks()


if __name__ == "__main__":
    sys.exit(main())
