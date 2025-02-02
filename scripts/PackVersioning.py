import json
import argparse
import re
import requests

def GetLatestReleaseTag(Repo: str) -> str:
    """Get latest release tag from GitHub repository
    
    Args:
        Repo (str): Repository name in format 'owner/repo'
        
    Returns:
        str: Latest release tag or 'v0.0.0' if none found
    """
    try:
        Response = requests.get(f"https://api.github.com/repos/{Repo}/releases/latest")
        return Response.json()["tag_name"]
    except Exception:
        return "v0.0.0"

def UpdatePackMeta(FilePath: str, Branch: str, Repo: str) -> None:
    """Update pack.mcmeta with current branch and latest release tag
    
    Args:
        FilePath (str): Path to pack.mcmeta
        Branch (str): Current branch name
        Repo (str): Repository name for GitHub API
    """
    # Load JSON
    with open(FilePath, 'r', encoding='utf-8') as File:
        Data = json.load(File)
    
    # Get latest tag
    LatestTag = GetLatestReleaseTag(Repo)
    
    # Update description using regex
    Description = Data["pack"]["description"]
    Description = re.sub(r'<branch>', Branch, Description)
    Description = re.sub(r'<latest tag>', LatestTag, Description)
    Data["pack"]["description"] = Description
    
    print(f"Updated pack.mcmeta with branch {Branch} and latest tag {LatestTag}")
    print(Data)

def Main():
    Parser = argparse.ArgumentParser(description='Update pack.mcmeta version info')
    Parser.add_argument('--branch', default='1.21', help='Current branch name')
    Parser.add_argument('--file', default='pack.mcmeta', help='Path to pack.mcmeta')
    Parser.add_argument('--repo', default='Hyphonic/Conquest', help='GitHub repository')
    
    Args = Parser.parse_args()
    UpdatePackMeta(Args.file, Args.branch, Args.repo)

if __name__ == "__main__":
    Main()