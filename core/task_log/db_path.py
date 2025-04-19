from pathlib import Path


class DbPath:
    def __init__(self, repo_path: Path, db_folder: str):
        self.repo_path = repo_path
        self.db_folder = db_folder
        self.path.mkdir(parents=True, exist_ok=True)

    @property
    def path(self) -> Path:
        return self.repo_path / self.db_folder
