from pathlib import Path
from typing import List
from dataclasses import dataclass
from core.task_log.models.base_model import BaseModel
from core.task_log.models.project import Project


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
    def get_list_string(items: List["Task"]) -> str:
        columns = [
            ("Id", "id", int),
            ("Project Id", "project_id", int),
            ("Name", "name"),
            ("Description", "description"),
        ]
        return Task.generate_list_string(items, columns)

    @classmethod
    def from_cli_input(cls, filePath: Path, projectFilePath: Path) -> "Task":
        def get_id():
            return {"id": cls._get_id_input(filePath)}

        def get_project_id():
            return {"project_id": Project.from_cli_input(projectFilePath)}

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
            filePath, input_methods=[get_id, get_project_id, get_name, get_description]
        )
