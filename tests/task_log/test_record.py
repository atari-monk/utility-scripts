import pytest
from core.task_log.models.record import Record


def test_record_initialization():
    record = Record(
        Date="2025-04-17",
        TaskId="1",
        Description="Test description",
        EstimateMinutes=30,
        StartTime="19:03",
        EndTime="20:55",
        ActualMinutes=112,
        Note="Test note",
    )
    assert record.Date == "2025-04-17"
    assert record.TaskId == "1"
    assert record.Description == "Test description"
    assert record.EstimateMinutes == 30
    assert record.StartTime == "19:03"
    assert record.EndTime == "20:55"
    assert record.ActualMinutes == 112
    assert record.Note == "Test note"


def test_record_validation():
    with pytest.raises(ValueError):
        Record(
            Date="invalid",
            TaskId="1",
            Description="",
            EstimateMinutes=0,
            StartTime="",
            EndTime="",
            ActualMinutes=0,
            Note="",
        )

    with pytest.raises(ValueError):
        Record(
            Date="2025-04-17",
            TaskId="1",
            Description="x" * 301,
            EstimateMinutes=0,
            StartTime="",
            EndTime="",
            ActualMinutes=0,
            Note="",
        )


def test_record_as_list():
    record = Record(
        Date="2025-04-17",
        TaskId="1",
        Description="Test",
        EstimateMinutes=30,
        StartTime="19:03",
        EndTime="20:55",
        ActualMinutes=112,
        Note="Note",
    )
    assert record.as_list() == [
        "2025-04-17",
        "1",
        "Test",
        30,
        "19:03",
        "20:55",
        112,
        "Note",
    ]


def test_load_from_json(tmp_path):
    json_data = """[
        {
            "Date": "2025-04-17",
            "TaskId": "1",
            "Description": "Test",
            "EstimateMinutes": 30,
            "StartTime": "19:03",
            "EndTime": "20:55",
            "ActualMinutes": 112,
            "Note": "Note"
        }
    ]"""
    file_path = tmp_path / "test.json"
    file_path.write_text(json_data)

    records = Record.load_from_json(file_path)
    assert len(records) == 1
    assert records[0].TaskId == "1"


def test_load_last_record(tmp_path):
    json_data = """[
        {"Date": "2025-04-16", "TaskId": "1", "Description": "First", "EstimateMinutes": 0, "StartTime": "", "EndTime": "", "ActualMinutes": 0, "Note": ""},
        {"Date": "2025-04-17", "TaskId": "2", "Description": "Last", "EstimateMinutes": 0, "StartTime": "", "EndTime": "", "ActualMinutes": 0, "Note": ""}
    ]"""
    file_path = tmp_path / "test.json"
    file_path.write_text(json_data)

    last_record = Record.loadLastRecord(file_path)
    assert last_record.TaskId == "2"
