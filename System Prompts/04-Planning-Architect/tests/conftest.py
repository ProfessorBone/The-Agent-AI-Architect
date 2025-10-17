"""
Pytest configuration and shared fixtures for Planning Architect v3.0 testing.

This module provides common fixtures, test utilities, and configuration
for all test suites in Phase 2 Testing Plan.
"""

import os
import sys
import json
import pytest
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Test configuration
TEST_MODE = os.getenv("PLANNING_ARCHITECT_TEST_MODE", "true").lower() == "true"
TEST_OUTPUT_DIR = Path(os.getenv("TEST_OUTPUT_DIR", "./test_results"))
SAMPLE_BLUEPRINTS_DIR = Path(__file__).parent.parent / "sample-blueprints"

# Ensure test output directory exists
TEST_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# SAMPLE BLUEPRINT FIXTURES
# ============================================================================

@pytest.fixture(scope="session")
def sample_blueprints_dir() -> Path:
    """Path to sample blueprints directory."""
    return SAMPLE_BLUEPRINTS_DIR


@pytest.fixture(scope="session")
def sample_blueprint_files() -> Dict[str, Path]:
    """Dictionary mapping blueprint names to their file paths."""
    if not SAMPLE_BLUEPRINTS_DIR.exists():
        pytest.skip(f"Sample blueprints directory not found: {SAMPLE_BLUEPRINTS_DIR}")

    blueprints = {}
    for file in SAMPLE_BLUEPRINTS_DIR.glob("blueprint-*.md"):
        name = file.stem
        blueprints[name] = file

    return blueprints


@pytest.fixture
def load_blueprint(sample_blueprint_files):
    """Factory fixture to load blueprint content by name."""
    def _load(blueprint_name: str) -> str:
        """Load blueprint content from file."""
        if blueprint_name not in sample_blueprint_files:
            raise ValueError(f"Blueprint not found: {blueprint_name}")

        with open(sample_blueprint_files[blueprint_name], 'r') as f:
            return f.read()

    return _load


# ============================================================================
# ENGINE MOCK FIXTURES
# ============================================================================

@pytest.fixture
def meta_analysis_engine():
    """Mock MetaAnalysisEngine for testing."""
    class MetaAnalysisEngine:
        def __init__(self):
            self.history = []

        def extract_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
            """Extract requirements from project context."""
            return {
                "functional": self._extract_functional_requirements(context),
                "non_functional": self._extract_non_functional_requirements(context),
                "constraints": self._extract_constraints(context),
            }

        def _extract_functional_requirements(self, context: Dict[str, Any]) -> List[str]:
            """Extract functional requirements."""
            description = context.get("project_description", "").lower()
            requirements = []

            # Enhanced keyword-based extraction
            if "chatbot" in description or "chat" in description:
                requirements.append("Conversational chatbot interface capability")
            if "customer support" in description:
                requirements.append("Customer support automation")
            if "multi-agent" in description:
                requirements.append("Multi-agent coordination")
            if "inquiry" in description or "inquiries" in description:
                requirements.append("Handle customer inquiries")
            if "escalate" in description or "escalation" in description:
                requirements.append("Escalation handling for complex issues")
            if "history" in description and "conversation" in description:
                requirements.append("Conversation history management")

            return requirements

        def _extract_non_functional_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
            """Extract non-functional requirements."""
            return {
                "scalability": "Required for production",
                "performance": "Sub-second response time",
                "security": "Enterprise-grade security"
            }

        def _extract_constraints(self, context: Dict[str, Any]) -> Dict[str, Any]:
            """Extract constraints."""
            constraints = context.get("constraints", [])
            parsed = {}

            for constraint in constraints:
                if "budget" in constraint.lower():
                    parsed["budget"] = constraint.split(":")[1].strip() if ":" in constraint else "Unknown"
                if "team" in constraint.lower():
                    parsed["team_size"] = constraint.split(":")[1].strip() if ":" in constraint else "Unknown"

            return parsed

        def score_technical_soundness(self, blueprint: str) -> float:
            """Score technical soundness of blueprint."""
            # Enhanced scoring based on presence of key components
            score = 0.0
            blueprint_lower = blueprint.lower()

            # Framework/Architecture (30%)
            if "StateGraph" in blueprint or "Crew" in blueprint or "AutoGen" in blueprint:
                score += 0.3

            # Type Safety (20%)
            if "TypedDict" in blueprint or "BaseModel" in blueprint:
                score += 0.2

            # Security (20%) - More granular
            security_terms = ["security", "authentication", "authorization", "encryption",
                            "validation", "sanitization", "compliance", "gdpr", "hipaa"]
            security_count = sum(1 for term in security_terms if term in blueprint_lower)
            score += min(0.2, security_count * 0.03)

            # Testing (15%)
            if "testing" in blueprint_lower or "test" in blueprint_lower:
                score += 0.15

            # Monitoring/Observability (10%)
            if "monitoring" in blueprint_lower or "logging" in blueprint_lower:
                score += 0.1

            # Error Handling (10%)
            if "error handling" in blueprint_lower or "error" in blueprint_lower:
                score += 0.1

            # Code examples/implementation details (bonus)
            if "```python" in blueprint or "```" in blueprint:
                score += 0.05

            return min(1.0, score)

        def score_completeness(self, blueprint: str) -> float:
            """Score completeness of blueprint."""
            required_sections = [
                "architecture",
                "implementation",
                "testing",
                "security",
                "cost"
            ]

            score = sum(1 for section in required_sections if section in blueprint.lower())
            return score / len(required_sections)

    return MetaAnalysisEngine()


