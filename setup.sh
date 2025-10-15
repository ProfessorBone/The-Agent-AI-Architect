#!/bin/bash

# The Agent AI Architect - Environment Setup Script
# Version: 1.1
# Date: October 15, 2025

echo "🚀 Setting up The Agent AI Architect development environment..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3.10+ and try again."
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
echo "✅ Found Python $python_version"

# Check if Poetry is installed for the agentic-coder subproject
if command -v poetry &> /dev/null; then
    echo "✅ Poetry found - can manage agentic-coder subproject"
    POETRY_AVAILABLE=true
else
    echo "⚠️  Poetry not found - will install pip-based dependencies only"
    echo "   To use the agentic-coder subproject, install Poetry: curl -sSL https://install.python-poetry.org | python3 -"
    POETRY_AVAILABLE=false
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install core dependencies
echo "📚 Installing core dependencies..."
pip install langchain langchain-community langchain-core langchain-openai
pip install openai anthropic
pip install python-dotenv pyyaml pydantic
pip install requests beautifulsoup4

echo "✅ Core dependencies installed"

# Install development dependencies
echo "🛠️  Installing development dependencies..."
pip install pytest black flake8 jupyter

echo "✅ Development dependencies installed"

# Install additional agent libraries
echo "🤖 Installing agent framework libraries..."
pip install crewai || echo "⚠️  CrewAI installation failed - may need manual installation"
pip install langgraph || echo "⚠️  LangGraph installation failed - may need manual installation"

# Setup agentic-coder subproject if Poetry is available
if [ "$POETRY_AVAILABLE" = true ] && [ -d "agentic-coder" ]; then
    echo "🔧 Setting up agentic-coder subproject..."
    cd agentic-coder
    
    # Install dependencies with Poetry
    poetry install
    echo "✅ agentic-coder dependencies installed with Poetry"
    
    # Return to main directory
    cd ..
else
    echo "⚠️  Skipping agentic-coder setup (Poetry not available or directory not found)"
fi

# Create .env template if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env template..."
    cat > .env << EOF
# API Keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

# LangSmith (Optional)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=agent-ai-architect

# Environment
ENVIRONMENT=development
DEBUG=true
EOF
    echo "✅ .env template created - please add your API keys"
else
    echo "✅ .env file already exists"
fi

echo ""
echo "🎉 Environment setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Add your API keys to the .env file"
echo "2. Activate the environment: source venv/bin/activate"
if [ "$POETRY_AVAILABLE" = true ] && [ -d "agentic-coder" ]; then
    echo "3. For agentic-coder development: cd agentic-coder && poetry shell"
fi
echo "4. Start developing with The Agent AI Architect!"
echo ""
echo "💡 To activate the environment in future sessions:"
echo "   cd '/Users/faheem/The Agent AI Architect'"
echo "   source venv/bin/activate"
if [ "$POETRY_AVAILABLE" = true ] && [ -d "agentic-coder" ]; then
    echo ""
    echo "💡 For agentic-coder subproject:"
    echo "   cd '/Users/faheem/The Agent AI Architect/agentic-coder'"
    echo "   poetry shell"
fi
echo ""