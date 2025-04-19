from typing import TypeVar, Type, List, Any, Callable
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, fields
import json

T = TypeVar("T", bound="BaseModel")


@dataclass
class BaseModel:
    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            self._validate_field(field.name, value, field.type)

    def _validate_field(self, field_name: str, value: Any, field_type: type) -> None:
        if field_type == int:
            self._validate_positive_integer(value, field_name)
        elif field_type == str:
            self._validate_string(value, field_name)

    @staticmethod
    def _validate_positive_integer(value: Any, field_name: str) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{field_name} must be a positive integer")

    @staticmethod
    def _validate_string(
        value: Any,
        field_name: str,
        max_length: int = None,
        must_be_lowercase: bool = False,
        no_spaces: bool = False,
    ) -> None:
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")

        if max_length is not None and len(value) > max_length:
            raise ValueError(f"{field_name} cannot exceed {max_length} characters")

        if must_be_lowercase and value != value.lower():
            raise ValueError(f"{field_name} must be lowercase")

        if no_spaces and " " in value:
            raise ValueError(f"{field_name} must not contain spaces")

    @staticmethod
    def _validate_date_string(
        value: str, field_name: str, date_format: str = "%Y-%m-%d"
    ) -> None:
        try:
            datetime.strptime(value, date_format)
        except ValueError:
            raise ValueError(f"Invalid {field_name} format, expected {date_format}")

    @staticmethod
    def _validate_time_string(
        value: str, field_name: str, time_format: str = "%H:%M"
    ) -> None:
        try:
            datetime.strptime(value, time_format)
        except ValueError:
            raise ValueError(f"Invalid {field_name} format, expected {time_format}")

    @staticmethod
    def _validate_time_range(
        start_time: str,
        end_time: str,
        start_field_name: str = "StartTime",
        end_field_name: str = "EndTime",
        time_format: str = "%H:%M",
    ) -> None:
        start = datetime.strptime(start_time, time_format)
        end = datetime.strptime(end_time, time_format)
        if end <= start:
            raise ValueError(f"{end_field_name} must be after {start_field_name}")

    @classmethod
    def load_from_json(cls: Type[T], filePath: Path) -> List[T]:
        if not filePath.exists():
            raise FileNotFoundError(f"File not found: {filePath}")

        with open(filePath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("JSON data should be a list of items")

        return [cls(**item) for item in data]

    @classmethod
    def validate_ids(cls: Type[T], filePath: Path) -> bool:
        items = cls.load_from_json(filePath)
        ids = [item.id for item in items if hasattr(item, "id")]
        return len(ids) == len(set(ids)) and all(isinstance(id, int) for id in ids)

    @classmethod
    def get_next_id(cls: Type[T], filePath: Path) -> int:
        if not filePath.exists():
            return 1
        items = cls.load_from_json(filePath)
        if not items:
            return 1
        if not hasattr(items[0], "id"):
            raise AttributeError("Items must have an 'id' attribute")
        return max(item.id for item in items) + 1

    @classmethod
    def save_to_json(
        cls: Type[T], items: List[T], filePath: Path, indent: int = 2
    ) -> None:
        if not isinstance(items, list):
            raise ValueError("Items to save must be a list")

        new_data = [item.__dict__ for item in items if isinstance(item, cls)]
        if len(new_data) != len(items):
            raise ValueError(f"All items must be instances of {cls.__name__}")

        filePath.parent.mkdir(parents=True, exist_ok=True)

        try:
            existing_items = []
            if filePath.exists():
                existing_items = cls.load_from_json(filePath)
                existing_data = [item.__dict__ for item in existing_items]
            else:
                existing_data = []

            combined_data = existing_data + new_data

            with open(filePath, "w", encoding="utf-8") as f:
                json.dump(combined_data, f, indent=indent, ensure_ascii=False)
        except (IOError, TypeError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to save JSON to {filePath}: {str(e)}")

    @classmethod
    def generate_list_string(cls, items: List[T], columns: list) -> str:
        if not items:
            return f"No {cls.__name__.lower()}s to list"

        max_lengths = []
        for col in columns:
            header, field_name, *rest = col
            max_len = len(header)
            format_func = rest[0] if rest else None
            for item in items:
                value = getattr(item, field_name)
                if format_func:
                    value = format_func(value)
                value_len = len(str(value))
                if value_len > max_len:
                    max_len = value_len
            max_lengths.append(max_len)

        header_parts = []
        for i, (header, _, *_) in enumerate(columns):
            header_parts.append(f"{header:<{max_lengths[i]}}")
        header = "  ".join(header_parts)

        separator = "-" * len(header)
        lines = [header, separator]

        for item in items:
            line_parts = []
            for i, (_, field_name, *rest) in enumerate(columns):
                value = getattr(item, field_name)
                if rest:
                    value = rest[0](value)
                line_parts.append(f"{str(value):<{max_lengths[i]}}")
            lines.append("  ".join(line_parts))

        return "\n".join(lines)

    @classmethod
    def _get_id_input(cls, filePath: Path) -> int:
        if not cls.validate_ids(filePath=filePath):
            raise ValueError(f"{filePath} has errors in Ids")
        return cls.get_next_id(filePath=filePath)

    @classmethod
    def _get_string_input(
        cls,
        prompt: str,
        field_name: str,
        max_length: int = None,
        must_be_lowercase: bool = False,
        no_spaces: bool = False,
        allow_empty: bool = False,
    ) -> str:
        while True:
            try:
                value = input(prompt).strip()
                if not value and not allow_empty:
                    raise ValueError(f"{field_name} cannot be empty")
                cls._validate_string(
                    value,
                    field_name,
                    max_length=max_length,
                    must_be_lowercase=must_be_lowercase,
                    no_spaces=no_spaces,
                )
                return value
            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Please try again.\n")

    @classmethod
    def from_cli_input(
        cls: Type[T], filePath: Path, input_methods: List[Callable]
    ) -> T:
        print(f"Create a new {cls.__name__}")
        print("-" * 20)
        inputs = {}
        for method in input_methods:
            result = method()
            inputs.update(result)
        return cls(**inputs)