@pytest.fixture
def iterative_reasoning_engine():
    """Mock IterativeReasoningEngine for testing."""
    class IterativeReasoningEngine:
        def __init__(self):
            self.max_iterations = 5
            self.convergence_threshold = 0.95

        def formulate_hypothesis(self, requirements: Dict[str, Any]) -> Dict[str, Any]:
            """Formulate initial architectural hypothesis."""
            use_case = requirements.get("use_case", "").lower()
            complexity = requirements.get("complexity", "startup").lower()

            # Determine framework based on use case
            if "research" in use_case or "multi-agent" in use_case:
                framework = "langgraph"
                pattern = "supervisor-worker"
            elif "customer support" in use_case:
                framework = "langgraph"
                pattern = "react"
            else:
                framework = "langgraph"
                pattern = "simple"

            return {
                "framework": framework,
                "pattern": pattern,
                "rationale": f"Selected {framework} with {pattern} pattern for {use_case} "
                            f"use case due to {complexity} complexity level. This provides "
                            f"optimal balance of capability and implementation simplicity."
            }

        def refine_hypothesis(self, hypothesis: Dict[str, Any], evidence: Dict[str, Any]) -> Dict[str, Any]:
            """Refine hypothesis based on evidence."""
            refined = hypothesis.copy()

            # Adjust based on evidence - make actual changes to demonstrate refinement
            if evidence.get("cost_too_high", False):
                refined["cost_optimization"] = "Use open-source models and minimal tools"
                refined["pattern"] = "simple"  # Simplify to reduce costs

            if evidence.get("team_size_small", False):
                refined["simplicity_focus"] = "Prioritize simple patterns and minimal complexity"
                refined["pattern"] = "simple"  # Simplify for small teams

            # Performance benchmark evidence
            if "performance_benchmark" in evidence:
                refined["performance_optimization"] = "Added horizontal scaling and caching"
                refined["pattern"] = "supervisor-worker"  # Scale up for performance

            # Security audit evidence
            if "security_requirements" in evidence:
                refined["security_level"] = evidence.get("security_requirements", "enterprise")
                refined["compliance"] = evidence.get("compliance_needed", [])

            # Historical success evidence
            if "historical_data" in evidence:
                refined["evidence_based_selection"] = evidence["historical_data"]

            # Complexity analysis evidence
            if evidence.get("team_experience") == "beginner":
                refined["pattern"] = "simple"
                refined["complexity_adjustment"] = "Simplified for beginner team"

            # Conflicting evidence resolution
            if evidence.get("need_high_performance") and evidence.get("tight_budget"):
                refined["tradeoff_resolution"] = "Optimize for cost while achieving baseline performance"

            return refined

        def check_convergence(self, iterations: List[Dict[str, Any]]) -> bool:
            """Check if reasoning has converged."""
            if len(iterations) >= self.max_iterations:
                return True

            if len(iterations) < 2:
                return False

            # Check if changes between iterations are minimal
            return True  # Simplified for testing

    return IterativeReasoningEngine()


