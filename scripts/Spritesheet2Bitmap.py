import json
import argparse
from pathlib import Path

def ValidateChar(value: str) -> str:
    """Validate that input is a single character"""
    if len(value) != 1:
        raise argparse.ArgumentTypeError(f"'{value}' must be a single character")
    return value

def GenerateCharacterGrid(Width: int, Height: int, StartChar: str) -> list[str]:
    """Generate a grid of characters with specified width and height"""
    StartCode = ord(StartChar)
    AllChars = [chr(StartCode + i) for i in range(Width * Height)]
    
    # Split into rows and join characters
    Grid = []
    for Row in range(Height):
        Start = Row * Width
        End = Start + Width
        RowChars = AllChars[Start:End]
        
        # Fill remaining space with empty strings if needed
        while len(RowChars) < Width:
            RowChars.append("")
            
        # Join characters into single string
        Grid.append("".join(RowChars))
    
    return Grid

def GenerateBitmapJson(TexturePath: str, Height: int, Width: int, Rows: int, StartChar: str) -> dict:
    """Generate bitmap font JSON structure"""
    return {
        "type": "bitmap",
        "file": f"font/{Path(TexturePath).name}",
        "height": Height,
        "ascent": Height - 1,
        "chars": GenerateCharacterGrid(Width, Rows, StartChar)
    }

def Main():
    Parser = argparse.ArgumentParser(description='Generate Minecraft bitmap font JSON')
    Parser.add_argument('texture', help='Texture filename (e.g. emojis.png)')
    Parser.add_argument('height', type=int, help='Character height in pixels')
    Parser.add_argument('width', type=int, help='Number of characters per row')
    Parser.add_argument('rows', type=int, help='Number of rows')
    Parser.add_argument('--start', type=ValidateChar, default='', 
                       help='Starting character (must be single character)')
    
    Args = Parser.parse_args()
    JsonData = GenerateBitmapJson(Args.texture, Args.height, Args.width, Args.rows, Args.start)
    
    # Ensure JSON encoder uses actual characters
    print(json.dumps(JsonData, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    Main()

# Example usage:
# python Spritesheet2Bitmap.py emojis.png 9 8 4 --start "Ḁ"