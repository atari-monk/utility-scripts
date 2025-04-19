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
    def from_cli_input(cls) -> "Project":
        print("Create a new Project")
        print("--------------------")

        while True:
            try:
                id_input = input("ID (number): ").strip()
                if not id_input:
                    raise ValueError("ID cannot be empty")
                id = int(id_input)

                name = input("Name (max 50 chars, lowercase, no spaces): ").strip()
                if not name:
                    raise ValueError("Name cannot be empty")

                description = input("Description (max 300 chars): ").strip()
                if not description:
                    description = ""

                return cls(id=id, name=name, description=description)

            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Please try again.\n")
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please try again.\n")
                continue
