from typing import List
from dataclasses import dataclass
from core.task_log.models.base_model import BaseModel

@dataclass
class Project(BaseModel):
    id: int
    name: str
    description: str

    def __post_init__(self):
        super().__post_init__()
        self._validate_string(self.name, "name", max_length=50, must_be_lowercase=True, no_spaces=True)
        self._validate_string(self.description, "description", max_length=300)
        
    @staticmethod
    def get_list_string(items: List['Project']) -> str:
        columns = [
            ("Id", "id", int),
            ("Name", "name"),
            ("Description", "description")
        ]
        return Project.generate_list_string(items, columns)
