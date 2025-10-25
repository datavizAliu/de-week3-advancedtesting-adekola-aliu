import pytest
from order_pipeline.reader import Reader
import json
import os

@pytest.fixture
def reader():
    return Reader()

@pytest.fixture
def valid_json_file(tmp_path):
    """Create a temporary valid JSON file."""
    sample_data = [{"order_id": 1, "item": "Phone"}]
    file_path = tmp_path / "valid.json"
    with open(file_path, "w") as f:
        json.dump(sample_data, f)
    return file_path


@pytest.fixture
def empty_json_file(tmp_path):
    """Create an empty JSON file."""
    file_path = tmp_path / "empty.json"
    with open(file_path, "w") as f:
        f.write("[]")
    return file_path


@pytest.fixture
def invalid_json_file(tmp_path):
    """Create a JSON file with invalid JSON content."""
    file_path = tmp_path / "invalid.json"
    with open(file_path, "w") as f:
        f.write("{invalid_json: true,}")  # corrupt JSON
    return file_path


@pytest.fixture
def wrong_format_json_file(tmp_path):
    """Create a JSON file with wrong structure (dict instead of list)."""
    file_path = tmp_path / "wrong_format.json"
    with open(file_path, "w") as f:
        json.dump({"order_id": 1, "item": "Phone"}, f)
    return file_path


def test_read_json_valid_file(reader, valid_json_file):
    """read valid JSON successfully and return a list of dicts."""
    data = reader.read_json(valid_json_file)
    assert isinstance(data, list)
    assert isinstance(data[0], dict)
    assert data[0]["item"] == "Phone"


def test_read_json_file_not_found(reader):
    """Should raise ValueError if file path does not exist."""
    with pytest.raises(ValueError, match="File not found"):
        reader.read_json("non_existing_file.json")


def test_read_json_invalid_format(reader, invalid_json_file):
    """Should raise ValueError if JSON is invalid."""
    with pytest.raises(ValueError, match="Not valid JSON"):
        reader.read_json(invalid_json_file)


def test_read_json_empty_file(reader, empty_json_file):
    """Should raise ValueError if JSON is empty."""
    with pytest.raises(ValueError, match="File is empty"):
        reader.read_json(empty_json_file)


def test_read_json_wrong_format(reader, wrong_format_json_file):
    """Should raise ValueError if JSON is not a list of dicts."""
    with pytest.raises(ValueError, match="JSON format must be list of dictionaries"):
        reader.read_json(wrong_format_json_file)
