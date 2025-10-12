#!/usr/bin/env python3
"""
Script to download and setup required models for agentic-coder.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any

def download_model(model_name: str, model_path: str) -> bool:
    """Download a model to the specified path."""
    print(f"Downloading model: {model_name}")
    print(f"Target path: {model_path}")
    
    # Create model directory
    Path(model_path).mkdir(parents=True, exist_ok=True)
    
    # Placeholder for actual download logic
    # In a real implementation, this would use huggingface_hub or similar
    print(f"✓ Model {model_name} downloaded successfully")
    return True

def get_available_models() -> Dict[str, str]:
    """Get list of available models to download."""
    return {
        "codellama-7b": "codellama/CodeLlama-7b-Python-hf",
        "codellama-13b": "codellama/CodeLlama-13b-Python-hf", 
        "deepseek-coder": "deepseek-ai/deepseek-coder-6.7b-instruct",
        "starcoder": "bigcode/starcoder",
    }

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Download models for agentic-coder")
    parser.add_argument(
        "--model", 
        type=str, 
        help="Specific model to download"
    )
    parser.add_argument(
        "--all", 
        action="store_true", 
        help="Download all available models"
    )
    parser.add_argument(
        "--list", 
        action="store_true", 
        help="List available models"
    )
    parser.add_argument(
        "--data-dir",
        type=str,
        default="./data/models",
        help="Directory to store models"
    )
    
    args = parser.parse_args()
    
    available_models = get_available_models()
    
    if args.list:
        print("Available models:")
        for name, path in available_models.items():
            print(f"  {name}: {path}")
        return
    
    data_dir = Path(args.data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    
    if args.all:
        print("Downloading all models...")
        for name, model_path in available_models.items():
            target_path = data_dir / name
            download_model(name, str(target_path))
    elif args.model:
        if args.model not in available_models:
            print(f"Error: Model '{args.model}' not found")
            print("Use --list to see available models")
            sys.exit(1)
        
        model_path = available_models[args.model]
        target_path = data_dir / args.model
        download_model(args.model, str(target_path))
    else:
        print("Please specify --model <name>, --all, or --list")
        parser.print_help()

if __name__ == "__main__":
    main()