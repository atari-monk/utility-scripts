from typing import List
from dataclasses import dataclass
from core.task_log.models.base_model import BaseModel

@dataclass
class Task(BaseModel):
    id: int
    project_id: int
    name: str
    description: str

    def __post_init__(self):
        super().__post_init__()
        self._validate_string(self.name, "name", max_length=50)
        self._validate_string(self.description, "description", max_length=300)

    @staticmethod
    def get_list_string(items: List['Task']) -> str:
        columns = [
            ("Id", "id", int),
            ("Project Id", "project_id", int),
            ("Name", "name"),
            ("Description", "description")
        ]
        return Task.generate_list_string(items, columns)
