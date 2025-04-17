import pytest
import json
from core.scheme import SchemeInfo
from core.scheme.SchemeLoader import SchemeLoader

def test_valid_scheme_info():
    valid = SchemeInfo(
        Name="validname",
        Description="A valid description",
        Path="C:\\valid\\path.json"
    )
    assert valid.Name == "validname"
    assert valid.Description == "A valid description"
    assert valid.Path == "C:\\valid\\path.json"

def test_invalid_name():
    with pytest.raises(ValueError):
        SchemeInfo(Name="InvalidName", Description="desc", Path="path")

def test_long_description():
    with pytest.raises(ValueError):
        SchemeInfo(
            Name="name",
            Description="x" * 301,
            Path="path"
        )

def test_from_valid_json():
    json_str = """
    [{
        "Name": "test",
        "Description": "Test description",
        "Path": "C:\\test.json"
    }]
    """
    schemes = SchemeLoader.from_json(json_str)
    assert len(schemes) == 1
    assert schemes[0].Name == "test"

def test_from_invalid_json():
    with pytest.raises(ValueError):
        SchemeLoader.from_json("invalid json")

def test_missing_required_field():
    json_str = """
    [{
        "Name": "test",
        "Description": "Test description"
    }]
    """
    with pytest.raises(ValueError):
        SchemeLoader.from_json(json_str)

def test_from_file(tmp_path):
    test_file = tmp_path / "test.json"
    test_data = [{
        "Name": "filetest",
        "Description": "File test",
        "Path": "C:\\filetest.json"
    }]
    test_file.write_text(json.dumps(test_data))
    
    schemes = SchemeLoader.from_file(test_file)
    assert len(schemes) == 1
    assert schemes[0].Name == "filetest"

def test_load_to_clipboard(tmp_path, monkeypatch):
    test_file = tmp_path / "clipboard.json"
    test_data = [{
        "Name": "clip",
        "Description": "Clipboard test",
        "Path": "C:\\clip.json"
    }]
    test_file.write_text(json.dumps(test_data))
    
    clipboard_content = None
    
    def mock_copy(content):
        nonlocal clipboard_content
        clipboard_content = content
    
    monkeypatch.setattr("pyperclip.copy", mock_copy)
    
    SchemeLoader.load_to_clipboard(test_file)
    assert clipboard_content == json.dumps(test_data)