from datetime import datetime
from typing import List
from pathlib import Path
from dataclasses import dataclass
from core.task_log.models.base_model import BaseModel


@dataclass
class Record(BaseModel):
    id: int
    date: str
    task_id: int
    description: str
    estimate_minutes: int
    start_time: str
    end_time: str = None
    actual_minutes: int = None
    note: str = None

    def __post_init__(self):
        self._validate_date_string(self.date, "date")
        self._validate_string(self.description, "description", max_length=300)
        self._validate_time_string(self.start_time, "start_time")
        if self.end_time:
            self._validate_time_string(self.end_time, "end_time")
            if self.start_time:
                self._validate_time_range(self.start_time, self.end_time)
                self._calculate_actual_minutes()
                self._validate_positive_integer(self.actual_minutes, "estimate_minutes")
        if self.note:
            self._validate_string(self.note, "note", max_length=300)

    def _calculate_actual_minutes(self):
        start_h, start_m = map(int, self.start_time.split(":"))
        end_h, end_m = map(int, self.end_time.split(":"))
        self.actual_minutes = (end_h * 60 + end_m) - (start_h * 60 + start_m)

    @staticmethod
    def get_list_string(items: List["Record"]) -> str:
        columns = [
            ("Id", "id", int),
            ("Date", "date"),
            ("Task Id", "task_id", int),
            ("Description", "description"),
            ("Estimate", "estimate_minutes", str),
            ("StartTime", "start_time", str),
            ("EndTime", "end_time", str),
            ("ActualMinutes", "actual_minutes", str),
            ("Note", "note", str),
        ]
        return Record.generate_list_string(items, columns)

    @classmethod
    def from_cli_input(cls, filePath: Path, task_id: int) -> "Record":
        def get_id():
            return {"id": cls._get_id_input(filePath)}

        def get_date():
            return {
                "date": cls._get_string_input(
                    "Date (YYYY-MM-DD): ", "date", allow_empty=False
                )
            }

        def get_task_id():
            return {"task_id": task_id}

        def get_description():
            return {
                "description": cls._get_string_input(
                    "Description: ", "description", max_length=300, allow_empty=False
                )
            }

        def get_estimate_minutes():
            return {
                "estimate_minutes": cls._get_positive_integer_input(
                    "Estimated minutes: ", "estimate_minutes"
                )
            }

        def get_start_time():
            return {
                "start_time": cls._get_string_input(
                    "Start time (HH:MM): ", "start_time", allow_empty=False
                )
            }

        inputs = {}
        for method in [
            get_id,
            get_task_id,
            get_date,
            get_description,
            get_estimate_minutes,
            get_start_time,
        ]:
            inputs.update(method())

        return cls(**inputs)

    def update_from_cli(self):
        def get_end_time():
            return {
                "end_time": self._get_string_input(
                    f"End time (HH:MM) [current: {self.end_time}]: ",
                    "end_time",
                    default_value=datetime.now().strftime("%H:%M"),
                )
            }

        def get_note():
            return {
                "note": self._get_string_input(
                    f"Note [current: {self.note}]: ",
                    "note",
                    max_length=300,
                    allow_empty=True,
                    default_value=self.note,
                )
            }

        inputs = {}
        for method in [get_end_time, get_note]:
            inputs.update(method())

        self.end_time = inputs["end_time"]
        self.note = inputs["note"]
        if self.start_time and self.end_time:
            self._calculate_actual_minutes()

    @classmethod
    def _get_positive_integer_input(cls, prompt: str, field_name: str) -> int:
        while True:
            try:
                value = input(prompt).strip()
                if not value:
                    raise ValueError(f"{field_name} cannot be empty")
                value = int(value)
                cls._validate_positive_integer(value, field_name)
                return value
            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Please try again.\n")
