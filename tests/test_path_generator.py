from datetime import datetime
import tempfile
import pytest
from pathlib import Path
from core.task_log.path_generator import PathGenerator

class TestPathGenerator:
    @pytest.fixture
    def path_gen(self):
        return PathGenerator(base_repo="test_repo", db_name="test_db")

    def test_initialization(self, path_gen):
        assert path_gen.base_repo == "test_repo"
        assert path_gen.db_name == "test_db"

    def test_generate_path_structure(self, path_gen):
        test_time = datetime(2023, 5, 15)
        expected_path = Path("test_repo/test_db/2023/05")
        assert path_gen._generate_path_structure(test_time) == expected_path

    def test_ensure_path_exists_creates_dirs(self, path_gen):
        with tempfile.TemporaryDirectory() as temp_dir:
            path_gen.base_repo = temp_dir
            test_path = Path(temp_dir) / "new_dir" / "sub_dir"
            path_gen._ensure_path_exists(test_path)
            assert test_path.exists()

    def test_get_full_path(self, path_gen):
        with tempfile.TemporaryDirectory() as temp_dir:
            path_gen.base_repo = temp_dir
            test_time = datetime(2023, 5, 15)
            file_name = "test_file"
            full_path = path_gen.get_full_path(file_name, test_time)
            
            expected_path = Path(temp_dir) / "test_db" / "2023" / "05" / "test_file"
            assert full_path == expected_path
            assert expected_path.parent.exists()

    def test_get_full_path_uses_current_time(self, path_gen):
        with tempfile.TemporaryDirectory() as temp_dir:
            path_gen.base_repo = temp_dir
            file_name = "test_file"
            full_path = path_gen.get_full_path(file_name)
            
            now = datetime.now()
            expected_path = Path(temp_dir) / "test_db" / now.strftime("%Y") / now.strftime("%m") / "test_file"
            assert full_path.parent == expected_path.parent