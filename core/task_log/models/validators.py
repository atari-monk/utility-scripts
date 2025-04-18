from datetime import datetime
import json
from pathlib import Path
from typing import Any

def validate_positive_integer(value: Any, field_name: str) -> None:
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field_name} must be a positive integer")

def validate_string(value: Any, field_name: str, max_length: int = None, 
                    must_be_lowercase: bool = False, no_spaces: bool = False) -> None:
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string")
    
    if max_length is not None and len(value) > max_length:
        raise ValueError(f"{field_name} cannot exceed {max_length} characters")
    
    if must_be_lowercase and value != value.lower():
        raise ValueError(f"{field_name} must be lowercase")
    
    if no_spaces and ' ' in value:
        raise ValueError(f"{field_name} must not contain spaces")

def validate_date_string(value: str, field_name: str, date_format: str = "%Y-%m-%d") -> None:
    try:
        datetime.strptime(value, date_format)
    except ValueError:
        raise ValueError(f"Invalid {field_name} format, expected {date_format}")

def validate_json_file(file_path: Path) -> list:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file {file_path}: {e.msg}", e.doc, e.pos)
    
    if not isinstance(data, list):
        raise ValueError("JSON data should be a list of items")
    
    return data

def generate_list_string(items: list, columns: list) -> str:
    if not items:
        return f"No items to list"
    
    max_lengths = []
    for header, field_name, *_ in columns:
        max_len = len(header)
        for item in items:
            value = getattr(item, field_name)
            if len(columns[0]) > 2:
                format_func = columns[0][2]
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
        for i, (_, field_name, *_) in enumerate(columns):
            value = getattr(item, field_name)
            if len(columns[i]) > 2:
                format_func = columns[i][2]
                value = format_func(value)
            line_parts.append(f"{str(value):<{max_lengths[i]}}")
        lines.append("  ".join(line_parts))
    
    return '\n'.join(lines)