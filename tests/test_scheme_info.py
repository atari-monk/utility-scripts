import pytest
import json
import os
from tempfile import NamedTemporaryFile
import pyperclip
from core.scheme.scheme_info import SchemeInfo


def test_valid_scheme_info():
    valid_scheme = SchemeInfo(
        Name="validscheme",
        Description="A valid scheme description",
        Path=os.path.abspath(__file__),
    )
    assert valid_scheme.Name == "validscheme"
    assert valid_scheme.Description == "A valid scheme description"


def test_invalid_name():
    with pytest.raises(ValueError):
        SchemeInfo(
            Name="InvalidSchemeWithUpperCase",
            Description="Test",
            Path=os.path.abspath(__file__),
        )


def test_long_name():
    with pytest.raises(ValueError):
        SchemeInfo(Name="a" * 51, Description="Test", Path=os.path.abspath(__file__))


def test_long_description():
    with pytest.raises(ValueError):
        SchemeInfo(
            Name="validscheme", Description="a" * 301, Path=os.path.abspath(__file__)
        )


def test_invalid_path():
    with pytest.raises(ValueError):
        SchemeInfo(Name="validscheme", Description="Test", Path="/nonexistent/path")


def test_from_json_file():
    json_data = [
        {
            "Name": "testscheme",
            "Description": "Test description",
            "Path": os.path.abspath(__file__),
        }
    ]

    with NamedTemporaryFile(mode="w", delete=False) as f:
        json.dump(json_data, f)
        temp_path = f.name

    try:
        schemes = SchemeInfo.from_json_file(temp_path)
        assert len(schemes) == 1
        assert schemes[0].Name == "testscheme"
    finally:
        os.unlink(temp_path)


def test_load_and_copy_scheme(monkeypatch):
    test_content = "Test file content"
    with NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(test_content)
        temp_path = f.name

    try:
        scheme = SchemeInfo(Name="copytest", Description="Copy test", Path=temp_path)

        copied_content = None

        def mock_copy(content):
            nonlocal copied_content
            copied_content = content

        monkeypatch.setattr(pyperclip, "copy", mock_copy)

        SchemeInfo.load_and_copy_scheme([scheme], "copytest")
        assert copied_content == test_content
    finally:
        os.unlink(temp_path)


def test_load_nonexistent_scheme():
    scheme = SchemeInfo(
        Name="exists", Description="Test", Path=os.path.abspath(__file__)
    )
    with pytest.raises(ValueError):
        SchemeInfo.load_and_copy_scheme([scheme], "nonexistent")
