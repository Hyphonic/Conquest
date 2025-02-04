import os
import json
import sys

class SoundFileGenerator:
    def __init__(self, folderPath):
        self.FolderPath = folderPath
        self.SoundsData = {}
        
    def ValidatePath(self):
        if not os.path.exists(self.FolderPath):
            raise FileNotFoundError(f"Folder '{self.FolderPath}' does not exist")
            
    def GenerateJsonStructure(self):
        FolderName = os.path.basename(self.FolderPath)
        
        for File in os.listdir(self.FolderPath):
            if os.path.isdir(os.path.join(self.FolderPath, File)):
                continue
                
            FilenameNoExt = os.path.splitext(File)[0]
            self.SoundsData[FilenameNoExt] = {
                "sounds": [
                    f"{FolderName}/{FilenameNoExt}"
                ]
            }
            
    def SaveToFile(self):
        OutputPath = os.path.join(self.FolderPath, "sounds.json")
        with open(OutputPath, "w") as f:
            json.dump(self.SoundsData, f, indent=2)
            
    def Execute(self):
        self.ValidatePath()
        self.GenerateJsonStructure()
        self.SaveToFile()

def Main():
    if len(sys.argv) != 2:
        print("Usage: python SoundFile.py <folderPath>")
        sys.exit(1)
        
    Generator = SoundFileGenerator(sys.argv[1])
    try:
        Generator.Execute()
        print(f"Generated sounds.json in {sys.argv[1]}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    Main()