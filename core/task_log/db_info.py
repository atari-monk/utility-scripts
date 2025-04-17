from pathlib import Path

class DbInfo:
    def __init__(self, repo_path, db_name):
        self._base_path = Path(repo_path)
        self._db_name = db_name
        self.db_path.mkdir(parents=True, exist_ok=True)

    @property
    def db_path(self):
        return self._base_path / self._db_name
