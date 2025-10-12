#!/bin/bash
# Development environment setup script for agentic-coder

set -e

echo "🚀 Setting up agentic-coder development environment..."

# Check if Python 3.10+ is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "📌 Using Python $PYTHON_VERSION"

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "📦 Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "✓ Poetry is already installed"
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
poetry install

# Copy environment file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your configuration"
fi

# Initialize databases
echo "🗄️ Initializing databases..."
poetry run python scripts/init_databases.py

# Install pre-commit hooks
echo "🔧 Installing pre-commit hooks..."
poetry run pre-commit install

# Check if Docker is available for services
if command -v docker &> /dev/null; then
    echo "🐳 Docker is available for running services"
    
    # Ask if user wants to start services
    read -p "Start Neo4j and ChromaDB with Docker? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🚀 Starting services with Docker Compose..."
        docker-compose up -d neo4j chroma
    fi
else
    echo "⚠️  Docker not found. You'll need to install Neo4j and ChromaDB manually."
fi

echo
echo "✅ Development environment setup completed!"
echo
echo "Next steps:"
echo "1. Edit .env file with your configuration"
echo "2. Ensure Neo4j and ChromaDB are running"
echo "3. Run tests: poetry run pytest"
echo "4. Start CLI: poetry run agentic-coder --help"
echo
echo "Happy coding! 🎉"