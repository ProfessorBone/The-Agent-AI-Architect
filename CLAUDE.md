# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**The Agent AI Architect** is a production-ready system exclusively specialized for building sophisticated agentic AI systems and multi-agent architectures. This is NOT a general-purpose coding assistant - it focuses solely on AI agent development and orchestration.

**Status**: Production-ready (October 2025), Version 3.0+ with Revolutionary Dynamic Modular Architecture

**Key Innovation**: Dynamic modular architecture achieving 76-85% token reduction while preserving 100% functionality through context-aware module loading, hot-swapping, and SHA-256 integrity verification.

## Repository Structure

The repository contains two major components:

1. **System Prompts/** - Production-ready architect agents with modular architecture
2. **agentic-coder/** - Python implementation package with CLI interface

## Common Development Commands

### Agentic Coder (Python Package)

```bash
# Initial setup
cd agentic-coder
./scripts/dev_setup.sh

# Development with Poetry
poetry install                          # Install dependencies
poetry run agentic-coder --help        # View CLI commands
poetry run agentic-coder init my-project  # Initialize new project
poetry run agentic-coder chat          # Interactive chat mode
poetry run agentic-coder task "description"  # Run specific task

# Testing
poetry run pytest                      # Run all tests
poetry run pytest --cov=agentic_coder  # Run with coverage
poetry run pytest tests/unit/          # Unit tests only
poetry run pytest tests/integration/   # Integration tests only
poetry run pytest tests/e2e/           # End-to-end tests only

# Code quality
poetry run black .                     # Format code
poetry run isort .                     # Sort imports
poetry run flake8                      # Lint code
poetry run mypy src/                   # Type checking

# Services (with Docker)
docker-compose up -d neo4j chroma      # Start databases
docker-compose down                    # Stop services
docker-compose logs -f                 # View logs

# Database initialization
poetry run python scripts/init_databases.py

# Benchmarks
python scripts/benchmark.py --level basic
python scripts/benchmark.py --level intermediate
python scripts/benchmark.py --level advanced
```

### Configuration

- Primary config: `.env` file (copy from `.env.example`)
- YAML configs in `agentic-coder/config/`: default.yaml, development.yaml, production.yaml, models.yaml, tools.yaml
- Python 3.10+ required

## High-Level Architecture

### Multi-Agent Orchestration System

The system implements 7 specialized architect agents that work sequentially under orchestrator coordination:

1. **Orchestrator Architect** (01) - Master coordinator with 5 AI engines, 85% token reduction via modularization
2. **Analyzer Architect** (02) - Code structure and requirements analysis
3. **Prompt Engineer Architect** (03) - Revolutionary prompt optimization specialist, 76% token reduction, 39 tool integrations
4. **Planning Architect** (04) - Architecture design, 99/100 validation score, 38 integrated tools, 8 sample blueprints
5. **Coding Architect** (05) - Implementation code generation
6. **Testing Architect** (06) - Test creation and validation
7. **Reviewing Architect** (07) - Quality assurance and final validation

**Workflow Pattern**: Analyzer → Prompt Engineer → Planner → Coder → Tester → Reviewer (under Orchestrator coordination)

### Revolutionary Dynamic Modular Architecture (v3.0)

Each architect follows a consistent modular structure to achieve massive token reduction:

```
[Agent]/
├── [Agent]-System-Prompt.md          # Bootstrap core (300-400 lines, 85% smaller)
└── config/
    ├── revolutionary_core_logic.md    # 5 AI engines (REQUIRED)
    ├── security_policies.md           # Multi-layer security (REQUIRED, loaded first)
    ├── behavioral_governance.md       # Agent behavior (REQUIRED)
    ├── communication_framework.md     # Personality/voice (OPTIONAL)
    ├── [agent]_modes.yaml            # Operation modes (OPTIONAL)
    └── [agent]_tools.yaml            # Tool configurations (OPTIONAL)
```

**5 Revolutionary AI Engines** (present in each agent):
1. **MetaAnalysisEngine** - Self-improving capability analysis
2. **IterativeReasoningEngine** - Hypothesis-driven refinement with backtracking
3. **AutomatedEvaluationEngine** - Multi-metric assessment and A/B testing
4. **HierarchicalMemorySystem** - 4-tier memory (Working/Episodic/Semantic/Procedural)
5. **DefensiveSecurityEngine** - Adaptive threat response with 8-10 security layers

**Module Loading Order** (critical for correct operation):
1. security_policies.md (FIRST, non-overridable)
2. behavioral_governance.md (core logic)
3. revolutionary_core_logic.md (AI engines)
4. Operation modes (agent-specific)
5. Communication framework (personality)
6. Tool configurations

### Cognitive Architecture

**4-Tier Memory System**:
- **Working Memory**: 7-item capacity (Miller's law), 0.1 decay per cycle, active task context
- **Episodic Memory**: 10,000 episodes, temporal tagging, historical experiences
- **Semantic Memory**: 10,000+ items, conceptual relationships, factual knowledge
- **Procedural Memory**: Reinforcement-based learning, skills and procedures

**3 Reasoning Patterns**:
- **Reactive**: Fast pattern matching for immediate responses
- **Deliberative**: Systematic planning for complex tasks
- **Reflective**: Self-correction and learning from outcomes

### Knowledge Management: Graph RAG

**Neo4j Graph Database**:
- Nodes: Agents, tools, states, patterns, frameworks
- Relationships: Agent interactions, tool usage, state transitions, delegation patterns
- Purpose: Structural understanding of agent architectures and orchestration patterns

**ChromaDB Vector Database**:
- Embeddings: Code snippets, architecture descriptions, patterns
- Semantic search: Similarity-based pattern discovery
- Retrieval: Context-aware suggestions during blueprint generation

**Pattern Libraries**:
- LangGraph: ReAct, Supervisor-Worker, Hierarchical agents
- CrewAI: Sequential crews, hierarchical processes
- AutoGen: Conversational agents, group chat
- Hybrid: Multi-framework orchestration patterns

### Implementation Package Structure

**agentic-coder/** package organized by concern:

- **src/agentic_coder/agents/** - 6 agent implementations (orchestrator, analyzer, planner, coder, tester, reviewer)
- **src/agentic_coder/cognitive/** - Memory (4 tiers) + reasoning (3 types) + learning systems
- **src/agentic_coder/knowledge/** - Graph RAG (Neo4j), vector stores (ChromaDB), pattern libraries
- **src/agentic_coder/tools/** - File ops, code analysis, git, execution, web tools
- **src/agentic_coder/models/** - LLM management, model factory, prompt templates
- **src/agentic_coder/ui/** - CLI (Rich-formatted) + future API structure
- **tests/** - Unit, integration, e2e, benchmarks (AADB)
- **config/** - YAML configuration files by environment
- **scripts/** - Setup and utility scripts
- **docker/** - Containerization (standard + GPU images)

## Key Architectural Patterns

### Build-First, Then Modularize Methodology

This repository follows a deliberate 3-phase approach:

**Phase 1: Complete System Construction**
- Build fully functional monolithic system prompts first
- Test with real-world scenarios and establish baselines
- Ensures all capabilities and decision logic are complete

**Phase 2: Intelligent Modularization**
- Extract logical modules while preserving 100% functionality
- Implement dynamic loading with context-aware selection
- Add SHA-256 integrity verification and hot-swapping

**Phase 3: Enhanced Intelligence**
- Personal learning system (auto-adapts to user patterns)
- A/B testing for continuous improvement
- Enterprise features: compliance, audit trails, graceful degradation

**Benefits**: Guaranteed completeness, risk mitigation, easier testing, natural flow preservation, zero-risk deployment

### Context-Aware Module Loading

The system automatically adjusts module loading based on:
- **User expertise level** (detected from language patterns)
- **Task complexity** (analyzed from requirements)
- **Project type** (startup/research/enterprise)
- **Budget constraints** (token limits)
- **Success patterns** (learned from history)

**Example**: Startup projects load 7-10 tools (P0-P1), enterprise projects load 20-25 tools (P0-P2), maximum complexity loads 30-35 tools (P0-P3).

### Tool Integration Strategy

**Planning Architect Example** - 38 tools across 6 categories:
1. Blueprint Management & Registry (8 tools)
2. State Schema Automation (7 tools)
3. Orchestration & Framework Tools (9 tools)
4. Visual Planning & Documentation (6 tools)
5. Testing & Validation (5 tools)
6. Monitoring & Observability (3 tools)

**Tool Selection Validation**: 8/8 test scenarios passing (100% accuracy)

### Personal AI Architect System

Zero-configuration learning system that automatically:
- Detects expertise level from language patterns
- Adapts to complexity preferences from project history
- Learns communication style from interaction history
- Optimizes context budget from resource constraints
- Selects optimal modules from success patterns

No manual configuration required - system learns and adapts automatically.

## Important Cross-Component Relationships

### Data Flow Between Agents

```
User Input → Orchestrator (routing)
  ↓
Analyzer (requirements + code analysis)
  ↓
Prompt Engineer (instruction optimization)
  ↓
Planner (architecture blueprint with state schemas)
  ↓
Coder (implementation from blueprint)
  ↓
Tester (validation with test strategies from blueprint)
  ↓
Reviewer (final QA)
  ↓
Output
```

### Memory-Knowledge Integration

**Query Pattern**:
1. Fast lookup in episodic memory (Was this done before?)
2. Semantic search in vector store (Similar patterns?)
3. Graph traversal for relationships (How did agents interact?)
4. Procedural memory for best-performing approaches

**Learning Loop**: All agents feed effectiveness metrics back to Personal AI Architect, which adapts module selection and orchestration patterns.

### Analyzer → Planner Integration

- Analyzer extracts code patterns, dependencies, and requirements
- Results inform Planner's architecture decisions and framework selection
- Pattern recommendations guide blueprint generation with state schemas

### Planner → Coder → Tester Chain

- Planner generates comprehensive blueprint with:
  - State schemas (TypedDict/Pydantic models)
  - Node definitions (agent roles)
  - Edge definitions (transitions)
  - Tool selections (context-aware)
- Coder translates blueprint to implementation
- Tester uses blueprint's test strategy for validation

## Technology Stack (2025)

**Core**: Python 3.10+, Poetry, Docker
**LLM**: OpenAI GPT-4, Anthropic Claude, vLLM (local models)
**Frameworks**: LangChain, LangGraph, CrewAI, AutoGen
**Databases**: Neo4j (graph), ChromaDB (vectors), PostgreSQL (relational), Redis (cache)
**API**: FastAPI, Uvicorn, WebSockets
**CLI**: Typer, Rich (formatting)
**Testing**: Pytest, pytest-asyncio, pytest-cov
**Code Quality**: Black, isort, flake8, mypy, pre-commit
**Monitoring**: LangSmith (LLM tracing), Helicone (analytics), Weights & Biases (experiments)
**Analysis**: Tree-sitter, AST parsing
**Version Control**: GitPython

## Production Readiness & Validation

**Validation Scores**:
- Planning Architect: 99/100 (highest in system)
- Prompt Engineer: 95/100
- Sample Blueprints: 94.1/100 average (8 examples, ~8,700 lines)
- Tool Selection Tests: 8/8 passing (100%)

**Token Reduction Achievements**:
- Orchestrator: 85% reduction (2,245 → 341 lines)
- Prompt Engineer: 76% reduction (852 → 204 lines)
- 100% feature preservation across all modularization

**Enterprise Features**:
- SHA-256 integrity verification for all modules
- 10-layer security framework with compliance (GDPR, SOX, HIPAA)
- Fail-safe bootstrap with graceful degradation
- Real-time hot-swapping for underperforming modules
- Comprehensive audit trails and logging

## Development Notes

### When Working with System Prompts

1. **Always preserve modular structure** - Do not merge modules back into monolithic files
2. **Load security_policies.md first** - Non-negotiable, non-overridable security foundation
3. **Maintain module independence** - Each module should function standalone
4. **Test with modular system** - Use `System Prompts/test_modular_system.py` for validation
5. **Keep archives** - All monolithic versions preserved in `archive/` subdirectories

### When Working with agentic-coder Package

1. **Use Poetry** - Package management, dependencies, scripts
2. **Follow data models** - Pydantic models in `src/agentic_coder/data/models.py`
3. **Respect cognitive patterns** - 4-tier memory, 3 reasoning types
4. **Integrate with knowledge layer** - Use Graph RAG for pattern storage and retrieval
5. **CLI-first approach** - Rich formatting, user-friendly commands

### Testing Strategy

- **Unit tests**: Individual components in isolation
- **Integration tests**: Multi-component interactions (memory + reasoning, graph + vector search)
- **E2E tests**: Full agent workflows (orchestrator → reviewer chain)
- **Benchmarks**: Agentic AI Development Benchmark (AADB) in `tests/benchmarks/`

### Security Considerations

- Multi-layer security framework (10 layers in orchestrator, 8 in prompt engineer)
- Prompt injection defense at every agent entry point
- Content safety validation before LLM calls
- Audit logging for all sensitive operations
- SHA-256 verification for module integrity
- Compliance-ready (GDPR, SOX, HIPAA)

## Special Features

### Sample Blueprints (Planning Architect)

8 comprehensive reference implementations in `System Prompts/04-Planning-Architect/sample-blueprints/`:
1. LangGraph Startup MVP (e-commerce chatbot)
2. CrewAI Azure Enterprise (healthcare data pipeline)
3. AutoGen Research Team (academic literature review)
4. LangGraph Healthcare (patient care coordinator)
5. Hybrid Multi-Framework (financial analysis)
6. CrewAI Content Pipeline
7. LangGraph Customer Support
8. Enterprise Multi-Agent System

Each blueprint demonstrates:
- Framework-specific patterns
- State schema design (TypedDict + Pydantic)
- Tool selection rationale
- Testing strategies
- Deployment considerations

### Dynamic Module Hot-Swapping

Performance-based module replacement without service interruption:
1. Continuous effectiveness monitoring with exponential moving averages
2. Statistical significance testing (A/B tests)
3. Automatic module replacement when underperforming
4. Rollback capabilities if replacement degrades performance
5. Learning from successful replacements

### Comprehensive Documentation

- **agentic-ai-coding-system-design.md** - 530KB comprehensive system design (2,000+ lines)
- **System Prompts/** - 50+ markdown files with agent specifications
- **agentic-coder/docs/** - Architecture guides, API docs, user guides
- **agentic-coder/PROJECT_STRUCTURE.md** - 199-line detailed structure breakdown
- **README files** - In root and each major component directory

## Key Files to Understand

**System Design**:
- [agentic-ai-coding-system-design.md](agentic-ai-coding-system-design.md) - Complete architectural overview

**Agent Specifications**:
- [System Prompts/01-Orchestrator-Architect/01-Orchestrator-Architect-System-Prompt.md](System Prompts/01-Orchestrator-Architect/01-Orchestrator-Architect-System-Prompt.md)
- [System Prompts/03-Prompt-Engineer-Architect/03-Prompt-Engineer-Architect-System-Prompt.md](System Prompts/03-Prompt-Engineer-Architect/03-Prompt-Engineer-Architect-System-Prompt.md)
- [System Prompts/04-Planning-Architect/04-Planning-Architect-System-Prompt-v3.0-REVOLUTIONARY.md](System Prompts/04-Planning-Architect/04-Planning-Architect-System-Prompt-v3.0-REVOLUTIONARY.md)

**Implementation**:
- [agentic-coder/PROJECT_STRUCTURE.md](agentic-coder/PROJECT_STRUCTURE.md)
- [agentic-coder/pyproject.toml](agentic-coder/pyproject.toml)
- [agentic-coder/src/agentic_coder/__main__.py](agentic-coder/src/agentic_coder/__main__.py)

**Configuration**:
- [agentic-coder/config/default.yaml](agentic-coder/config/default.yaml)
- [agentic-coder/.env.example](agentic-coder/.env.example)

## Quantitative Summary

- **Total files**: 144+ relevant files (Python, Markdown, YAML, JSON)
- **System prompts**: 7 architects, 21 core files, 50+ configs
- **Documentation**: 10,000+ lines across 50+ markdown files
- **Code**: ~30 Python modules, comprehensive test coverage
- **Sample blueprints**: 8 production-ready examples (~8,700 lines, 94.1/100 avg)
- **Tool integrations**: 38-39 per architect
- **Memory tiers**: 4 (Working/Episodic/Semantic/Procedural)
- **Reasoning patterns**: 3 (Reactive/Deliberative/Reflective)
- **AI engines**: 5 per agent (Meta/Iterative/Automated/Memory/Security)

---

**Last Updated**: October 2025 (Production-ready v3.0 with Dynamic Modular Architecture)
