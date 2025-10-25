import pytest
from order_pipeline.validator import Validator

@pytest.fixture
def validator():
    return Validator()
@pytest.fixture
def valid_record():
    return {
        "order_id": "ORD001",
        "timestamp": "2025-10-24",
        "item": "Laptop",
        "quantity": 2,
        "price": 500.0,
        "total": 1000.0,
        "payment_status": "Paid"
    }

def test_valid_record_passes(validator, valid_record):
    assert validator.validate_record(valid_record) == True

# missing required field
def test_missing_feield_fails(validator, valid_record):
    del valid_record["item"]
    assert validator.validate_record(valid_record) == False

# Negative numeric value

def test_negative_quantity_fails(validator, valid_record):
    valid_record["quantity"] = -3
    assert validator.validate_record(valid_record) == False

# Inconsistence total

def test_inconsistence_total_fails(validator, valid_record):
    valid_record["total"] = 2000
    assert validator.validate_record(valid_record) == False

# invalid payment method

def test_invalid_payment_status_fails(validator, valid_record):
    valid_record["payment_status"] = "Completed"
    assert validator.validate_record(valid_record) == False

# Timestamp wrong format
def test_invalid_timestamp_fails(validator, valid_record):
    valid_record["timestamp"] = "20-10-2025"
    assert validator.validate_record(valid_record) == False

# Validate_all returns only valid records
def test_validate_all_returns_only_valid(validator, valid_record):
    bad_record = valid_record.copy()
    bad_record["quantity"] = -1
    data = [valid_record, bad_record]
    result = validator.validate_all(data)
    assert len(result) == 1
    assert result[0]["order_id"] == "ORD001"
