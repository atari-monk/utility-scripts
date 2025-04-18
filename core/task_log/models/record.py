from typing import List
from pathlib import Path
from dataclasses import dataclass
from core.task_log.models.base_model import BaseModel

@dataclass
class Record(BaseModel):
    Date: str
    TaskId: int
    Description: str
    EstimateMinutes: int
    StartTime: str
    EndTime: str
    ActualMinutes: int
    Note: str

    def __post_init__(self):
        super().__post_init__()
        self._validate_date_string(self.Date, "Date")
        self._validate_string(self.Description, "Description", max_length=300)
        self._validate_string(self.Note, "Note", max_length=300)

    @classmethod
    def loadLastRecord(cls, file_path: Path) -> 'Record':
        records = cls.loadFromJson(file_path)
        if not records:
            raise ValueError("No records found in file")
        return records[-1]
    
    @staticmethod
    def getListString(items: List['Record']) -> str:
        columns = [
            ("Date", "Date"),
            ("Task Id", "TaskId", int),
            ("Description", "Description"),
            ("Estimate", "EstimateMinutes", str),
            ("StartTime", "StartTime", str),
            ("EndTime", "EndTime", str),
            ("ActualMinutes", "ActualMinutes", str),
            ("Note", "Note", str)
        ]
        return Record.generate_list_string(items, columns)