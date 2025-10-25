import pytest
import os
import json
from order_pipeline.exporter import Exporter

@pytest.fixture
def exporter(tmp_path):
    """Use a temporary folder so tests don’t write to disk permanently."""
    return Exporter(output_dir=tmp_path)

@pytest.fixture
def sample_data():
    return [{"id": 1, "name": "Laptop", "price": 1200.5}]

def test_export_to_json_creates_file(exporter, sample_data):
    exporter.export_to_json(sample_data, "test.json")
    assert (exporter.output_dir / "test.json").exists()

def test_export_to_json_content_is_correct(exporter, sample_data):
    file_path = exporter.output_dir / "test.json"
    exporter.export_to_json(sample_data, "test.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    assert data[0]["name"] == "Laptop"

def test_export_to_csv_creates_file(exporter, sample_data):
    exporter.export_to_csv(sample_data, "test.csv")
    assert (exporter.output_dir / "test.csv").exists()
