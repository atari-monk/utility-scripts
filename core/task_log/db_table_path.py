from core.task_log.db_path import DbPath

class DbTablePath:
    def __init__(self, dbPath:DbPath, namingLogic):
        self.dbPath = dbPath
        self.namingLogic = namingLogic
    
    def getPath(self, ext="json"):
        return self.dbPath.path / f"{self.namingLogic()}.{ext}"
