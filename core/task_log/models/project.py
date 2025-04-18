from typing import List
from dataclasses import dataclass
from pathlib import Path
from core.task_log.models.base_model import BaseModel
from .validators import validate_positive_integer, validate_string, validate_json_file, generate_list_string

@dataclass
class Project(BaseModel):
    Id: int
    Name: str
    Description: str

    def __post_init__(self):
        validate_positive_integer(self.Id, "Id")
        validate_string(self.Name, "Name", max_length=50, must_be_lowercase=True, no_spaces=True)
        validate_string(self.Description, "Description", max_length=300)
        
    @staticmethod
    def getListString(items: List['Project']) -> str:
        columns = [
            ("ID", "Id", str),
            ("Name", "Name"),
            ("Description", "Description")
        ]
        return generate_list_string(items, columns)