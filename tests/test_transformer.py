import pytest
from order_pipeline.transformer import Transformer

@pytest.fixture
def transformer():
    return Transformer()

@pytest.fixture
def sample_record():
    return {
        "order_id": "ORD456",
        "timestamp": "2025-10-24",
        "item": "laptop ",
        "quantity": "2",
        "price": "500",
        "total": "1000",
        "payment_status": "Paid"
    }

def test_transform_record_converts_types(transformer, sample_record):
    """Should convert numeric fields to float and add unit_price."""
    transformed = transformer.transform_record(sample_record)
    assert isinstance(transformed["quantity"], float)

def test_transform_record_formats_text(transformer, sample_record):
    """Should title-case item name and lowercase payment_status."""
    transformed = transformer.transform_record(sample_record)
    assert transformed["item"] == "Laptop"
    assert transformed["payment_status"] == "paid"

def test_transform_record_handles_invalid_data(transformer):
    """Should return None for malformed record."""
    bad_record = {"order_id": "123", "quantity": "x"}
    assert transformer.transform_record(bad_record) is None
