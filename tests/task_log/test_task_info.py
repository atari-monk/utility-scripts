import pytest
import json
from core.task_log.models.task import Task

def test_taskinfo_creation():
    task = Task(
        Id="task-123",
        ProjectId="proj-456",
        Name="sample-task",
        Description="A sample task description"
    )
    assert task.Id == "task-123"
    assert task.ProjectId == "proj-456"
    assert task.Name == "sample-task"
    assert task.Description == "A sample task description"

def test_name_lowercase_conversion():
    task = Task(
        Id="task-123",
        ProjectId="proj-456",
        Name="Sample-Task",
        Description="Test"
    )
    assert task.Name == "sample-task"

def test_description_length_validation():
    with pytest.raises(ValueError):
        Task(
            Id="task-123",
            ProjectId="proj-456",
            Name="sample-task",
            Description="A" * 301
        )

def test_load_from_json(tmp_path):
    test_data = [
        {
            "Id": "task-1",
            "ProjectId": "proj-1",
            "Name": "task-one",
            "Description": "First task"
        },
        {
            "Id": "task-2",
            "ProjectId": "proj-1",
            "Name": "task-two",
            "Description": "Second task"
        }
    ]
    
    file_path = tmp_path / "test_tasks.json"
    with open(file_path, 'w') as f:
        json.dump(test_data, f)
    
    loaded_tasks = Task.load_from_json(file_path)
    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].Name == "task-one"
    assert loaded_tasks[1].Description == "Second task"

def test_invalid_json_file():
    with pytest.raises(FileNotFoundError):
        Task.load_from_json("nonexistent.json")

def test_display_as_list(capsys):
    tasks = [
        Task(
            Id="task-1",
            ProjectId="proj-1",
            Name="task-one",
            Description="First task"
        ),
        Task(
            Id="task-2",
            ProjectId="proj-1",
            Name="task-two",
            Description="Second task"
        )
    ]
    
    Task.display_as_list(tasks)
    captured = capsys.readouterr()
    assert "task-one" in captured.out
    assert "Second task" in captured.out