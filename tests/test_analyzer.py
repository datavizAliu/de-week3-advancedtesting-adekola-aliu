import pytest
from order_pipeline.analyzer import Analyzer

@pytest.fixture
def sample_data():
    return [
        {"item": "Laptop", "total": 1000, "payment_status": "paid"},
        {"item": "Phone", "total": 500, "payment_status": "pending"},
        {"item": "Laptop", "total": 1500, "payment_status": "paid"}
    ]

def test_total_sales(sample_data):
    analyzer = Analyzer(sample_data)
    assert analyzer.total_sales() == 3000

def test_average_order_value(sample_data):
    analyzer = Analyzer(sample_data)
    assert round(analyzer.average_order_value(), 2) == 1000.0

def test_sales_by_status(sample_data):
    analyzer = Analyzer(sample_data)
    result = analyzer.sales_by_status()
    assert result["paid"] == 2500
    assert result["pending"] == 500

def test_top_items(sample_data):
    analyzer = Analyzer(sample_data)
    top = analyzer.top_items(1)
    assert top[0][0] == "Laptop"
    assert top[0][1] == 2
