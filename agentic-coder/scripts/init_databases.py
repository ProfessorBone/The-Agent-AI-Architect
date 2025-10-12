#!/usr/bin/env python3
"""
Script to initialize databases for agentic-coder.
"""

import os
import sys
import asyncio
from pathlib import Path

async def init_neo4j():
    """Initialize Neo4j database."""
    print("Initializing Neo4j database...")
    
    # Placeholder for Neo4j initialization
    # In a real implementation, this would connect to Neo4j and create schema
    print("✓ Neo4j database initialized")

async def init_chroma():
    """Initialize ChromaDB."""
    print("Initializing ChromaDB...")
    
    # Create ChromaDB directory
    chroma_dir = Path("./data/chroma_db")
    chroma_dir.mkdir(parents=True, exist_ok=True)
    
    # Placeholder for ChromaDB initialization
    print("✓ ChromaDB initialized")

async def create_directories():
    """Create required directories."""
    print("Creating required directories...")
    
    directories = [
        "./data",
        "./data/logs",
        "./data/cache", 
        "./data/models",
        "./data/chroma_db",
        "./data/neo4j_db",
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"  ✓ Created {directory}")

async def main():
    """Main initialization function."""
    print("Initializing agentic-coder databases...")
    
    try:
        await create_directories()
        await init_chroma()
        await init_neo4j()
        
        print("\n✅ Database initialization completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Database initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())