from typing import TypeVar, Type, List
from pathlib import Path
import json

T = TypeVar('T', bound='BaseModel')

class BaseModel:
    @classmethod
    def loadFromJson(cls: Type[T], filePath: Path) -> List[T]:
        data = validate_json_file(filePath)
        return [cls(**item) for item in data]
      
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
