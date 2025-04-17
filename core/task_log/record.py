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

    def as_list(self):
        return [
            self.Date,
            self.TaskId,
            self.Description,
            self.EstimateMinutes,
            self.StartTime,
            self.EndTime,
            self.ActualMinutes,
            self.Note
        ]

    @staticmethod
    def display_as_list(records: List['Record']):
        for record in records:
            print(f"Date: {record.Date}, TaskId: {record.TaskId}, Description: {record.Description}, EstimateMinutes: {record.EstimateMinutes}, StartTime: {record.StartTime}, EndTime: {record.EndTime}, ActualMinutes: {record.ActualMinutes}, Note: {record.Note}")

    @classmethod
    def load_from_json(cls, file_path: Path) -> List['Record']:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return [cls(**record_data) for record_data in data]

    @classmethod
    def load_last_record(cls, file_path: Path) -> 'Record':
        records = cls.load_from_json(file_path)
        if not records:
            raise ValueError("No records found in file")
        return records[-1]