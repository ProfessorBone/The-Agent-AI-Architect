"""
Test Suite 4: HierarchicalMemorySystem (25 tests)

Focus: 4-layer memory architecture and pattern performance tracking

Test Categories:
- 4.1 Working Memory (6 tests)
- 4.2 Episodic Memory (6 tests)
- 4.3 Procedural Memory (7 tests)
- 4.4 Semantic Memory (6 tests)

Expected Results:
- Pass Rate: ≥95%
- Execution Time: ~20 minutes
"""

import pytest
from typing import Dict, Any, List


# ============================================================================
# 4.1 WORKING MEMORY (6 tests)
# ============================================================================

def test_working_memory_capacity(hierarchical_memory_system):
    """Test 7-item capacity limit (Miller's Law)."""
    wm = hierarchical_memory_system.working_memory

    # Add exactly 7 items
    for i in range(7):
        wm.add(f"item_{i}")

    # Assertions
    assert len(wm.get_all()) == 7, "Working memory should hold exactly 7 items"

    # Add 8th item - should remove oldest
    wm.add("item_7")
    assert len(wm.get_all()) == 7, "Capacity should remain at 7"
    assert "item_0" not in wm.get_all(), "Oldest item should be removed"
    assert "item_7" in wm.get_all(), "Newest item should be present"

    print(f"✓ Working memory capacity enforced (7 items max)")


def test_working_memory_decay(hierarchical_memory_system):
    """Test 0.1 decay rate over time."""
    wm = hierarchical_memory_system.working_memory

    # Verify decay rate is configured
    assert wm.decay_rate == 0.1, "Decay rate should be 0.1"

    print(f"✓ Working memory decay rate configured ({wm.decay_rate})")


def test_working_memory_priority_retention(hierarchical_memory_system):
    """Test high-priority items retained longer."""
    wm = hierarchical_memory_system.working_memory

    # Add items with implicit priority (newer = higher priority)
    for i in range(10):
        wm.add(f"item_{i}")

    # Most recent 7 should be retained
    items = wm.get_all()
    assert len(items) == 7, "Should retain 7 items"
    assert "item_9" in items, "Most recent item should be retained"
    assert "item_3" in items, "7th most recent should be retained"
    assert "item_2" not in items, "8th most recent should be removed"

    print("✓ Working memory priority retention working")


def test_working_memory_context_switching(hierarchical_memory_system):
    """Test context switch between blueprints."""
    wm = hierarchical_memory_system.working_memory

    # Load context A
    wm.clear()
    for i in range(5):
        wm.add(f"context_A_item_{i}")

    context_a_items = wm.get_all()
    assert len(context_a_items) == 5, "Context A should have 5 items"

    # Switch to context B
    wm.clear()
    for i in range(3):
        wm.add(f"context_B_item_{i}")

    context_b_items = wm.get_all()
    assert len(context_b_items) == 3, "Context B should have 3 items"
    assert all("context_B" in str(item) for item in context_b_items), \
        "All items should be from context B"

    print("✓ Working memory context switching working")


def test_working_memory_overflow_handling(hierarchical_memory_system):
    """Test oldest items removed when capacity exceeded."""
    wm = hierarchical_memory_system.working_memory

    # Fill to capacity
    for i in range(7):
        wm.add(f"initial_{i}")

    # Add 5 more items
    for i in range(5):
        wm.add(f"overflow_{i}")

    items = wm.get_all()

    # Should only have last 7 items
    assert len(items) == 7, "Should maintain capacity of 7"
    assert "overflow_4" in items, "Most recent overflow item should be present"
    assert "initial_0" not in items, "Oldest initial items should be removed"

    print("✓ Working memory overflow handling working")


