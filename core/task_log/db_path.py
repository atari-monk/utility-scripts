from pathlib import Path

class DbPath:
    def __init__(self, repoPath, dbFolder):
        self.repoPath = Path(repoPath)
        self.dbFolder = dbFolder
        self.path.mkdir(parents=True, exist_ok=True)

    @property
    def path(self):
        return self.repoPath / self.dbFolder
