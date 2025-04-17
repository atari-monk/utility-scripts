from core.task_log.db_info import DbInfo

class DbTable:
    def __init__(self, db_info:DbInfo, naming_logic):
        self.db_info = db_info
        self._naming_logic = naming_logic
    
    def get_path(self, ext="json"):
        return self.db_info.db_path / f"{self._naming_logic()}.{ext}"
