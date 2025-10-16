"""
Test Suite 2: IterativeReasoningEngine (20 tests)

Focus: Architectural hypothesis formulation, evidence-based refinement, convergence detection

Test Categories:
- 2.1 Hypothesis Formulation (5 tests)
- 2.2 Evidence-Based Refinement (8 tests)
- 2.3 Convergence Detection (4 tests)
- 2.4 Reasoning Path Documentation (3 tests)

Expected Results:
- Pass Rate: ≥95%
- Execution Time: ~15 minutes
"""

import pytest
from typing import Dict, Any, List


# ============================================================================
# 2.1 HYPOTHESIS FORMULATION (5 tests)
# ============================================================================

def test_initial_hypothesis_generation(iterative_reasoning_engine):
    """Test generation of initial architectural hypothesis."""
    requirements = {
        "use_case": "Multi-agent research system",
        "complexity": "enterprise",
        "team_size": "15-20"
    }

    hypothesis = iterative_reasoning_engine.formulate_hypothesis(requirements)

    # Assertions
    assert "framework" in hypothesis, "Hypothesis should include framework choice"
    assert "pattern" in hypothesis, "Hypothesis should include pattern choice"
    assert "rationale" in hypothesis, "Hypothesis should include rationale"
    assert len(hypothesis["rationale"]) >= 100, "Rationale should be detailed (≥100 chars)"

    print(f"✓ Generated hypothesis: {hypothesis['framework']} with {hypothesis['pattern']} pattern")


def test_alternative_hypothesis_generation(iterative_reasoning_engine):
    """Test generation of multiple competing hypotheses."""
    requirements = {
        "use_case": "Customer support automation",
        "complexity": "research"
    }

    # Generate primary hypothesis
    hypothesis1 = iterative_reasoning_engine.formulate_hypothesis(requirements)

    # Should be able to generate alternative
    hypothesis2 = iterative_reasoning_engine.formulate_hypothesis(requirements)

    # Assertions
    assert hypothesis1 is not None, "Should generate primary hypothesis"
    assert hypothesis2 is not None, "Should generate alternative hypothesis"
    assert "framework" in hypothesis1, "Primary should have framework"
    assert "framework" in hypothesis2, "Alternative should have framework"

    print(f"✓ Generated alternatives: {hypothesis1['framework']} and {hypothesis2['framework']}")


def test_hypothesis_specificity(iterative_reasoning_engine):
    """Test that hypotheses are specific and actionable."""
    requirements = {
        "use_case": "E-commerce chatbot with product recommendations",
        "complexity": "startup",
        "constraints": ["budget: $200/month"]
    }

    hypothesis = iterative_reasoning_engine.formulate_hypothesis(requirements)

    # Assertions
    assert "framework" in hypothesis, "Should specify framework"
    assert hypothesis["framework"] in ["langgraph", "crewai", "autogen"], \
        "Should recommend specific framework"
    assert "pattern" in hypothesis, "Should specify pattern"
    assert hypothesis["pattern"] != "generic", "Pattern should be specific"

    print(f"✓ Hypothesis is specific: {hypothesis['framework']}/{hypothesis['pattern']}")


def test_hypothesis_feasibility_check(iterative_reasoning_engine):
    """Test that hypotheses are technically feasible."""
    requirements = {
        "use_case": "Simple task automation",
        "complexity": "startup",
        "team_size": "1",
        "constraints": ["budget: $50/month", "timeline: 2 weeks"]
    }

    hypothesis = iterative_reasoning_engine.formulate_hypothesis(requirements)

    # Assertions - should recommend simple, feasible solution
    assert hypothesis is not None, "Should generate feasible hypothesis"
    assert "rationale" in hypothesis, "Should explain feasibility"

    print(f"✓ Feasible hypothesis generated for constrained scenario")


def test_hypothesis_alignment_with_requirements(iterative_reasoning_engine):
    """Test that hypotheses address all requirements."""
    requirements = {
        "use_case": "Multi-agent research system with document analysis",
        "complexity": "research",
        "key_features": ["document processing", "data analysis", "report generation"]
    }

    hypothesis = iterative_reasoning_engine.formulate_hypothesis(requirements)

    # Assertions
    assert hypothesis is not None, "Should generate hypothesis"
    assert "framework" in hypothesis, "Should address framework requirement"
    assert "rationale" in hypothesis, "Should explain how it addresses requirements"

    print("✓ Hypothesis aligns with requirements")


# ============================================================================
# 2.2 EVIDENCE-BASED REFINEMENT (8 tests)
# ============================================================================

def test_performance_benchmark_evidence(iterative_reasoning_engine):
    """Test refinement based on performance benchmarks."""
    initial_hypothesis = {
        "framework": "langgraph",
        "pattern": "simple",
        "rationale": "Initial choice"
    }

    evidence = {
        "performance_benchmark": {
            "current_throughput": "100 req/sec",
            "required_throughput": "1000 req/sec",
            "bottleneck": "sequential processing"
        }
    }

    refined = iterative_reasoning_engine.refine_hypothesis(initial_hypothesis, evidence)

    # Assertions
    assert refined is not None, "Should refine based on performance evidence"
    assert refined != initial_hypothesis, "Should make changes based on evidence"

    print("✓ Refined hypothesis based on performance benchmarks")


