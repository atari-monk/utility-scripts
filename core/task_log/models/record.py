from dataclasses import dataclass
from pathlib import Path
from typing import List
from .validators import validate_string, validate_json_file, validate_date_string, generate_list_string

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
        validate_date_string(self.Date, "Date")
        validate_string(self.Description, "Description", max_length=300)
        validate_string(self.Note, "Note", max_length=300)

    @classmethod
    def loadFromJson(cls, filePath: Path) -> List['Record']:
        data = validate_json_file(filePath)
        return [cls(**item) for item in data]

    @classmethod
    def load_last_record(cls, file_path: Path) -> 'Record':
        records = cls.loadFromJson(file_path)
        if not records:
            raise ValueError("No records found in file")
        return records[-1]
    
    @staticmethod
    def getListString(items: List['Record']) -> str:
        columns = [
            ("Date", "Date"),
            ("Task ID", "TaskId"),
            ("Description", "Description"),
            ("Estimate", "EstimateMinutes", str)
        ]
        return generate_list_string(items, columns)