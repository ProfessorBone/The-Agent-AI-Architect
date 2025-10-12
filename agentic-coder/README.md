# Agentic Coder

A comprehensive agentic AI coding system featuring multi-agent orchestration, cognitive architecture, and Graph RAG knowledge management.

## 🚀 Features

- **Multi-Agent System**: Orchestrator, Analyzer, Planner, Coder, Tester, and Reviewer agents
- **Cognitive Architecture**: Working, episodic, semantic, and procedural memory systems
- **Graph RAG**: Neo4j-based knowledge graphs with vector embeddings
- **Advanced Reasoning**: Reactive, deliberative, and reflective reasoning patterns
- **Tool Ecosystem**: Comprehensive tools for file operations, code analysis, Git, and execution
- **Learning Systems**: Experience replay, meta-learning, and curriculum learning
- **Modern UI**: CLI with Rich formatting and future API support

## 🏗️ Architecture

### Agent Types
- **Orchestrator**: Coordinates multi-agent workflows
- **Analyzer**: Analyzes code structure and patterns
- **Planner**: Creates execution plans and strategies
- **Coder**: Generates and modifies code
- **Tester**: Creates and runs tests
- **Reviewer**: Reviews code quality and adherence

### Memory Systems
- **Working Memory**: Short-term context and active information
- **Episodic Memory**: Historical experiences and interactions
- **Semantic Memory**: Factual knowledge and concepts
- **Procedural Memory**: Skills and procedures

### Knowledge Layer
- **Graph RAG**: Structured knowledge in Neo4j
- **Vector Stores**: Embeddings in ChromaDB
- **Pattern Libraries**: Reusable patterns for LangGraph, CrewAI, AutoGen

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/agentic-coder.git
cd agentic-coder

# Install with Poetry
poetry install

# Or with pip
pip install -e .
```

## 🚀 Quick Start

```bash
# Initialize a new project
agentic-coder init my-project

# Start interactive chat
agentic-coder chat

# Run a specific task
agentic-coder task "Create a FastAPI application with user authentication"

# Start system monitoring
agentic-coder system status
```

## 📖 Documentation

- [Architecture Overview](docs/architecture/system-overview.md)
- [Installation Guide](docs/guides/installation.md)
- [Quick Start Tutorial](docs/guides/quick-start.md)
- [API Reference](docs/api/)

## 🧪 Testing

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=agentic_coder

# Run specific test categories
poetry run pytest tests/unit/
poetry run pytest tests/integration/
poetry run pytest tests/e2e/
```

## 🏗️ Development

```bash
# Setup development environment
./scripts/dev_setup.sh

# Start services
./scripts/start_servers.py

# Load initial knowledge
./scripts/load_knowledge.py
```

## 📊 Benchmarks

The project includes the Agentic AI Development Benchmark (AADB):

```bash
# Run benchmarks
python scripts/benchmark.py --level basic
python scripts/benchmark.py --level intermediate
python scripts/benchmark.py --level advanced
```

## 🤝 Contributing

Please read [CONTRIBUTING.md](docs/development/contributing.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- LangChain & LangGraph for agent frameworks
- Neo4j for graph database technology
- ChromaDB for vector storage
- OpenAI for language models
- The open-source AI community