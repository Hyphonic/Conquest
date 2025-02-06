from rich.console import Console
import json
import os
import argparse
from pathlib import Path
from typing import List


LOG_LEVEL = 0  # 0: Debug, 1: Info, 2: Warning, 3: Error, 4: Critical

class RichLogger:
    def __init__(self, Name=__name__):
        self.Console = Console(
            markup=True,
            log_time=False,
            force_terminal=True,
            width=140,
            log_path=False
        )
    
    LogLevels = {
        'DEBUG': 1,
        'INFO': 2,
        'WARNING': 3,
        'ERROR': 4,
        'CRITICAL': 5
    }

    def Debug(self, Message):
        if LOG_LEVEL <= self.LogLevels['DEBUG']:
            self.Console.log(f'[bold blue]DEBUG:   [/bold blue] {Message}')

    def Info(self, Message):
        if LOG_LEVEL <= self.LogLevels['INFO']:
            self.Console.log(f'[bold green]INFO:    [/bold green] {Message}')

    def Warning(self, Message):
        if LOG_LEVEL <= self.LogLevels['WARNING']:
            self.Console.log(f'[bold yellow]WARNING: [/bold yellow] {Message}')

    def Error(self, Message):
        if LOG_LEVEL <= self.LogLevels['ERROR']:
            self.Console.log(f'[bold red]ERROR:   [/bold red] {Message}')

    def Critical(self, Message):
        if LOG_LEVEL <= self.LogLevels['CRITICAL']:
            self.Console.log(f'[bold magenta]CRITICAL:[/bold magenta] {Message}')

Logger = RichLogger(__name__)

class UnusedCharacterFinder:
    def __init__(self, AssetsPath: str, Count: int):
        self.AssetsPath = AssetsPath
        self.Count = Count
        self.UsedChars = set()
        
    def FindFontDirectories(self) -> List[Path]:
        Logger.Debug(f"Searching for font directories in {self.AssetsPath}")
        FontDirs = []
        for Root, Dirs, _ in os.walk(self.AssetsPath):
            if "font" in Dirs:
                FontPath = Path(Root) / "font"
                if (FontPath / "default.json").exists():
                    Logger.Debug(f"Found font directory: {FontPath}")
                    FontDirs.append(FontPath)
        return FontDirs

    def ExtractCharsFromJson(self, JsonFile: Path) -> None:
        Logger.Debug(f"Reading characters from {JsonFile}")
        try:
            with open(JsonFile, 'r', encoding='utf-8') as File:
                Data = json.load(File)
                if 'providers' in Data:
                    for Provider in Data['providers']:
                        if 'chars' in Provider:
                            self.UsedChars.update(Provider['chars'])
        except Exception as Error:
            Logger.Error(f"Error reading {JsonFile}: {str(Error)}")

    def GenerateUnusedChars(self) -> List[str]:
        Logger.Debug("Generating unused characters")
        StartCode = 0xE000  # Private Use Area
        UnusedChars = []
        CurrentCode = StartCode
        
        while len(UnusedChars) < self.Count:
            Char = chr(CurrentCode)
            if Char not in self.UsedChars:
                UnusedChars.append(Char)
            CurrentCode += 1
        
        return UnusedChars

    def Execute(self) -> List[str]:
        Logger.Info(f"Starting search in {self.AssetsPath}")
        FontDirs = self.FindFontDirectories()
        Logger.Info(f"Found {len(FontDirs)} font directories")

        for FontDir in FontDirs:
            JsonFile = FontDir / "default.json"
            self.ExtractCharsFromJson(JsonFile)

        Logger.Info(f"Total unique characters found: {len(self.UsedChars)}")
        return self.GenerateUnusedChars()

def Main():
    Parser = argparse.ArgumentParser(description='Find unused characters for bitmap fonts')
    Parser.add_argument('AssetsPath', help='Path to assets directory')
    Parser.add_argument('Count', type=int, help='Number of characters needed')
    Args = Parser.parse_args()

    Finder = UnusedCharacterFinder(Args.AssetsPath, Args.Count)
    UnusedChars = Finder.Execute()
    
    Logger.Info("Unused characters (copy these):")
    for Char in UnusedChars:
        Logger.Info(f"'{Char}'")

if __name__ == "__main__":
    Main()