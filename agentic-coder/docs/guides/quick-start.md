# Quick Start Guide

Get up and running with Agentic Coder in just a few minutes!

## Prerequisites

- Python 3.10 or higher
- Git
- 8GB RAM minimum (16GB recommended)

## Installation

### Option 1: Using Poetry (Recommended)

```bash
git clone https://github.com/yourusername/agentic-coder.git
cd agentic-coder
poetry install
poetry shell
```

### Option 2: Using pip

```bash
git clone https://github.com/yourusername/agentic-coder.git
cd agentic-coder
pip install -e .
```

## Configuration

1. Copy the environment template:
```bash
cp .env.example .env
```

2. Edit `.env` with your settings:
```bash
# Required: OpenAI API key
OPENAI_API_KEY=your_api_key_here

# Optional: Local model configuration
VLLM_API_BASE=http://localhost:8000
```

## First Steps

### 1. Initialize the System

```bash
agentic-coder init my-project
cd my-project
```

### 2. Start Interactive Chat

```bash
agentic-coder chat
```

### 3. Run a Simple Task

```bash
agentic-coder task "Create a Python function to calculate fibonacci numbers"
```

## What's Next?

- Read the [Architecture Guide](../architecture/system-overview.md)
- Try the [First Agent Tutorial](../tutorials/first-agent.md)
- Explore [Examples](../../examples/)
- Check out [Configuration Options](configuration.md)