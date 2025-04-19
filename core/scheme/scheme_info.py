import json
import os
from dataclasses import dataclass
from typing import List
import pyperclip
import jsonschema


@dataclass
class SchemeInfo:
    Name: str
    Description: str
    Path: str

    def __post_init__(self):
        self._validate_name()
        self._validate_description()
        self._validate_path()

    def _validate_name(self):
        if not isinstance(self.Name, str):
            raise ValueError("Name must be a string")
        if len(self.Name) > 50:
            raise ValueError("Name exceeds 50 characters")
        if not self.Name.islower():
            raise ValueError("Name must be lowercase")

    def _validate_description(self):
        if not isinstance(self.Description, str):
            raise ValueError("Description must be a string")
        if len(self.Description) > 300:
            raise ValueError("Description exceeds 300 characters")

    def _validate_path(self):
        if not isinstance(self.Path, str):
            raise ValueError("Path must be a string")
        if not os.path.exists(self.Path):
            raise ValueError("Path does not exist")

    @classmethod
    def from_json_file(cls, file_path: str) -> List["SchemeInfo"]:
        with open(file_path, "r") as f:
            data = json.load(f)

        schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Name": {"type": "string", "maxLength": 50},
                    "Description": {"type": "string", "maxLength": 300},
                    "Path": {"type": "string"},
                },
                "required": ["Name", "Description", "Path"],
            },
        }

        jsonschema.validate(instance=data, schema=schema)

        return [cls(**item) for item in data]

    @staticmethod
    def load_and_copy_scheme(schemes: List["SchemeInfo"], name: str) -> None:
        matching_schemes = [s for s in schemes if s.Name == name]

        if not matching_schemes:
            raise ValueError(f"No scheme found with name: {name}")
        if len(matching_schemes) > 1:
            raise ValueError(f"Multiple schemes found with name: {name}")

        scheme = matching_schemes[0]

        try:
            with open(scheme.Path, "r") as f:
                content = f.read()
            pyperclip.copy(content)
        except Exception as e:
            raise ValueError(f"Failed to load or copy scheme: {str(e)}")
