from typing import List
from dataclasses import dataclass
from core.task_log.models.base_model import BaseModel

@dataclass
class Task(BaseModel):
    Id: int
    ProjectId: int
    Name: str
    Description: str

    def __post_init__(self):
        super().__post_init__()
        self._validate_string(self.Name, "Name", max_length=50)
        self._validate_string(self.Description, "Description", max_length=300)

    @staticmethod
    def getListString(items: List['Task']) -> str:
        columns = [
            ("Id", "Id", int),
            ("Project Id", "ProjectId", int),
            ("Name", "Name"),
            ("Description", "Description")
        ]
        return Task.generate_list_string(items, columns)