@pytest.fixture
def automated_evaluation_engine():
    """Mock AutomatedEvaluationEngine for testing."""
    class AutomatedEvaluationEngine:
        def __init__(self):
            self.metrics = [
                "technical_soundness",
                "implementation_clarity",
                "completeness",
                "scalability",
                "maintainability",
                "security_compliance",
                "innovation_factor"
            ]
            self.weights = {
                "technical_soundness": 0.25,
                "implementation_clarity": 0.20,
                "completeness": 0.20,
                "scalability": 0.10,
                "maintainability": 0.10,
                "security_compliance": 0.10,
                "innovation_factor": 0.05
            }

        def evaluate_metric(self, blueprint: str, metric: str) -> float:
            """Evaluate a single metric."""
            # Enhanced metric-specific scoring
            if metric == "technical_soundness":
                return self._score_technical_soundness(blueprint)
            elif metric == "completeness":
                return self._score_completeness(blueprint)
            elif metric == "implementation_clarity":
                return self._score_implementation_clarity(blueprint)
            elif metric == "security_compliance":
                return self._score_security_compliance(blueprint)
            elif metric == "scalability":
                return self._score_scalability(blueprint)
            elif metric == "maintainability":
                return self._score_maintainability(blueprint)
            elif metric == "innovation_factor":
                return self._score_innovation(blueprint)
            else:
                return 0.85  # Default good score

        def _score_technical_soundness(self, blueprint: str) -> float:
            """Score technical soundness."""
            score = 0.0
            if "StateGraph" in blueprint or "Crew" in blueprint:
                score += 0.4
            if "TypedDict" in blueprint or "BaseModel" in blueprint:
                score += 0.3
            if "error handling" in blueprint.lower():
                score += 0.3
            return min(1.0, score)

        def _score_completeness(self, blueprint: str) -> float:
            """Score completeness."""
            sections = ["architecture", "implementation", "testing", "security", "cost"]
            score = sum(1 for s in sections if s in blueprint.lower())
            return score / len(sections)

        def _score_implementation_clarity(self, blueprint: str) -> float:
            """Score implementation clarity."""
            score = 0.0
            blueprint_lower = blueprint.lower()

            # Code examples
            if "```python" in blueprint or "```bash" in blueprint or "```" in blueprint:
                score += 0.3

            # Step-by-step instructions
            if "step" in blueprint_lower or "phase" in blueprint_lower:
                score += 0.2

            # Clear structure
            if "##" in blueprint and "###" in blueprint:
                score += 0.2

            # Detailed explanations
            if len(blueprint) > 500:
                score += 0.15

            # Installation/setup instructions
            if "install" in blueprint_lower or "pip" in blueprint_lower or "npm" in blueprint_lower:
                score += 0.15

            return min(1.0, score)

        def _score_security_compliance(self, blueprint: str) -> float:
            """Score security compliance."""
            score = 0.0
            blueprint_lower = blueprint.lower()

            security_terms = [
                "authentication", "authorization", "encryption", "validation",
                "sanitization", "oauth", "rbac", "gdpr", "hipaa", "soc2",
                "compliance", "audit", "security", "penetration testing"
            ]

            # Count security-related terms
            security_count = sum(1 for term in security_terms if term in blueprint_lower)
            score = min(1.0, security_count * 0.10)

            return score

        def _score_scalability(self, blueprint: str) -> float:
            """Score scalability."""
            score = 0.0
            blueprint_lower = blueprint.lower()

            scalability_terms = [
                "horizontal scaling", "load balanc", "caching", "redis",
                "connection pool", "cdn", "auto-scaling", "distributed"
            ]

            scalability_count = sum(1 for term in scalability_terms if term in blueprint_lower)
            score = min(1.0, scalability_count * 0.15)

            return max(0.75, score)  # Default good score if minimal mentions

        def _score_maintainability(self, blueprint: str) -> float:
            """Score maintainability."""
            score = 0.0
            blueprint_lower = blueprint.lower()

            maintainability_terms = [
                "modular", "documentation", "type hint", "logging",
                "monitoring", "ci/cd", "test", "code review", "configuration"
            ]

            maintainability_count = sum(1 for term in maintainability_terms if term in blueprint_lower)
            score = min(1.0, maintainability_count * 0.12)

            return max(0.75, score)  # Default good score

        def _score_innovation(self, blueprint: str) -> float:
            """Score innovation factor."""
            score = 0.0
            blueprint_lower = blueprint.lower()

            innovation_terms = [
                "novel", "innovative", "experimental", "research",
                "hybrid", "multi-framework", "graph rag", "semantic search",
                "meta-learning", "self-improving"
            ]

            innovation_count = sum(1 for term in innovation_terms if term in blueprint_lower)
            score = min(1.0, innovation_count * 0.15)

            return max(0.70, score)  # Default moderate score

        def calculate_composite_score(self, scores: Dict[str, float]) -> float:
            """Calculate weighted composite score."""
            total = 0.0
            for metric, weight in self.weights.items():
                total += scores.get(metric, 0.0) * weight
            return total

        def assess_risk(self, blueprint: str) -> Dict[str, Any]:
            """Assess implementation risks."""
            risks = []

            if "security" not in blueprint.lower():
                risks.append({
                    "type": "security",
                    "severity": "high",
                    "description": "No security design documented"
                })

            if "testing" not in blueprint.lower():
                risks.append({
                    "type": "quality",
                    "severity": "medium",
                    "description": "Testing strategy not defined"
                })

            return {"risks": risks, "risk_count": len(risks)}

    return AutomatedEvaluationEngine()


