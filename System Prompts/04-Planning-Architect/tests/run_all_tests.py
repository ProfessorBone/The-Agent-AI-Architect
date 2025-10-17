#!/usr/bin/env python3
"""
Phase 2 Testing - Comprehensive Test Runner

Executes all 9 test suites for Planning Architect v3.0 and generates
comprehensive reports with pass rates, timings, and baseline metrics.

Usage:
    python run_all_tests.py [--suite SUITE_NUMBER] [--verbose] [--html]

Examples:
    python run_all_tests.py                    # Run all suites
    python run_all_tests.py --suite 1          # Run only suite 1
    python run_all_tests.py --verbose --html   # Verbose with HTML report
"""

import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
import argparse


class Phase2TestRunner:
    """Orchestrates execution of all Phase 2 test suites."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.test_dir = Path(__file__).parent

        self.suites = {
            1: {"name": "MetaAnalysisEngine", "tests": 25, "critical": True},
            2: {"name": "IterativeReasoningEngine", "tests": 20, "critical": True},
            3: {"name": "AutomatedEvaluationEngine", "tests": 20, "critical": True},
            4: {"name": "HierarchicalMemorySystem", "tests": 25, "critical": True},
            5: {"name": "DefensiveSecurityEngine", "tests": 20, "critical": True},
            6: {"name": "PatternImplementations", "tests": 30, "critical": False},
            7: {"name": "ToolSelectionAlgorithm", "tests": 15, "critical": True},
            8: {"name": "IntegrationWorkflows", "tests": 20, "critical": False},
            9: {"name": "QualityValidation", "tests": 25, "critical": False},
        }

        self.results = {
            "start_time": datetime.now().isoformat(),
            "suites": {},
            "summary": {}
        }

    def run_suite(self, suite_num: int, verbose: bool = False) -> Dict[str, Any]:
        """Run a single test suite."""
        suite_info = self.suites[suite_num]
        suite_file = self.test_dir / f"test_suite_{suite_num:02d}_{self._snake_case(suite_info['name'])}.py"

        if not suite_file.exists():
            return {
                "status": "skipped",
                "reason": f"Test file not found: {suite_file}",
                "passed": 0,
                "failed": 0,
                "skipped": suite_info["tests"]
            }

        print(f"\n{'='*70}")
        print(f"Running Test Suite {suite_num}: {suite_info['name']}")
        print(f"{'='*70}")
        print(f"Expected tests: {suite_info['tests']}")
        print(f"Critical: {'YES' if suite_info['critical'] else 'NO'}")
        print()

        # Run pytest
        cmd = [
            "pytest",
            str(suite_file),
            "-v" if verbose else "-q",
            "--tb=short",
            f"--html={self.output_dir}/suite_{suite_num:02d}_report.html",
            "--self-contained-html",
            "--json-report",
            f"--json-report-file={self.output_dir}/suite_{suite_num:02d}_results.json"
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)

            # Parse results from JSON if available
            json_file = self.output_dir / f"suite_{suite_num:02d}_results.json"
            if json_file.exists():
                with open(json_file) as f:
                    test_data = json.load(f)
                    return {
                        "status": "completed",
                        "passed": test_data.get("summary", {}).get("passed", 0),
                        "failed": test_data.get("summary", {}).get("failed", 0),
                        "skipped": test_data.get("summary", {}).get("skipped", 0),
                        "duration": test_data.get("duration", 0),
                        "exit_code": result.returncode
                    }
            else:
                # Fallback: parse pytest output
                return self._parse_pytest_output(result.stdout, result.returncode)

        except subprocess.TimeoutExpired:
            return {
                "status": "timeout",
                "passed": 0,
                "failed": suite_info["tests"],
                "skipped": 0,
                "duration": 600
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "passed": 0,
                "failed": suite_info["tests"],
                "skipped": 0
            }

    def _parse_pytest_output(self, output: str, exit_code: int) -> Dict[str, Any]:
        """Parse pytest output to extract results."""
        # Simple parsing - look for summary line
        passed, failed, skipped = 0, 0, 0

        for line in output.split('\n'):
            if 'passed' in line.lower():
                try:
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if 'passed' in part and i > 0:
                            passed = int(parts[i-1])
                        elif 'failed' in part and i > 0:
                            failed = int(parts[i-1])
                        elif 'skipped' in part and i > 0:
                            skipped = int(parts[i-1])
                except:
                    pass

        return {
            "status": "completed",
            "passed": passed,
            "failed": failed,
            "skipped": skipped,
            "exit_code": exit_code
        }

    def run_all_suites(self, verbose: bool = False, specific_suite: int = None):
        """Run all test suites or a specific suite."""
        suites_to_run = [specific_suite] if specific_suite else list(self.suites.keys())

        for suite_num in suites_to_run:
            suite_info = self.suites[suite_num]
            result = self.run_suite(suite_num, verbose)

            self.results["suites"][suite_num] = {
                "name": suite_info["name"],
                "expected_tests": suite_info["tests"],
                "critical": suite_info["critical"],
                **result
            }

            # Print summary
            self._print_suite_summary(suite_num, result)

        # Calculate overall summary
        self._calculate_summary()

        # Save results
        self._save_results()

        # Print final summary
        self._print_final_summary()

    def _print_suite_summary(self, suite_num: int, result: Dict[str, Any]):
        """Print summary for a single suite."""
        passed = result.get("passed", 0)
        failed = result.get("failed", 0)
        skipped = result.get("skipped", 0)
        total = passed + failed + skipped

        pass_rate = (passed / total * 100) if total > 0 else 0

        status_icon = "✓" if failed == 0 and passed > 0 else "✗" if failed > 0 else "○"

        print(f"\n{status_icon} Suite {suite_num} Results:")
        print(f"   Passed:  {passed}/{total} ({pass_rate:.1f}%)")
        if failed > 0:
            print(f"   Failed:  {failed}")
        if skipped > 0:
            print(f"   Skipped: {skipped}")
        if "duration" in result:
            print(f"   Duration: {result['duration']:.2f}s")

    def _calculate_summary(self):
        """Calculate overall summary statistics."""
        total_passed = sum(r.get("passed", 0) for r in self.results["suites"].values())
        total_failed = sum(r.get("failed", 0) for r in self.results["suites"].values())
        total_skipped = sum(r.get("skipped", 0) for r in self.results["suites"].values())
        total_tests = total_passed + total_failed + total_skipped

        critical_suites = [s for s, r in self.results["suites"].items()
                          if self.suites[s]["critical"]]
        critical_passed = sum(self.results["suites"][s].get("passed", 0)
                            for s in critical_suites)
        critical_failed = sum(self.results["suites"][s].get("failed", 0)
                            for s in critical_suites)
        critical_total = critical_passed + critical_failed

        self.results["summary"] = {
            "total_tests": total_tests,
            "total_passed": total_passed,
            "total_failed": total_failed,
            "total_skipped": total_skipped,
            "overall_pass_rate": (total_passed / total_tests * 100) if total_tests > 0 else 0,
            "critical_pass_rate": (critical_passed / critical_total * 100) if critical_total > 0 else 0,
            "suites_run": len(self.results["suites"]),
            "end_time": datetime.now().isoformat()
        }

    def _save_results(self):
        """Save results to JSON file."""
        results_file = self.output_dir / "phase2_comprehensive_results.json"
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"\n✓ Results saved to: {results_file}")

    def _print_final_summary(self):
        """Print final comprehensive summary."""
        summary = self.results["summary"]

        print("\n" + "="*70)
        print("PHASE 2 TESTING - FINAL SUMMARY")
        print("="*70)
        print(f"\nTotal Tests:     {summary['total_tests']}")
        print(f"Passed:          {summary['total_passed']}")
        print(f"Failed:          {summary['total_failed']}")
        print(f"Skipped:         {summary['total_skipped']}")
        print(f"\nOverall Pass Rate:  {summary['overall_pass_rate']:.1f}%")
        print(f"Critical Pass Rate: {summary['critical_pass_rate']:.1f}%")

        # Success criteria
        print("\n" + "-"*70)
        print("SUCCESS CRITERIA")
        print("-"*70)

        criteria = [
            ("Overall Pass Rate ≥90%", summary['overall_pass_rate'] >= 90),
            ("Critical Pass Rate = 100%", summary['critical_pass_rate'] == 100),
            ("Total Failed = 0", summary['total_failed'] == 0),
        ]

        for criterion, met in criteria:
            icon = "✓" if met else "✗"
            print(f"{icon} {criterion}")

        overall_success = all(met for _, met in criteria)
        print(f"\n{'='*70}")
        if overall_success:
            print("🎉 PHASE 2 TESTING: SUCCESS!")
            print("Ready to proceed to Phase 3 (Modularization)")
        else:
            print("⚠️  PHASE 2 TESTING: INCOMPLETE")
            print("Review failed tests before proceeding to Phase 3")
        print(f"{'='*70}\n")

    def _snake_case(self, name: str) -> str:
        """Convert CamelCase to snake_case."""
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Phase 2 Test Runner")
    parser.add_argument("--suite", type=int, help="Run specific suite number (1-9)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--html", action="store_true", help="Generate HTML reports")
    parser.add_argument("--output-dir", default="./test_results",
                       help="Output directory for results")

    args = parser.parse_args()

    # Create runner
    runner = Phase2TestRunner(Path(args.output_dir))

    # Run tests
    try:
        runner.run_all_suites(
            verbose=args.verbose,
            specific_suite=args.suite
        )
    except KeyboardInterrupt:
        print("\n\nTest execution interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nError during test execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
