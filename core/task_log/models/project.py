from typing import List
from dataclasses import dataclass
from core.task_log.models.base_model import BaseModel

@dataclass
class Project(BaseModel):
    Id: int
    Name: str
    Description: str

    def __post_init__(self):
        super().__post_init__()
        self._validate_string(self.Name, "Name", max_length=50, must_be_lowercase=True, no_spaces=True)
        self._validate_string(self.Description, "Description", max_length=300)
        
    @staticmethod
    def getListString(items: List['Project']) -> str:
        columns = [
            ("ID", "Id", str),
            ("Name", "Name"),
            ("Description", "Description")
        ]
        return Project.generate_list_string(items, columns)