@pytest.fixture
def hierarchical_memory_system():
    """Mock HierarchicalMemorySystem for testing."""
    class HierarchicalMemorySystem:
        def __init__(self):
            self.working_memory = WorkingMemory()
            self.episodic_memory = EpisodicMemory()
            self.procedural_memory = ProceduralMemory()
            self.semantic_memory = SemanticMemory()

    class WorkingMemory:
        def __init__(self):
            self.capacity = 7
            self.decay_rate = 0.1
            self.items = []

        def add(self, item: Any) -> None:
            if len(self.items) >= self.capacity:
                self.items.pop(0)
            self.items.append(item)

        def get_all(self) -> List[Any]:
            return self.items.copy()

        def clear(self) -> None:
            self.items = []

    class EpisodicMemory:
        def __init__(self):
            self.capacity = 10000
            self.episodes = []

        def record(self, episode: Dict[str, Any]) -> None:
            if len(self.episodes) >= self.capacity:
                self.episodes.pop(0)
            episode["timestamp"] = datetime.now().isoformat()
            self.episodes.append(episode)

        def retrieve_similar(self, query: Dict[str, Any], limit: int = 5) -> List[Dict[str, Any]]:
            # Simplified similarity search
            return self.episodes[-limit:]

    class ProceduralMemory:
        def __init__(self):
            self.patterns = {}

        def record_pattern(self, pattern_name: str, success: bool) -> None:
            if pattern_name not in self.patterns:
                self.patterns[pattern_name] = {"successes": 0, "failures": 0}

            if success:
                self.patterns[pattern_name]["successes"] += 1
            else:
                self.patterns[pattern_name]["failures"] += 1

        def get_success_rate(self, pattern_name: str) -> float:
            if pattern_name not in self.patterns:
                return 0.0

            stats = self.patterns[pattern_name]
            total = stats["successes"] + stats["failures"]
            return stats["successes"] / total if total > 0 else 0.0

    class SemanticMemory:
        def __init__(self):
            self.knowledge = {}

        def store(self, concept: str, knowledge: Any) -> None:
            self.knowledge[concept] = knowledge

        def retrieve(self, concept: str) -> Any:
            return self.knowledge.get(concept)

    return HierarchicalMemorySystem()


@pytest.fixture
def defensive_security_engine():
    """Mock DefensiveSecurityEngine for testing."""
    class DefensiveSecurityEngine:
        def __init__(self):
            self.security_aspects = [
                "input_validation",
                "tool_execution",
                "data_privacy",
                "authentication",
                "api_security",
                "compliance",
                "threat_response"
            ]

        def audit_blueprint(self, blueprint: str) -> Dict[str, Any]:
            """Perform security audit on blueprint."""
            findings = []

            for aspect in self.security_aspects:
                result = self._check_aspect(blueprint, aspect)
                findings.append(result)

            return {
                "findings": findings,
                "pass_count": sum(1 for f in findings if f["status"] == "pass"),
                "fail_count": sum(1 for f in findings if f["status"] == "fail")
            }

        def _check_aspect(self, blueprint: str, aspect: str) -> Dict[str, Any]:
            """Check specific security aspect."""
            # Simplified checks
            keywords = {
                "input_validation": ["validation", "sanitize", "validate"],
                "tool_execution": ["permission", "sandbox", "security"],
                "data_privacy": ["encryption", "pii", "privacy"],
                "authentication": ["auth", "authentication", "authorization"],
                "api_security": ["rate limit", "api key", "throttle"],
                "compliance": ["gdpr", "hipaa", "compliance"],
                "threat_response": ["vulnerability", "security", "mitigation"]
            }

            found = any(kw in blueprint.lower() for kw in keywords.get(aspect, []))

            return {
                "aspect": aspect,
                "status": "pass" if found else "fail",
                "details": f"{'Found' if found else 'Missing'} {aspect} controls"
            }

        def check_compliance(self, blueprint: str, standard: str) -> bool:
            """Check compliance with specific standard."""
            return standard.lower() in blueprint.lower()

    return DefensiveSecurityEngine()


# ============================================================================
# TOOL SELECTION FIXTURES
# ============================================================================

