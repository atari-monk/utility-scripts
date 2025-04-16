import pytest
import json
from core.info import CliScriptsInfo

def test_valid_cli_scripts_info():
    data = [{"CliName": "test", "Description": "Test description"}]
    scripts = [CliScriptsInfo(**item) for item in data]
    assert scripts[0].CliName == "test"
    assert scripts[0].Description == "Test description"

def test_invalid_cliname_length():
    with pytest.raises(ValueError):
        CliScriptsInfo(CliName="toolong", Description="Valid")

def test_invalid_description_length():
    with pytest.raises(ValueError):
        CliScriptsInfo(CliName="test", Description="x" * 301)

def test_load_from_json(tmp_path):
    json_data = [{"CliName": "load", "Description": "Loading test"}]
    file_path = tmp_path / "test.json"
    file_path.write_text(json.dumps(json_data))
    
    loaded = CliScriptsInfo.load_from_json(file_path)
    assert len(loaded) == 1
    assert loaded[0].CliName == "load"

def test_to_string():
    data = [CliScriptsInfo(CliName="prnt", Description="Print test")]
    output = CliScriptsInfo.to_string(data)
    assert "prnt" in output
    assert "Print test" in output