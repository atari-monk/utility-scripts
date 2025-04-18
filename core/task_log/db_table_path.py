from pathlib import Path
from typing import Callable
from core.task_log.db_path import DbPath

class DbTablePath:
    def __init__(self, db_path: DbPath, name_func: Callable[[], str]):
        self.db_path = db_path
        self.name_func = name_func

    def get_path(self, ext: str = "json") -> Path:
        return self.db_path.path / f"{self.name_func()}.{ext}"