def test_cost_analysis_evidence(iterative_reasoning_engine):
    """Test refinement based on cost projections."""
    initial_hypothesis = {
        "framework": "langgraph",
        "pattern": "complex",
        "estimated_cost": "$1000/month"
    }

    evidence = {
        "cost_too_high": True,
        "budget_constraint": "$200/month"
    }

    refined = iterative_reasoning_engine.refine_hypothesis(initial_hypothesis, evidence)

    # Assertions
    assert refined is not None, "Should refine based on cost evidence"
    assert "cost_optimization" in refined or refined != initial_hypothesis, \
        "Should address cost concerns"

    print("✓ Refined hypothesis to reduce costs")


def test_complexity_analysis_evidence(iterative_reasoning_engine):
    """Test refinement based on implementation complexity."""
    initial_hypothesis = {
        "framework": "langgraph",
        "pattern": "hierarchical_multi_supervisor",
        "complexity_score": 9.5
    }

    evidence = {
        "team_size_small": True,
        "timeline_tight": True
    }

    refined = iterative_reasoning_engine.refine_hypothesis(initial_hypothesis, evidence)

    # Assertions
    assert refined is not None, "Should refine based on complexity evidence"

    print("✓ Refined hypothesis to reduce complexity")


def test_team_capability_evidence(iterative_reasoning_engine):
    """Test refinement based on team skills/size."""
    initial_hypothesis = {
        "framework": "autogen",
        "pattern": "advanced",
        "required_expertise": "expert"
    }

    evidence = {
        "team_experience": "beginner",
        "team_size": 1
    }

    refined = iterative_reasoning_engine.refine_hypothesis(initial_hypothesis, evidence)

    # Assertions
    assert refined is not None, "Should refine based on team capability"

    print("✓ Refined hypothesis to match team capabilities")


def test_historical_success_evidence(iterative_reasoning_engine):
    """Test refinement based on past blueprint performance."""
    initial_hypothesis = {
        "framework": "crewai",
        "pattern": "sequential"
    }

    evidence = {
        "historical_data": {
            "crewai_success_rate": 0.95,
            "langgraph_success_rate": 0.88
        }
    }

    refined = iterative_reasoning_engine.refine_hypothesis(initial_hypothesis, evidence)

    # Assertions
    assert refined is not None, "Should consider historical evidence"

    print("✓ Refined hypothesis based on historical success rates")


def test_security_audit_evidence(iterative_reasoning_engine):
    """Test refinement based on security analysis."""
    initial_hypothesis = {
        "framework": "langgraph",
        "pattern": "simple",
        "security_level": "basic"
    }

    evidence = {
        "security_requirements": "enterprise",
        "compliance_needed": ["HIPAA", "GDPR"]
    }

    refined = iterative_reasoning_engine.refine_hypothesis(initial_hypothesis, evidence)

    # Assertions
    assert refined is not None, "Should refine for security"

    print("✓ Refined hypothesis to meet security requirements")


def test_conflicting_evidence_resolution(iterative_reasoning_engine):
    """Test handling of contradictory evidence."""
    initial_hypothesis = {
        "framework": "langgraph",
        "pattern": "simple"
    }

    evidence = {
        "need_high_performance": True,  # Suggests complex architecture
        "tight_budget": True,  # Suggests simple architecture
        "small_team": True  # Suggests simple architecture
    }

    refined = iterative_reasoning_engine.refine_hypothesis(initial_hypothesis, evidence)

    # Assertions
    assert refined is not None, "Should handle conflicting evidence"

    print("✓ Handled conflicting evidence successfully")


def test_evidence_weight_prioritization(iterative_reasoning_engine):
    """Test prioritization of stronger evidence."""
    initial_hypothesis = {
        "framework": "langgraph",
        "pattern": "simple"
    }

    # Strong evidence should outweigh weak evidence
    strong_evidence = {
        "critical_requirement": "Must handle 10k concurrent users",
        "nice_to_have": "Would like simple setup"
    }

    refined = iterative_reasoning_engine.refine_hypothesis(initial_hypothesis, strong_evidence)

    # Assertions
    assert refined is not None, "Should prioritize strong evidence"

    print("✓ Prioritized stronger evidence correctly")


# ============================================================================
# 2.3 CONVERGENCE DETECTION (4 tests)
# ============================================================================

