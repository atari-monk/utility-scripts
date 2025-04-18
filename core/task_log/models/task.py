from dataclasses import dataclass
from typing import List
from pathlib import Path
import json

@dataclass
class Task:
    Id: str
    ProjectId: str
    Name: str
    Description: str

    def __post_init__(self):
        if not isinstance(self.Id, int) or self.Id <= 0:
            raise ValueError("Id must be a positive integer")
        
        if not isinstance(self.ProjectId, int) or self.ProjectId <= 0:
            raise ValueError("ProjectId must be a positive integer")
        
        if not isinstance(self.Name, str):
            raise ValueError("Name must be a string")

        if len(self.Name) > 50:
            raise ValueError("Name cannot exceed 50 characters")
        
        if not isinstance(self.Description, str):
            raise ValueError("Description must be a string")
            
        if len(self.Description) > 300:
            raise ValueError("Description cannot exceed 300 characters")
        
    @classmethod
    def loadFromJson(cls, filePath: Path) -> List['Task']:
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
    def getListString(items: List['Task']) -> str:
        if not items:
            return "No tasks to list"
        
        max_id_len = max(len(str(task.Id)) for task in items)
        max_project_id_len = max(len(str(task.ProjectId)) for task in items)
        max_name_len = max(len(task.Name) for task in items)
        
        header = (f"{'ID':<{max_id_len}}  {'Project ID':<{max_project_id_len}}  {'Name':<{max_name_len}}  Description")
        separator = '-' * len(header)
        
        lines = [header, separator]
        for task in items:
            lines.append(
                f"{task.Id:<{max_id_len}}  "
                f"{task.ProjectId:<{max_project_id_len}}  "
                f"{task.Name:<{max_name_len}}  "
                f"{task.Description}"
            )
        
        return '\n'.join(lines)