import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
from math import ceil, sqrt

def LoadFontChars(FontPath: str) -> set[str]:
    """Load characters from font JSON file and return used chars"""
    with open(FontPath, 'r', encoding='utf-8') as File:
        Data = json.load(File)
        UsedChars = set()
        for Provider in Data.get('providers', []):
            if Provider.get('type') == 'bitmap':
                for CharList in Provider.get('chars', []):
                    UsedChars.update(set(CharList))
        return UsedChars

def CreateVisualGrid(UsedChars: set[str], MinCode: int, MaxCode: int) -> None:
    """Create visual grid representation of character usage"""
    TotalChars = MaxCode - MinCode + 1
    GridSize = ceil(sqrt(TotalChars))
    
    # Create grid data
    Grid = np.zeros((GridSize, GridSize))
    for i in range(TotalChars):
        Row = i // GridSize
        Col = i % GridSize
        Char = chr(MinCode + i)
        Grid[Row, Col] = 1 if Char in UsedChars else 0
    
    # Create visualization with sharp pixels
    plt.figure(figsize=(10, 10))
    plt.imshow(Grid, cmap='RdYlGn', interpolation='nearest')  # Turn off interpolation
    plt.title(f'Character Usage Map ({len(UsedChars)}/{TotalChars} used)')
    plt.grid(True, antialiased=False)  # Turn off grid anti-aliasing
    plt.savefig('char_usage.png', dpi=100, bbox_inches='tight')
    plt.close()

def VisualizeUsage(UsedChars: set[str]):
    """Print character usage statistics and create visual grid"""
    if not UsedChars:
        print("No characters found in font file")
        return
    
    CharCodes = [ord(c) for c in UsedChars]
    MinCode = min(CharCodes)
    MaxCode = max(CharCodes)
    
    TotalAvailable = MaxCode - MinCode + 1
    TotalUsed = len(UsedChars)
    UsagePercentage = (TotalUsed / TotalAvailable) * 100
    
    print(f"Character Range: {hex(MinCode)} to {hex(MaxCode)}")
    print(f"Total Available: {TotalAvailable}")
    print(f"Total Used: {TotalUsed}")
    print(f"Usage: {UsagePercentage:.2f}%")
    
    CreateVisualGrid(UsedChars, MinCode, MaxCode)
    print("Visual grid saved as 'char_usage.png'")

def Main():
    Parser = argparse.ArgumentParser(description='Visualize font character usage')
    Parser.add_argument('font', help='Path to font JSON file')
    
    Args = Parser.parse_args()
    UsedChars = LoadFontChars(Args.font)
    VisualizeUsage(UsedChars)

if __name__ == "__main__":
    Main()