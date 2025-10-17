# Phase 2 Testing - Planning Architect v3.0

Comprehensive test suite for validating Planning Architect v3.0 before modularization.

## Overview

- **Total Tests**: 230 tests across 9 suites
- **Timeline**: 7 days (Week 1)
- **Objective**: Pre-Modularization Baseline Validation
- **Success Criteria**: ≥90% overall pass rate, 100% engine tests

## Test Suites

| Suite | Name | Tests | Focus | Critical |
|-------|------|-------|-------|----------|
| 1 | MetaAnalysisEngine | 25 | Self-improving architecture design | ✓ |
| 2 | IterativeReasoningEngine | 20 | Hypothesis formulation & refinement | ✓ |
| 3 | AutomatedEvaluationEngine | 20 | 7-metric blueprint evaluation | ✓ |
| 4 | HierarchicalMemorySystem | 25 | 4-tier memory architecture | ✓ |
| 5 | DefensiveSecurityEngine | 20 | 7-aspect security audit | ✓ |
| 6 | PatternImplementations | 30 | LangGraph, CrewAI, AutoGen patterns | - |
| 7 | ToolSelectionAlgorithm | 15 | Context-aware tool selection | ✓ |
| 8 | IntegrationWorkflows | 20 | End-to-end workflows | - |
| 9 | QualityValidation | 25 | Output quality validation | - |

## Quick Start

### 1. Install Dependencies

```bash
# From the tests directory
pip install -r requirements-test.txt
```

### 2. Run All Tests

```bash
# Run all 230 tests
python run_all_tests.py

# Run with verbose output
python run_all_tests.py --verbose

# Run with HTML reports
python run_all_tests.py --html
```

### 3. Run Specific Suite

```bash
# Run only Suite 1 (MetaAnalysisEngine)
python run_all_tests.py --suite 1

# Run specific suite with pytest directly
pytest test_suite_01_meta_analysis_engine.py -v
```

### 4. Run with Coverage

```bash
pytest --cov=. --cov-report=html --cov-report=term
```

## Test Execution Options

```bash
# Run all tests in parallel (faster)
pytest -n auto

# Run until first failure (debugging)
pytest -x

# Run with detailed output
pytest -vv --tb=long

# Run only engine tests (critical)
pytest -m engine

# Run only pattern tests
pytest -m pattern

# Generate comprehensive HTML report
pytest --html=test_results/report.html --self-contained-html
```

## Directory Structure

```
tests/
├── README.md                          # This file
├── requirements-test.txt              # Test dependencies
├── conftest.py                        # Shared fixtures and configuration
├── run_all_tests.py                   # Comprehensive test runner
│
├── test_suite_01_meta_analysis_engine.py        # 25 tests
├── test_suite_02_iterative_reasoning_engine.py  # 20 tests
├── test_suite_03_automated_evaluation_engine.py # 20 tests (placeholder)
├── test_suite_04_hierarchical_memory_system.py  # 25 tests (placeholder)
├── test_suite_05_defensive_security_engine.py   # 20 tests (placeholder)
├── test_suite_06_pattern_implementations.py     # 30 tests (placeholder)
├── test_suite_07_tool_selection_algorithm.py    # 15 tests (placeholder)
├── test_suite_08_integration_workflows.py       # 20 tests (placeholder)
└── test_suite_09_quality_validation.py          # 25 tests (placeholder)
```

## Success Criteria

### Quantitative Metrics

| Metric | Target | Critical |
|--------|--------|----------|
| Overall Pass Rate | ≥90% | Yes |
| Engine Test Pass Rate | 100% | Yes |
| Pattern Test Pass Rate | ≥95% | No |
| Tool Selection Accuracy | 100% | Yes |
| Integration Test Pass Rate | ≥90% | No |
| Quality Test Pass Rate | ≥90% | No |

### Qualitative Metrics

- ✅ All 5 revolutionary engines operational
- ✅ Pattern implementations faithful to frameworks
- ✅ Tool selection rationale clear and justified
- ✅ Integration between engines seamless
- ✅ Output quality matches sample blueprints

## Test Results

Test results are saved to `test_results/` directory:

```
test_results/
├── phase2_comprehensive_results.json   # Overall results
├── suite_01_report.html               # Suite 1 HTML report
├── suite_01_results.json              # Suite 1 JSON results
├── ...                                # Reports for all suites
└── coverage/                          # Coverage reports
    └── index.html
```

## Viewing Results

```bash
# View comprehensive results
cat test_results/phase2_comprehensive_results.json | jq

# Open HTML report in browser
open test_results/suite_01_report.html

# View coverage report
open test_results/coverage/index.html
```

## Troubleshooting

### Missing Sample Blueprints

If tests fail with "Sample blueprints directory not found", ensure sample blueprints are present:

```bash
ls -la ../sample-blueprints/
# Should show blueprint-1-langgraph-startup.md, etc.
```

### Pytest Not Found

```bash
# Install pytest
pip install pytest

# Or install all test dependencies
pip install -r requirements-test.txt
```

### Import Errors

```bash
# Ensure parent directory is in Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/.."

# Or run tests from project root
cd ..
pytest tests/ -v
```

## Development Workflow

### Adding New Tests

1. Add test to appropriate suite file
2. Update test count in `run_all_tests.py`
3. Run specific suite to validate: `pytest test_suite_XX_name.py -v`
4. Run full test suite to ensure no regressions

### Running Tests During Development

```bash
# Watch mode - re-run tests on file changes (requires pytest-watch)
pip install pytest-watch
ptw tests/ -- -v

# Run only failed tests from last run
pytest --lf

# Run tests matching pattern
pytest -k "test_technical_soundness"
```

## Baseline Metrics

These tests establish baseline metrics for comparison after modularization:

1. **Blueprint Generation Time**
   - Startup: TBD
   - Enterprise: TBD

2. **Engine Execution Time**
   - MetaAnalysisEngine: TBD
   - IterativeReasoningEngine: TBD
   - AutomatedEvaluationEngine: TBD
   - HierarchicalMemorySystem: TBD
   - DefensiveSecurityEngine: TBD

3. **Quality Metrics**
   - Average validation score: TBD
   - Tool selection accuracy: TBD
   - Pattern correctness: TBD

## Next Steps

After Phase 2 completion:

1. ✅ Review all test results
2. ✅ Fix any critical (P0) bugs
3. ✅ Document baseline metrics
4. ✅ Prepare Phase 3 readiness assessment
5. ✅ Proceed to Phase 3 (Modularization)

## Contact

For questions or issues with the test suite, refer to:
- [PHASE_2_TESTING_PLAN.md](../PHASE_2_TESTING_PLAN.md) - Comprehensive testing plan
- [Planning Architect README](../README.md) - System overview

---

**Created**: October 2025
**Status**: Phase 2 Testing in Progress
**Goal**: 230 tests, ≥90% pass rate, 100% engine tests
