import shutil
import tempfile
import unittest
from pathlib import Path
from core.task_log.db_path import DbPath


class TestDbInfo(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_init_creates_directory(self):
        db_info = DbPath(Path(self.test_dir), "")
        expected_path = Path(db_info.path)
        self.assertTrue(expected_path.exists())
        self.assertTrue(expected_path.is_dir())

    def test_db_path_property(self):
        repo_path = Path(self.test_dir)
        db_name = "test_db"
        db_info = DbPath(repo_path, db_name)

        expected_path = repo_path / db_name
        self.assertEqual(db_info.path, expected_path)

    def test_with_string_path(self):
        db_name = "string_test_db"
        db_info = DbPath(self.test_dir, db_name)

        expected_path = Path(self.test_dir) / db_name
        self.assertEqual(db_info.path, expected_path)

    def test_with_path_object(self):
        db_name = "path_obj_test_db"
        path_obj = Path(self.test_dir)
        db_info = DbPath(path_obj, db_name)

        expected_path = path_obj / db_name
        self.assertEqual(db_info.path, expected_path)