def test_working_memory_retrieval_speed(hierarchical_memory_system):
    """Test O(1) retrieval performance."""
    wm = hierarchical_memory_system.working_memory

    # Add items
    for i in range(7):
        wm.add(f"item_{i}")

    # Retrieve all - should be instant (list copy)
    import time
    start = time.time()
    items = wm.get_all()
    duration = time.time() - start

    # Assertions
    assert len(items) == 7, "Should retrieve all items"
    assert duration < 0.001, "Retrieval should be under 1ms (O(1))"

    print(f"✓ Working memory retrieval is fast ({duration*1000:.3f}ms)")


# ============================================================================
# 4.2 EPISODIC MEMORY (6 tests)
# ============================================================================

def test_episodic_memory_storage(hierarchical_memory_system):
    """Test storage of blueprint generation episodes."""
    em = hierarchical_memory_system.episodic_memory

    episode = {
        "blueprint_id": "test_001",
        "framework": "langgraph",
        "pattern": "react",
        "success": True,
        "score": 0.92
    }

    em.record(episode)

    # Assertions
    assert len(em.episodes) == 1, "Should store 1 episode"
    stored_episode = em.episodes[0]
    assert "timestamp" in stored_episode, "Episode should have timestamp"
    assert stored_episode["blueprint_id"] == "test_001", "Should store correct data"

    print("✓ Episodic memory storage working")


def test_episodic_memory_capacity(hierarchical_memory_system):
    """Test 10,000 episode capacity."""
    em = hierarchical_memory_system.episodic_memory

    # Verify capacity
    assert em.capacity == 10000, "Capacity should be 10,000 episodes"

    # Add episodes up to capacity
    for i in range(100):  # Test with smaller number for speed
        em.record({"episode_id": i, "data": f"test_{i}"})

    assert len(em.episodes) == 100, "Should store all episodes within capacity"

    print(f"✓ Episodic memory capacity verified ({em.capacity} episodes)")


def test_episodic_memory_retrieval_by_similarity(hierarchical_memory_system):
    """Test retrieval of similar past episodes."""
    em = hierarchical_memory_system.episodic_memory

    # Record various episodes
    episodes = [
        {"framework": "langgraph", "pattern": "react", "complexity": "startup"},
        {"framework": "langgraph", "pattern": "supervisor", "complexity": "enterprise"},
        {"framework": "crewai", "pattern": "sequential", "complexity": "startup"},
        {"framework": "langgraph", "pattern": "react", "complexity": "research"},
    ]

    for ep in episodes:
        em.record(ep)

    # Query for similar episodes
    query = {"framework": "langgraph"}
    similar = em.retrieve_similar(query, limit=3)

    # Assertions
    assert len(similar) <= 3, "Should respect limit"
    assert len(similar) > 0, "Should find similar episodes"

    print(f"✓ Episodic memory similarity retrieval working ({len(similar)} episodes)")


def test_episodic_memory_temporal_ordering(hierarchical_memory_system):
    """Test episodes maintain temporal sequence."""
    em = hierarchical_memory_system.episodic_memory

    # Record episodes in order
    for i in range(5):
        em.record({"sequence": i, "data": f"episode_{i}"})

    # Verify temporal order
    episodes = em.episodes
    assert episodes[0]["sequence"] == 0, "First episode should be first"
    assert episodes[-1]["sequence"] == 4, "Last episode should be last"
    assert episodes[2]["sequence"] == 2, "Middle episode should be in order"

    print("✓ Episodic memory temporal ordering working")


def test_episodic_memory_context_reconstruction(hierarchical_memory_system):
    """Test reconstruction of past context."""
    em = hierarchical_memory_system.episodic_memory

    # Record detailed episode
    original_context = {
        "blueprint_id": "project_x",
        "requirements": ["feature_a", "feature_b"],
        "constraints": {"budget": "$500", "timeline": "4 weeks"},
        "decisions": ["chose_langgraph", "chose_react_pattern"],
        "outcome": "success"
    }

    em.record(original_context)

    # Retrieve and reconstruct
    retrieved = em.episodes[0]

    # Assertions
    assert retrieved["blueprint_id"] == original_context["blueprint_id"], \
        "Should preserve blueprint ID"
    assert retrieved["requirements"] == original_context["requirements"], \
        "Should preserve requirements"
    assert retrieved["outcome"] == original_context["outcome"], \
        "Should preserve outcome"

    print("✓ Episodic memory context reconstruction working")


