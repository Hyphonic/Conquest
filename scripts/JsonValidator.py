import json
import argparse
from pathlib import Path
from typing import Tuple
from rich.console import Console
from rich.theme import Theme

def ValidateJson(FilePath: str) -> Tuple[bool, str]:
    """Validate JSON file for syntax and basic structure
    
    Args:
        FilePath (str): Path to JSON file
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    try:
        path = Path(FilePath)
        
        # Check if file exists
        if not path.exists():
            return False, f"File not found: {FilePath}"
            
        # Try to read and parse JSON
        with open(FilePath, 'r', encoding='utf-8') as File:
            json.load(File)
            
        return True, "JSON is valid"
        
    except json.JSONDecodeError as Error:
        return False, f"Invalid JSON: {str(Error)}"
    except Exception as Error:
        return False, f"Error validating JSON: {str(Error)}"

def Main():
    Parser = argparse.ArgumentParser(description='Validate JSON files')
    Parser.add_argument('file', help='Path to JSON file to validate')
    
    Args = Parser.parse_args()
    IsValid, Message = ValidateJson(Args.file)
    
    # Initialize rich console
    console = Console(theme=Theme({
        "valid": "green",
        "invalid": "red"
    }))
    
    # Print result with rich formatting
    Style = "valid" if IsValid else "invalid"
    console.print(Message, style=Style)
    
    # Set exit code based on validation result
    exit(0 if IsValid else 1)

if __name__ == "__main__":
    Main()