import pytest
from order_pipeline.pipeline import Pipeline

@pytest.fixture
def sample_json(tmp_path):
    """Create temporary input JSON file for integration test."""
    data = [
        {"order_id": 1, "timestamp": "2025-10-23", "item": "Phone",
         "quantity": 2, "price": 300, "total": 600, "payment_status": "paid"}
    ]
    file_path = tmp_path / "orders.json"
    import json
    with open(file_path, "w") as f:
        json.dump(data, f)
    return file_path

def test_pipeline_runs_end_to_end(sample_json):
    """Pipeline should execute all stages and return summary."""
    pipeline = Pipeline(str(sample_json))
    summary = pipeline.run()
    assert "total_sales" in summary
    assert summary["total_sales"] == 600
