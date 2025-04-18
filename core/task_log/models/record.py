from datetime import datetime
from typing import List
from pathlib import Path
from dataclasses import dataclass
from core.task_log.models.base_model import BaseModel

@dataclass
class Record(BaseModel):
    date: str
    task_id: int
    description: str
    estimate_minutes: int
    start_time: str
    end_time: str
    actual_minutes: int
    note: str

    def __post_init__(self):
        super().__post_init__()
        self._validate_date_string(self.date, "date")
        self._validate_string(self.description, "description", max_length=300)
        self._validate_string(self.note, "note", max_length=300)
        self._validate_time_string(self.start_time, "start_time")
        self._validate_time_string(self.end_time, "end_time")
        if self.start_time and self.end_time:
            self._validate_time_range(self.start_time, self.end_time)
            self._calculate_actual_minutes()

    def _calculate_actual_minutes(self):
        start_h, start_m = map(int, self.start_time.split(':'))
        end_h, end_m = map(int, self.end_time.split(':'))
        self.actual_minutes = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        
    @classmethod
    def load_last_record(cls, file_path: Path) -> 'Record':
        records = cls.load_from_json(file_path)
        if not records:
            raise ValueError("No records found in file")
        return records[-1]
    
    @staticmethod
    def get_list_string(items: List['Record']) -> str:
        columns = [
            ("Date", "date"),
            ("Task Id", "task_id", int),
            ("Description", "description"),
            ("Estimate", "estimate_minutes", str),
            ("StartTime", "start_time", str),
            ("EndTime", "end_time", str),
            ("ActualMinutes", "actual_minutes", str),
            ("Note", "note", str)
        ]
        return Record.generate_list_string(items, columns)
