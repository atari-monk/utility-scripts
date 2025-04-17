from pathlib import Path
from datetime import datetime

class PathGenerator:
    def __init__(self, base_repo, db_name):
        self.base_repo = base_repo
        self.db_name = db_name

    def _generate_path_structure(self, time_reference=None):
        reference_time = time_reference if time_reference else datetime.now()
        return Path(self.base_repo) / self.db_name / reference_time.strftime("%Y") / reference_time.strftime("%m")

    def _ensure_path_exists(self, path):
        path.mkdir(parents=True, exist_ok=True)

    def get_full_path(self, file_name, time_reference=None):
        path_structure = self._generate_path_structure(time_reference)
        self._ensure_path_exists(path_structure)
        return path_structure / file_name