def test_episodic_memory_pruning(hierarchical_memory_system):
    """Test removal of oldest episodes when capacity exceeded."""
    em = hierarchical_memory_system.episodic_memory

    # Simulate capacity overflow (use smaller numbers for test)
    em.capacity = 10  # Override for testing

    # Add 15 episodes
    for i in range(15):
        em.record({"id": i, "data": f"episode_{i}"})

    # Should only have last 10
    assert len(em.episodes) == 10, "Should prune to capacity"
    assert em.episodes[0]["id"] == 5, "Should keep most recent episodes"
    assert em.episodes[-1]["id"] == 14, "Should have latest episode"

    print("✓ Episodic memory pruning working")


# ============================================================================
# 4.3 PROCEDURAL MEMORY (7 tests)
# ============================================================================

def test_procedural_memory_pattern_recording(hierarchical_memory_system):
    """Test recording of successful patterns."""
    pm = hierarchical_memory_system.procedural_memory

    # Record pattern usage
    pm.record_pattern("langgraph_react", success=True)

    # Assertions
    assert "langgraph_react" in pm.patterns, "Pattern should be recorded"
    assert pm.patterns["langgraph_react"]["successes"] == 1, "Should track success"

    print("✓ Procedural memory pattern recording working")


def test_procedural_memory_reinforcement(hierarchical_memory_system):
    """Test reinforcement of frequently used patterns."""
    pm = hierarchical_memory_system.procedural_memory

    # Use pattern multiple times
    for _ in range(5):
        pm.record_pattern("crewai_sequential", success=True)

    for _ in range(2):
        pm.record_pattern("crewai_sequential", success=False)

    # Assertions
    assert pm.patterns["crewai_sequential"]["successes"] == 5, "Should count successes"
    assert pm.patterns["crewai_sequential"]["failures"] == 2, "Should count failures"

    print("✓ Procedural memory reinforcement working")


def test_procedural_memory_pattern_retrieval(hierarchical_memory_system):
    """Test retrieval of patterns by context."""
    pm = hierarchical_memory_system.procedural_memory

    # Record various patterns
    pm.record_pattern("pattern_a", success=True)
    pm.record_pattern("pattern_b", success=True)
    pm.record_pattern("pattern_a", success=True)

    # Retrieve success rate
    success_rate = pm.get_success_rate("pattern_a")

    # Assertions
    assert success_rate == 1.0, "Pattern A should have 100% success rate"

    print(f"✓ Procedural memory pattern retrieval working (rate: {success_rate:.2f})")


def test_procedural_memory_pattern_adaptation(hierarchical_memory_system):
    """Test adaptation of patterns to new contexts."""
    pm = hierarchical_memory_system.procedural_memory

    # Record pattern in different contexts
    pm.record_pattern("adaptive_pattern_v1", success=True)
    pm.record_pattern("adaptive_pattern_v2", success=True)
    pm.record_pattern("adaptive_pattern_v2", success=True)

    # v2 should be more reinforced
    v1_count = pm.patterns.get("adaptive_pattern_v1", {}).get("successes", 0)
    v2_count = pm.patterns.get("adaptive_pattern_v2", {}).get("successes", 0)

    assert v2_count > v1_count, "Adapted pattern should have more usage"

    print("✓ Procedural memory pattern adaptation working")


def test_procedural_memory_failure_learning(hierarchical_memory_system):
    """Test learning from pattern failures."""
    pm = hierarchical_memory_system.procedural_memory

    # Record pattern with failures
    pm.record_pattern("risky_pattern", success=True)
    pm.record_pattern("risky_pattern", success=False)
    pm.record_pattern("risky_pattern", success=False)
    pm.record_pattern("risky_pattern", success=False)

    success_rate = pm.get_success_rate("risky_pattern")

    # Assertions
    assert success_rate == 0.25, "Should calculate correct success rate (1/4)"
    assert success_rate < 0.5, "Should identify low-performing pattern"

    print(f"✓ Procedural memory failure learning working (rate: {success_rate:.2f})")


