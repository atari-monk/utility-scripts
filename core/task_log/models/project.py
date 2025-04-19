from pathlib import Path
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
        self._validate_string(
            self.name, "name", max_length=50, must_be_lowercase=True, no_spaces=True
        )
        self._validate_string(self.description, "description", max_length=300)

    @staticmethod
    def get_list_string(items: List["Project"]) -> str:
        columns = [("Id", "id", int), ("Name", "name"), ("Description", "description")]
        return Project.generate_list_string(items, columns)

    @classmethod
    def from_cli_input(cls, filePath: Path) -> "Project":
        def get_id():
            return {"id": cls._get_id_input(filePath)}

        def get_name():
            return {
                "name": cls._get_string_input(
                    "Name (max 50 chars, lowercase, no spaces): ",
                    "name",
                    max_length=50,
                    must_be_lowercase=True,
                    no_spaces=True,
                )
            }

        def get_description():
            return {
                "description": cls._get_string_input(
                    "Description (max 300 chars): ",
                    "description",
                    max_length=300,
                    allow_empty=False,
                )
            }

        return super().from_cli_input(
            filePath, input_methods=[get_id, get_name, get_description]
        )