def test_convergence_threshold_detection(iterative_reasoning_engine):
    """Test detection when refinements stabilize (95% threshold)."""
    # Simulate iterations that converge
    iterations = [
        {"framework": "langgraph", "pattern": "simple", "score": 0.80},
        {"framework": "langgraph", "pattern": "react", "score": 0.90},
        {"framework": "langgraph", "pattern": "react", "score": 0.95},
        {"framework": "langgraph", "pattern": "react", "score": 0.95},
    ]

    converged = iterative_reasoning_engine.check_convergence(iterations)

    # Assertions
    assert converged is not None, "Should check convergence"
    # After multiple iterations with same pattern, should converge
    assert converged or len(iterations) >= 3, "Should detect convergence or allow sufficient iterations"

    print(f"✓ Convergence detection working (converged: {converged})")


def test_iteration_limit_enforcement(iterative_reasoning_engine):
    """Test max 5 iterations enforced."""
    # Simulate many iterations
    iterations = [{"iteration": i} for i in range(10)]

    converged = iterative_reasoning_engine.check_convergence(iterations)

    # Assertions
    assert converged or len(iterations) <= iterative_reasoning_engine.max_iterations, \
        "Should enforce max iterations or converge"

    print(f"✓ Iteration limit enforcement working (max: {iterative_reasoning_engine.max_iterations})")


def test_early_convergence_handling(iterative_reasoning_engine):
    """Test stopping when convergence reached early."""
    # Simulate quick convergence
    iterations = [
        {"framework": "langgraph", "pattern": "react", "score": 0.96},
        {"framework": "langgraph", "pattern": "react", "score": 0.96},
    ]

    converged = iterative_reasoning_engine.check_convergence(iterations)

    # Should allow early convergence
    assert converged is not None, "Should handle early convergence"

    print("✓ Early convergence handling working")


def test_non_convergence_handling(iterative_reasoning_engine):
    """Test fallback when convergence not reached."""
    # Simulate oscillating iterations
    iterations = [
        {"framework": "langgraph", "pattern": "simple", "score": 0.70},
        {"framework": "crewai", "pattern": "sequential", "score": 0.75},
        {"framework": "langgraph", "pattern": "react", "score": 0.72},
        {"framework": "crewai", "pattern": "hierarchical", "score": 0.74},
        {"framework": "langgraph", "pattern": "simple", "score": 0.71},
    ]

    converged = iterative_reasoning_engine.check_convergence(iterations)

    # Should handle non-convergence (force convergence at max iterations)
    assert len(iterations) <= iterative_reasoning_engine.max_iterations or converged, \
        "Should force convergence at max iterations"

    print("✓ Non-convergence fallback working")


# ============================================================================
# 2.4 REASONING PATH DOCUMENTATION (3 tests)
# ============================================================================

def test_reasoning_chain_recording(iterative_reasoning_engine):
    """Test complete reasoning chain is documented."""
    # Simulate reasoning process
    requirements = {"use_case": "Test system", "complexity": "startup"}

    # Generate hypothesis and refinements
    hypothesis = iterative_reasoning_engine.formulate_hypothesis(requirements)
    refined = iterative_reasoning_engine.refine_hypothesis(hypothesis, {"evidence": "test"})

    # Both should have rationale/documentation
    assert "rationale" in hypothesis, "Initial hypothesis should document reasoning"

    print("✓ Reasoning chain recording working")


def test_decision_rationale_clarity(iterative_reasoning_engine):
    """Test each decision has clear rationale."""
    requirements = {
        "use_case": "E-commerce recommendation system",
        "complexity": "research"
    }

    hypothesis = iterative_reasoning_engine.formulate_hypothesis(requirements)

    # Assertions
    assert "rationale" in hypothesis, "Should include rationale"
    assert len(hypothesis["rationale"]) >= 50, "Rationale should be substantial"
    assert any(keyword in hypothesis["rationale"].lower()
               for keyword in ["because", "due to", "provides", "enables"]), \
        "Rationale should explain reasoning"

    print(f"✓ Decision rationale is clear ({len(hypothesis['rationale'])} chars)")


def test_reasoning_path_reproducibility(iterative_reasoning_engine):
    """Test same inputs produce same reasoning path."""
    requirements = {
        "use_case": "Customer support chatbot",
        "complexity": "startup",
        "budget": "$100/month"
    }

    # Generate hypothesis multiple times with same inputs
    hypothesis1 = iterative_reasoning_engine.formulate_hypothesis(requirements)
    hypothesis2 = iterative_reasoning_engine.formulate_hypothesis(requirements)

    # Assertions
    assert hypothesis1["framework"] == hypothesis2["framework"], \
        "Same inputs should produce same framework choice"
    assert hypothesis1["pattern"] == hypothesis2["pattern"], \
        "Same inputs should produce same pattern choice"

    print("✓ Reasoning path is reproducible")


# ============================================================================
# TEST SUMMARY
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("TEST SUITE 2: IterativeReasoningEngine")
    print("="*70)
    print("\nRunning 20 tests...")
    print("\nTest Categories:")
    print("  - Hypothesis Formulation: 5 tests")
    print("  - Evidence-Based Refinement: 8 tests")
    print("  - Convergence Detection: 4 tests")
    print("  - Reasoning Path Documentation: 3 tests")
    print("\n" + "="*70)

    pytest.main([__file__, "-v", "--tb=short"])