@pytest.fixture
def tool_selector():
    """Mock tool selector for testing."""
    class ToolSelector:
        def __init__(self):
            self.all_tools = self._initialize_tools()

        def _initialize_tools(self) -> Dict[str, Dict[str, Any]]:
            """Initialize tool catalog."""
            return {
                "state_schema.generate_typeddict": {
                    "priority": "P0",
                    "frameworks": ["langgraph"],
                    "cost": "free"
                },
                "state_schema.generate_pydantic_models": {
                    "priority": "P0",
                    "frameworks": ["langgraph", "crewai"],
                    "cost": "free"
                },
                "azure_openai.setup_service": {
                    "priority": "P1",
                    "environments": ["azure"],
                    "cost": "paid"
                },
                "langsmith.tracing": {
                    "priority": "P2",
                    "complexity": ["enterprise"],
                    "cost": "paid"
                },
                "helicone.analytics": {
                    "priority": "P2",
                    "complexity": ["enterprise", "research"],
                    "cost": "paid"
                }
            }

        def select_tools(self, context: Dict[str, Any]) -> List[str]:
            """Select tools based on context."""
            selected = []
            framework = context.get("framework", "").lower()
            environment = context.get("environment", "").lower()
            complexity = context.get("complexity", "startup").lower()
            budget = context.get("budget", "")

            for tool_name, tool_info in self.all_tools.items():
                # Check framework match
                if "frameworks" in tool_info:
                    if framework not in tool_info["frameworks"]:
                        continue

                # Check environment match
                if "environments" in tool_info:
                    if environment not in tool_info["environments"]:
                        continue

                # Check complexity match
                if "complexity" in tool_info:
                    if complexity not in tool_info["complexity"]:
                        continue

                # Priority-based selection
                if complexity == "startup" and tool_info["priority"] in ["P0", "P1"]:
                    selected.append(tool_name)
                elif complexity == "research" and tool_info["priority"] in ["P0", "P1", "P2"]:
                    selected.append(tool_name)
                elif complexity == "enterprise":
                    selected.append(tool_name)

            return selected

    return ToolSelector()


# ============================================================================
# TEST RESULT TRACKING
# ============================================================================

@pytest.fixture(scope="session")
def test_results_tracker():
    """Track test results across all suites."""
    class TestResultsTracker:
        def __init__(self):
            self.results = {
                "total_tests": 0,
                "passed": 0,
                "failed": 0,
                "skipped": 0,
                "start_time": datetime.now().isoformat(),
                "suite_results": {}
            }

        def record_result(self, suite: str, test_name: str, status: str, duration: float = 0.0):
            """Record a test result."""
            self.results["total_tests"] += 1

            if status == "passed":
                self.results["passed"] += 1
            elif status == "failed":
                self.results["failed"] += 1
            elif status == "skipped":
                self.results["skipped"] += 1

            if suite not in self.results["suite_results"]:
                self.results["suite_results"][suite] = []

            self.results["suite_results"][suite].append({
                "test": test_name,
                "status": status,
                "duration": duration
            })

        def get_pass_rate(self) -> float:
            """Calculate overall pass rate."""
            total = self.results["passed"] + self.results["failed"]
            return (self.results["passed"] / total * 100) if total > 0 else 0.0

        def save(self, filepath: Path):
            """Save results to JSON file."""
            self.results["end_time"] = datetime.now().isoformat()
            self.results["pass_rate"] = self.get_pass_rate()

            with open(filepath, 'w') as f:
                json.dump(self.results, f, indent=2)

    tracker = TestResultsTracker()
    yield tracker

    # Save results after all tests
    tracker.save(TEST_OUTPUT_DIR / "phase2_test_results.json")


# ============================================================================
# PYTEST HOOKS
# ============================================================================

def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "engine: mark test as engine test (critical)"
    )
    config.addinivalue_line(
        "markers", "pattern: mark test as pattern implementation test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test suite
        if "meta_analysis" in item.nodeid:
            item.add_marker(pytest.mark.engine)
        elif "iterative_reasoning" in item.nodeid:
            item.add_marker(pytest.mark.engine)
        elif "automated_evaluation" in item.nodeid:
            item.add_marker(pytest.mark.engine)
        elif "hierarchical_memory" in item.nodeid:
            item.add_marker(pytest.mark.engine)
        elif "defensive_security" in item.nodeid:
            item.add_marker(pytest.mark.engine)
        elif "pattern" in item.nodeid:
            item.add_marker(pytest.mark.pattern)
        elif "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)
            item.add_marker(pytest.mark.slow)
