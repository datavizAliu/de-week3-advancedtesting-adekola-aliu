import pytest
from order_pipeline.reader import Reader

def test_read_json_valid_file():
    reader = Reader()
    path = '../shoplink.json'
    data = reader.read_json(path)
    assert isinstance(data,list)
    assert len(data) > 0
    assert all(isinstance(row, dict) for row in data)