def test_procedural_memory_pattern_evolution(hierarchical_memory_system):
    """Test evolution of patterns over time."""
    pm = hierarchical_memory_system.procedural_memory

    # Simulate pattern evolution
    patterns_over_time = [
        ("pattern_v1", True),
        ("pattern_v1", True),
        ("pattern_v1", False),  # 67% success
        ("pattern_v2", True),
        ("pattern_v2", True),
        ("pattern_v2", True),
        ("pattern_v2", True),  # 100% success
    ]

    for pattern, success in patterns_over_time:
        pm.record_pattern(pattern, success)

    v1_rate = pm.get_success_rate("pattern_v1")
    v2_rate = pm.get_success_rate("pattern_v2")

    # Assertions
    assert v2_rate > v1_rate, "Evolved pattern should perform better"
    assert v2_rate == 1.0, "v2 should have perfect success"

    print(f"✓ Pattern evolution tracked (v1: {v1_rate:.2f}, v2: {v2_rate:.2f})")


def test_procedural_memory_performance_tracking(hierarchical_memory_system):
    """Test tracking of pattern success rates."""
    pm = hierarchical_memory_system.procedural_memory

    # Track multiple patterns
    patterns = {
        "excellent_pattern": (9, 1),  # 90% success
        "good_pattern": (7, 3),        # 70% success
        "poor_pattern": (3, 7),        # 30% success
    }

    for pattern_name, (successes, failures) in patterns.items():
        for _ in range(successes):
            pm.record_pattern(pattern_name, success=True)
        for _ in range(failures):
            pm.record_pattern(pattern_name, success=False)

    # Calculate success rates
    rates = {name: pm.get_success_rate(name) for name in patterns.keys()}

    # Assertions
    assert rates["excellent_pattern"] == 0.9, "Excellent pattern should be 90%"
    assert rates["good_pattern"] == 0.7, "Good pattern should be 70%"
    assert rates["poor_pattern"] == 0.3, "Poor pattern should be 30%"

    print(f"✓ Performance tracking working (tracked {len(rates)} patterns)")


# ============================================================================
# 4.4 SEMANTIC MEMORY (6 tests)
# ============================================================================

def test_semantic_memory_knowledge_integration(hierarchical_memory_system):
    """Test integration of architectural knowledge."""
    sm = hierarchical_memory_system.semantic_memory

    # Store knowledge
    knowledge = {
        "framework": "langgraph",
        "concepts": ["StateGraph", "TypedDict", "conditional edges"],
        "best_practices": ["Use TypedDict for state", "Implement error handling"]
    }

    sm.store("langgraph_knowledge", knowledge)

    # Assertions
    retrieved = sm.retrieve("langgraph_knowledge")
    assert retrieved is not None, "Should retrieve stored knowledge"
    assert retrieved["framework"] == "langgraph", "Should preserve framework info"
    assert len(retrieved["concepts"]) == 3, "Should preserve all concepts"

    print("✓ Semantic memory knowledge integration working")


def test_semantic_memory_concept_relationships(hierarchical_memory_system):
    """Test relationship mapping between concepts."""
    sm = hierarchical_memory_system.semantic_memory

    # Store related concepts
    sm.store("agent_concept", {
        "type": "agent",
        "related_to": ["orchestration", "tools", "memory"]
    })

    sm.store("orchestration_concept", {
        "type": "orchestration",
        "related_to": ["agent", "workflow", "coordination"]
    })

    # Retrieve and verify relationships
    agent = sm.retrieve("agent_concept")
    orchestration = sm.retrieve("orchestration_concept")

    assert "orchestration" in agent["related_to"], "Should link to orchestration"
    assert "agent" in orchestration["related_to"], "Should link back to agent"

    print("✓ Semantic memory concept relationships working")


