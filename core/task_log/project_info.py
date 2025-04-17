from dataclasses import dataclass
import json
from typing import List
from jsonschema import validate

@dataclass
class ProjectInfo:
    id: str
    name: str
    description: str

    def __post_init__(self):
        if not self.name.islower() or ' ' in self.name:
            raise ValueError("Name must be lowercase and in repo-name format")
        if len(self.description) > 300:
            raise ValueError("Description cannot exceed 300 characters")

    @classmethod
    def load_from_json(cls, file_path: str) -> List['ProjectInfo']:
        with open(file_path) as f:
            data = json.load(f)
        
        schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Id": {"type": "string"},
                    "Name": {"type": "string"},
                    "Description": {"type": "string"}
                },
                "required": ["Id", "Name", "Description"]
            }
        }
        
        validate(instance=data, schema=schema)
        
        return [cls(item["Id"], item["Name"], item["Description"]) for item in data]

    @classmethod
    def display_as_list(cls, projects: List['ProjectInfo']) -> None:
        for project in projects:
            print(f"ID: {project.id}, Name: {project.name}, Description: {project.description}")