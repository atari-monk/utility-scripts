from dataclasses import dataclass
from typing import List
import json
import os

@dataclass
class TaskInfo:
    Id: str
    ProjectId: str
    Name: str
    Description: str

    def __post_init__(self):
        self.Name = self.Name.lower()
        if len(self.Description) > 300:
            raise ValueError("Description must be 300 characters or less")

    @classmethod
    def from_json(cls, file_path: str) -> List['TaskInfo']:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        return [cls(**task_data) for task_data in data]

    @staticmethod
    def display_as_list(tasks: List['TaskInfo']):
        for task in tasks:
            print(f"ID: {task.Id}, Project: {task.ProjectId}, Name: {task.Name}, Description: {task.Description}")