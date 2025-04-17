from dataclasses import dataclass
import json
from typing import List

@dataclass
class CliScriptsInfo:
    CliName: str
    Description: str

    def __post_init__(self):
        if len(self.CliName) != 4 or not self.CliName.islower():
            raise ValueError("CliName must be 4 lowercase letters")
        if len(self.Description) > 300:
            raise ValueError("Description must be 300 characters or less")

    @classmethod
    def load_from_json(cls, file_path) -> List['CliScriptsInfo']:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return [cls(**item) for item in data]

    @staticmethod
    def to_string(scripts: List['CliScriptsInfo']) -> str:
        return "\n".join(
            f"{script.CliName}: {script.Description}"
            for script in scripts
        )