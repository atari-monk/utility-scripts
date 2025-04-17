import unittest
import tempfile
import shutil
from core.task_log.db_info import DbInfo
from core.task_log.db_table import DbTable

class TestDbTable(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_info = DbInfo(self.test_dir, "test_db")
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_get_path_with_string_naming_logic(self):
        table_name = "projects"
        db_table = DbTable(self.db_info, lambda: table_name)
        
        expected_path = self.db_info.db_path / f"{table_name}.json"
        self.assertEqual(db_table.get_path(), expected_path)
        
        expected_path = self.db_info.db_path / f"{table_name}.csv"
        self.assertEqual(db_table.get_path("csv"), expected_path)
    
    def test_get_path_with_callable_naming_logic(self):
        def naming_func():
            return "dynamic_name"
            
        db_table = DbTable(self.db_info, naming_func)
        
        expected_path = self.db_info.db_path / "dynamic_name.json"
        self.assertEqual(db_table.get_path(), expected_path)
    
    def test_get_path_with_different_extensions(self):
        table_name = "records"
        db_table = DbTable(self.db_info, lambda: table_name)
        
        extensions = ["json", "csv", "txt", "bin"]
        for ext in extensions:
            expected_path = self.db_info.db_path / f"{table_name}.{ext}"
            self.assertEqual(db_table.get_path(ext), expected_path)
    
    def test_db_table_initialization(self):
        naming_logic = lambda: "test"
        db_table = DbTable(self.db_info, naming_logic)
        
        self.assertEqual(db_table.db_info, self.db_info)
        self.assertEqual(db_table._naming_logic, naming_logic)

if __name__ == '__main__':
    unittest.main()