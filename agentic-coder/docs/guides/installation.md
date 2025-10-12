# Installation Guide

## Prerequisites

Before installing Agentic Coder, ensure you have the following prerequisites:

### System Requirements
- Python 3.10 or higher
- Git
- At least 8GB RAM (16GB recommended)
- 10GB free disk space

### External Services
- Neo4j database (optional, can use embedded)
- ChromaDB (embedded by default)
- OpenAI API key or local LLM setup

## Installation Methods

### Method 1: Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/agentic-coder.git
cd agentic-coder

# Install Poetry if not already installed
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Activate the virtual environment
poetry shell
```

### Method 2: Using pip

```bash
# Clone the repository
git clone https://github.com/yourusername/agentic-coder.git
cd agentic-coder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

### Method 3: Using Docker

```bash
# Clone the repository
git clone https://github.com/yourusername/agentic-coder.git
cd agentic-coder

# Build and run with Docker Compose
docker-compose up -d
```

## Configuration

### 1. Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit the configuration
nano .env
```

### 2. Database Setup

#### Neo4j Setup
```bash
# Using Docker
docker run -d \
  --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/your_password \
  neo4j:latest

# Or install locally
# Follow Neo4j installation guide for your OS
```

### 3. Initialize the System

```bash
# Run the setup script
./scripts/dev_setup.sh

# Initialize databases
python scripts/init_databases.py

# Load initial knowledge base
python scripts/load_knowledge.py
```

## Verification

Test your installation:

```bash
# Check the CLI
agentic-coder --help

# Run a simple test
agentic-coder system status

# Run the test suite
pytest tests/unit/
```

## Next Steps

1. Follow the [Quick Start Guide](quick-start.md)
2. Read the [Configuration Guide](configuration.md)
3. Explore the [Tutorials](../tutorials/)

## Troubleshooting

See the [Troubleshooting Guide](troubleshooting.md) for common issues and solutions.