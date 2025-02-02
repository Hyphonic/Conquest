import json
import argparse
from collections import defaultdict
from typing import Dict, List
from rich.console import Console
from rich.table import Table

def LoadBitmapChars(FontPath: str) -> Dict[str, List[str]]:
    """Load characters from font JSON file and track their bitmap sources
    
    Args:
        FontPath (str): Path to font JSON file
        
    Returns:
        Dict[str, List[str]]: Dictionary of characters and their bitmap sources
    """
    CharLocations = defaultdict(list)
    
    with open(FontPath, 'r', encoding='utf-8') as File:
        Data = json.load(File)
        
        for Provider in Data.get('providers', []):
            if Provider.get('type') == 'bitmap':
                BitmapFile = Provider.get('file', '')
                for CharList in Provider.get('chars', []):
                    for Char in CharList:
                        if Char:  # Skip empty characters
                            CharLocations[Char].append(BitmapFile)
    
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
    Parser = argparse.ArgumentParser(description='Find duplicate characters in Minecraft font')
    Parser.add_argument('font', help='Path to default.json')
    
    Args = Parser.parse_args()
    CharLocations = LoadBitmapChars(Args.font)
    FindDuplicates(CharLocations)

if __name__ == "__main__":
    Main()