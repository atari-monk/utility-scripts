from dataclasses import dataclass
import json
from pathlib import Path
from typing import List

@dataclass
class Project:
    Id: int
    Name: str
    Description: str

    def __post_init__(self):
        if not isinstance(self.Id, int) or self.Id <= 0:
            raise ValueError("ID must be a positive integer")
        
        if not isinstance(self.Name, str):
            raise ValueError("Name must be a string")
            
        if not self.Name.islower() or ' ' in self.Name:
            raise ValueError("Name must be lowercase and in repo-name format (no spaces)")
            
        if len(self.Name) > 50:
            raise ValueError("Name cannot exceed 50 characters")
            
        if not isinstance(self.Description, str):
            raise ValueError("Description must be a string")
            
        if len(self.Description) > 300:
            raise ValueError("Description cannot exceed 300 characters")

    @classmethod
    def loadFromJson(cls, filePath: Path) -> List['Project']:
        if not filePath.exists():
            raise FileNotFoundError(f"File not found: {filePath}")
        
        try:
            with open(filePath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file {filePath}: {e.msg}", e.doc, e.pos)
        
        if not isinstance(data, list):
            raise ValueError("JSON data should be a list of projects")
            
        return [cls(**item) for item in data]

    @staticmethod
    def getListString(items: List['Project']) -> str:
        if not items:
            return "No projects to list"
            
        max_id_len = max(len(str(p.Id)) for p in items)
        max_name_len = max(len(p.Name) for p in items)
        
        header = (f"{'ID':<{max_id_len}}  {'Name':<{max_name_len}}  Description")
        separator = '-' * len(header)
        
        lines = [header, separator]
        for item in items:
            lines.append(f"{item.Id:<{max_id_len}}  {item.Name:<{max_name_len}}  {item.Description}")
        
        return '\n'.join(lines)