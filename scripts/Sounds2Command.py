import json
import os
from pathlib import Path

class SoundsCommandGenerator:
    def __init__(self, soundsJsonPath):
        self.SoundsJsonPath = soundsJsonPath
        self.SoundNames = []
        
    def LoadSoundsJson(self):
        with open(self.SoundsJsonPath, 'r') as file:
            data = json.load(file)
            self.SoundNames = sorted(list(data.keys()))
            
    def GenerateCommand(self):
        command = ["command /memes [<string>]:", "    trigger:"]
        
        for sound in self.SoundNames:
            formattedLine = f'        send mini message from "∙ <white><u>{sound}</u></white>" to player'
            command.append(formattedLine)
            
        return "\n".join(command)
        
    def SaveToFile(self, outputPath):
        with open(outputPath, 'w', encoding='utf-8') as file:
            file.write(self.GenerateCommand())
            
    def Execute(self, outputPath):
        self.LoadSoundsJson()
        self.SaveToFile(outputPath)

def Main():
    soundsPath = Path("assets/memes/sounds.json")
    outputPath = Path("output/memes_command.sk")
    
    if not soundsPath.exists():
        print(f"Error: {soundsPath} not found")
        return
        
    outputPath.parent.mkdir(parents=True, exist_ok=True)
    
    generator = SoundsCommandGenerator(soundsPath)
    generator.Execute(outputPath)
    print(f"Generated Skript command at {outputPath}")

if __name__ == "__main__":
    Main()