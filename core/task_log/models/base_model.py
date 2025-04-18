from typing import TypeVar, Type, List, Any
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, fields
import json

T = TypeVar('T', bound='BaseModel')

@dataclass
class BaseModel:
    @classmethod
    def loadFromJson(cls: Type[T], filePath: Path) -> List[T]:
        if not filePath.exists():
            raise FileNotFoundError(f"File not found: {filePath}")
        
        with open(filePath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        
        if not isinstance(data, list):
            raise ValueError("JSON data should be a list of items")
        
        return [cls(**item) for item in data]

    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            self._validate_field(field.name, value, field.type)

    def _validate_field(self, field_name: str, value: Any, field_type: type) -> None:
        if field_type == int:
            self._validate_positive_integer(value, field_name)
        elif field_type == str:
            self._validate_string(value, field_name)
        # Add more type validations as needed

    @staticmethod
    def _validate_positive_integer(value: Any, field_name: str) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{field_name} must be a positive integer")

    @staticmethod
    def _validate_string(value: Any, field_name: str, 
                        max_length: int = None, 
                        must_be_lowercase: bool = False, 
                        no_spaces: bool = False) -> None:
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
        
        if max_length is not None and len(value) > max_length:
            raise ValueError(f"{field_name} cannot exceed {max_length} characters")
        
        if must_be_lowercase and value != value.lower():
            raise ValueError(f"{field_name} must be lowercase")
        
        if no_spaces and ' ' in value:
            raise ValueError(f"{field_name} must not contain spaces")

    @staticmethod
    def _validate_date_string(value: str, field_name: str, date_format: str = "%Y-%m-%d") -> None:
        try:
            datetime.strptime(value, date_format)
        except ValueError:
            raise ValueError(f"Invalid {field_name} format, expected {date_format}")

    @classmethod
    def generate_list_string(cls, items: List[T], columns: list) -> str:
        """
        Generate a formatted string for listing items.
        columns should be a list of tuples: (header_name, field_name, [optional_format_func])
        """
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
        
        separator = '-' * len(header)
        lines = [header, separator]
        
        for item in items:
            line_parts = []
            for i, (_, field_name, *rest) in enumerate(columns):
                value = getattr(item, field_name)
                if rest:
                    value = rest[0](value)
                line_parts.append(f"{str(value):<{max_lengths[i]}}")
            lines.append("  ".join(line_parts))
        
        return '\n'.join(lines)