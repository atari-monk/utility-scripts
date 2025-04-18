from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
from typing import List

@dataclass
class Record:
    Date: str
    TaskId: str
    Description: str
    EstimateMinutes: int
    StartTime: str
    EndTime: str
    ActualMinutes: int
    Note: str

    def __post_init__(self):
        self._validate_date()
        self._validate_description()
        self._validate_note()

    def _validate_date(self):
        try:
            datetime.strptime(self.Date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format, expected YYYY-MM-DD")

    def _validate_description(self):
        if len(self.Description) > 300:
            raise ValueError("Description cannot exceed 300 characters")

    def _validate_note(self):
        if len(self.Note) > 300:
            raise ValueError("Note cannot exceed 300 characters")

    @classmethod
    def loadFromJson(cls, filePath: Path) -> List['Record']:
        if not filePath.exists():
            raise FileNotFoundError(f"File not found: {filePath}")
        
        try:
            with open(filePath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file {filePath}: {e.msg}", e.doc, e.pos)
        
        if not isinstance(data, list):
            raise ValueError("JSON data should be a list of projects")
            
        return [cls(**item) for item in data]

    @classmethod
    def load_last_record(cls, file_path: Path) -> 'Record':
        records = cls.load_from_json(file_path)
        if not records:
            raise ValueError("No records found in file")
        return records[-1]
    
    @staticmethod
    def getListString(items: List['Record']) -> str:
        if not items:
            return "No records to list"
        
        max_date_len = max(len(record.Date) for record in items)
        max_task_id_len = max(len(record.TaskId) for record in items)
        max_desc_len = max(len(record.Description) for record in items)
        max_estimate_len = max(len(str(record.EstimateMinutes)) for record in items)
        
        header = (f"{'Date':<{max_date_len}}  {'Task ID':<{max_task_id_len}}  "
                f"{'Description':<{max_desc_len}}  {'Estimate':<{max_estimate_len}}")
        separator = '-' * len(header)
        
        lines = [header, separator]
        for record in items:
            lines.append(
                f"{record.Date:<{max_date_len}}  "
                f"{record.TaskId:<{max_task_id_len}}  "
                f"{record.Description:<{max_desc_len}}  "
                f"{record.EstimateMinutes:<{max_estimate_len}}"
            )
        
        return '\n'.join(lines)