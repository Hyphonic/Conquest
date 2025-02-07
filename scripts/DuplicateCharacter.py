import json
import argparse
import os
from collections import defaultdict
from typing import Dict, List
from rich.console import Console
from rich.table import Table

def LoadBitmapCharsFromFile(FilePath: str, CharLocations: Dict[str, List[str]]) -> None:
    """Load characters from a single font JSON file and track their bitmap sources
    
    Args:
        FilePath (str): Path to font JSON file
        CharLocations (Dict[str, List[str]]): Dictionary to update with characters and their locations
    """
    try:
        with open(FilePath, 'r', encoding='utf-8') as File:
            Data = json.load(File)
            
            for Provider in Data.get('providers', []):
                if Provider.get('type') == 'bitmap':
                    BitmapFile = Provider.get('file', '')
                    for CharList in Provider.get('chars', []):
                        for Char in CharList:
                            if Char:  # Skip empty characters
                                CharLocations[Char].append(f"{FilePath}: {BitmapFile}")
    except json.JSONDecodeError:
        print(f"[red]Error: Invalid JSON file: {FilePath}[/red]")
    except Exception as Error:
        print(f"[red]Error processing {FilePath}: {str(Error)}[/red]")

def LoadBitmapChars(DirectoryPath: str) -> Dict[str, List[str]]:
    """Recursively load characters from all JSON files in directory
    
    Args:
        DirectoryPath (str): Root directory path to search for JSON files
        
    Returns:
        Dict[str, List[str]]: Dictionary of characters and their bitmap sources
    """
    CharLocations = defaultdict(list)
    
    for Root, _, Files in os.walk(DirectoryPath):
        for File in Files:
            if File.endswith('.json'):
                FilePath = os.path.join(Root, File)
                LoadBitmapCharsFromFile(FilePath, CharLocations)
    
    return CharLocations

def FindDuplicates(CharLocations: Dict[str, List[str]]) -> None:
    """Find and display duplicate characters
    
    Args:
        CharLocations (Dict[str, List[str]]): Dictionary of characters and their locations
    """
    console = Console()
    table = Table(title="Duplicate Characters")
    table.add_column("Character", style="cyan")
    table.add_column("Unicode", style="magenta")
    table.add_column("Occurrences", style="green")
    table.add_column("Locations", style="yellow")
    
    HasDuplicates = False
    
    for Char, Locations in CharLocations.items():
        if len(Locations) > 1:
            HasDuplicates = True
            table.add_row(
                Char,
                f"U+{ord(Char):04X}",
                str(len(Locations)),
                "\n".join(Locations)
            )
    
    if HasDuplicates:
        console.print(table)
    else:
        console.print("[green]No duplicate characters found[/green]")

def Main():
    Parser = argparse.ArgumentParser(description='Find duplicate characters in Minecraft font files')
    Parser.add_argument('directory', help='Directory path containing JSON font files')
    
    Args = Parser.parse_args()
    CharLocations = LoadBitmapChars(Args.directory)
    FindDuplicates(CharLocations)

if __name__ == "__main__":
    Main()