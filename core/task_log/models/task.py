from dataclasses import dataclass
from typing import List
from pathlib import Path
from .validators import validate_positive_integer, validate_string, validate_json_file, generate_list_string

@dataclass
class Task:
    Id: int
    ProjectId: int
    Name: str
    Description: str

    def __post_init__(self):
        validate_positive_integer(self.Id, "Id")
        validate_positive_integer(self.ProjectId, "ProjectId")
        validate_string(self.Name, "Name", max_length=50)
        validate_string(self.Description, "Description", max_length=300)
        
    @classmethod
    def loadFromJson(cls, filePath: Path) -> List['Task']:
        data = validate_json_file(filePath)
        return [cls(**item) for item in data]

    @staticmethod
    def getListString(items: List['Task']) -> str:
        columns = [
            ("ID", "Id", str),
            ("Project ID", "ProjectId", str),
            ("Name", "Name"),
            ("Description", "Description")
        ]
        return generate_list_string(items, columns)