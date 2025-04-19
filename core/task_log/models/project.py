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
        self._validate_string(
            self.name, "name", max_length=50, must_be_lowercase=True, no_spaces=True
        )
        self._validate_string(self.description, "description", max_length=300)

    @staticmethod
    def get_list_string(items: List["Project"]) -> str:
        columns = [("Id", "id", int), ("Name", "name"), ("Description", "description")]
        return Project.generate_list_string(items, columns)

    @classmethod
    def from_cli_input(cls, file_path: Path) -> "Project":
        def get_id():
            return {"id": cls._get_id_input(file_path)}

        def get_name():
            name = cls._get_string_input(
                "Name (max 50 chars, lowercase, no spaces): ",
                "name",
                max_length=50,
                must_be_lowercase=True,
                no_spaces=True,
            )
            cls._validate_unique_field(file_path, "name", name)
            return {"name": name}

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
            file_path, input_methods=[get_id, get_name, get_description]
        )

    @classmethod
    def select_project(cls, filePath: Path) -> "Project":
        if not filePath.exists():
            raise FileNotFoundError(f"No projects file found at {filePath}")

        projects = cls.load_from_json(filePath)
        if not projects:
            raise ValueError("No projects available to select")

        print("\nAvailable Projects:")
        print(cls.get_list_string(projects))

        while True:
            try:
                selected_id = int(input("\nEnter project ID to select: "))
                for project in projects:
                    if project.id == selected_id:
                        return project
                raise ValueError("Invalid project ID")
            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Please try again.")
