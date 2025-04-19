import pytest
import json
from jsonschema import ValidationError
from core.task_log.models.project import Project


def test_valid_project_info_creation():
    project = Project("id1", "validname", "Short description")
    assert project.Id == "id1"
    assert project.Name == "validname"
    assert project.Description == "Short description"


def test_invalid_name_format():
    with pytest.raises(ValueError):
        Project("id1", "Invalid Name", "Description")


def test_invalid_name_case():
    with pytest.raises(ValueError):
        Project("id1", "InvalidName", "Description")


def test_description_too_long():
    long_desc = "a" * 301
    with pytest.raises(ValueError):
        Project("id1", "validname", long_desc)


def test_from_json_valid_file(tmp_path):
    test_data = [
        {"Id": "test1", "Name": "projectone", "Description": "First test project"}
    ]
    file_path = tmp_path / "test.json"
    with open(file_path, "w") as f:
        json.dump(test_data, f)

    projects = Project.load_from_json(file_path)
    assert len(projects) == 1
    assert projects[0].Name == "projectone"


def test_from_json_invalid_schema(tmp_path):
    test_data = [{"WrongField": "value"}]
    file_path = tmp_path / "test.json"
    with open(file_path, "w") as f:
        json.dump(test_data, f)

    with pytest.raises(ValidationError):
        Project.load_from_json(file_path)


def test_display_as_list(capsys):
    projects = [
        Project("id1", "projectone", "First project"),
        Project("id2", "projecttwo", "Second project"),
    ]
    Project.getListString(projects)
    captured = capsys.readouterr()
    assert "projectone" in captured.out
    assert "projecttwo" in captured.out
