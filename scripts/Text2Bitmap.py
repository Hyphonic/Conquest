from rich.console import Console
from rich.style import Style
import argparse
import sys

ZeroWidthCharacter = "󏿿"

# Each row has 28 characters total:
# [0] is the "space" glyph,
# [1..26] are glyphs for A..Z,
# [27] is another "space" glyph.
# These three rows correspond to Red, Blue, and Green, in that order.
BitmapRows = [
    "",
    "",
    ""
]

ColorMapping = {
    "Red": 0,
    "Blue": 1,
    "Green": 2
}

def TextToBitmap(InputText: str, ColorChoice: str, Space: bool) -> str:
    """
    Converts each character in InputText to the glyph from the selected color row:
    - Space => index 0
    - Letters => 'A'..'Z' => indices 1..26
    Returns the concatenated glyphs, separated by the zero width character.
    """
    if ColorChoice.title() not in ColorMapping:
        sys.exit("Invalid color choice. Use Red, Blue, or Green.")

    SelectedRow = BitmapRows[ColorMapping[ColorChoice.title()]]
    BitmapList = []

    for Character in InputText:
        if Character == ' ':
            Index = 0
        elif Character.isalpha():
            Index = ord(Character.upper()) - ord('A') + 1
            if Index < 1 or Index > 26:
                sys.exit(f"Character out of range: {Character}")
        else:
            sys.exit(f"Invalid character: {Character}")

        try:
            Glyph = SelectedRow[Index]
        except IndexError:
            sys.exit("Index out of range in the bitmap rows.")
        BitmapList.append(Glyph)

    BitmapList.insert(0, SelectedRow[0]) if Space else None
    BitmapList.append(SelectedRow[len(SelectedRow)-1]) if Space else None
    InputTextVisual = f" {InputText.upper()} " if Space else InputText.upper()

    console = Console()
    console.print(InputTextVisual, style=Style(bgcolor=ColorChoice.title().lower()))

    console.print(ZeroWidthCharacter.join(BitmapList))

if __name__ == "__main__":
    Parser = argparse.ArgumentParser(description="Convert text to a bitmap.")
    Parser.add_argument("--text", help="The text to convert.", required=True, default="Hello, World")
    Parser.add_argument("--color", help="The color to use: Red, Blue, or Green.", default="Red")
    Parser.add_argument("--space", help="Add an extra space to the beginning and end of the text.", type=lambda x: (str(x).lower() == 'true'), default=False)
    Args = Parser.parse_args()
    TextToBitmap(Args.text, Args.color, Args.space)