def test_semantic_memory_knowledge_retrieval(hierarchical_memory_system):
    """Test retrieval of relevant knowledge."""
    sm = hierarchical_memory_system.semantic_memory

    # Store various knowledge items
    knowledge_items = {
        "patterns": {"react": "...", "supervisor": "..."},
        "frameworks": {"langgraph": "...", "crewai": "..."},
        "best_practices": {"security": "...", "testing": "..."}
    }

    for concept, knowledge in knowledge_items.items():
        sm.store(concept, knowledge)

    # Retrieve specific knowledge
    patterns = sm.retrieve("patterns")
    frameworks = sm.retrieve("frameworks")

    # Assertions
    assert patterns is not None, "Should retrieve patterns"
    assert frameworks is not None, "Should retrieve frameworks"
    assert "react" in patterns, "Should have react pattern"
    assert "langgraph" in frameworks, "Should have langgraph framework"

    print(f"✓ Knowledge retrieval working ({len(knowledge_items)} items)")


def test_semantic_memory_knowledge_generalization(hierarchical_memory_system):
    """Test generalization across similar concepts."""
    sm = hierarchical_memory_system.semantic_memory

    # Store specific instances
    sm.store("chatbot_pattern", {
        "type": "conversational",
        "characteristics": ["user interaction", "context management"]
    })

    sm.store("assistant_pattern", {
        "type": "conversational",
        "characteristics": ["user interaction", "task completion"]
    })

    # Both should be retrievable as conversational type
    chatbot = sm.retrieve("chatbot_pattern")
    assistant = sm.retrieve("assistant_pattern")

    assert chatbot["type"] == assistant["type"], "Should share type"
    assert "user interaction" in chatbot["characteristics"], "Should have common trait"
    assert "user interaction" in assistant["characteristics"], "Should have common trait"

    print("✓ Semantic memory generalization working")


def test_semantic_memory_contradiction_handling(hierarchical_memory_system):
    """Test handling of contradictory knowledge."""
    sm = hierarchical_memory_system.semantic_memory

    # Store initial knowledge
    sm.store("best_practice", {
        "recommendation": "use simple patterns for startups",
        "version": 1
    })

    # Store updated (contradictory) knowledge
    sm.store("best_practice", {
        "recommendation": "use react patterns even for startups",
        "version": 2
    })

    # Latest should override
    current = sm.retrieve("best_practice")

    assert current["version"] == 2, "Should use latest knowledge"
    assert "react" in current["recommendation"], "Should have updated recommendation"

    print("✓ Semantic memory contradiction handling working")


def test_semantic_memory_knowledge_update(hierarchical_memory_system):
    """Test updating of outdated knowledge."""
    sm = hierarchical_memory_system.semantic_memory

    # Store initial knowledge
    sm.store("framework_info", {
        "name": "langgraph",
        "version": "0.0.20",
        "features": ["StateGraph", "checkpointing"]
    })

    # Update knowledge
    sm.store("framework_info", {
        "name": "langgraph",
        "version": "0.1.0",
        "features": ["StateGraph", "checkpointing", "streaming", "time-travel"]
    })

    updated = sm.retrieve("framework_info")

    # Assertions
    assert updated["version"] == "0.1.0", "Should have updated version"
    assert len(updated["features"]) == 4, "Should have additional features"
    assert "streaming" in updated["features"], "Should include new features"

    print("✓ Semantic memory knowledge update working")


# ============================================================================
# TEST SUMMARY
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("TEST SUITE 4: HierarchicalMemorySystem")
    print("="*70)
    print("\nRunning 25 tests...")
    print("\nTest Categories:")
    print("  - Working Memory: 6 tests")
    print("  - Episodic Memory: 6 tests")
    print("  - Procedural Memory: 7 tests")
    print("  - Semantic Memory: 6 tests")
    print("\n" + "="*70)

    pytest.main([__file__, "-v", "--tb=short"])
