# Core Testing Pipeline

A modular Python project for testing and validating a complete **data processing pipeline**  from reading raw data to exporting clean analytical results.  
This project demonstrates the use of **Pytest** for automated unit testing and **pytest-cov** for coverage tracking across multiple pipeline stages.

---

##  Project Structure

coretesting/
│
├── order_pipeline/
│   ├── __init__.py
│   ├── reader.py      # Reads and validates JSON input files
│   ├── validator.py   # Validates structure, data types, and logic of records
│   ├── transformer.py # Cleans, normalizes, and computes derived values
│   ├── analyzer.py    # Performs analytical summaries and grouping
│   ├── exporter.py    # Exports processed data to JSON/CSV
│   └── pipeline.py    # Orchestrates the full pipeline process
│
└── tests/
    ├── test_reader.py
    ├── test_validator.py
    ├── test_transformer.py
    ├── test_analyzer.py
    ├── test_exporter.py
    └── test_pipeline.py
---

##  Key Features

- **End-to-End Data Pipeline**
  - Reads, validates, transforms, analyzes, and exports data.
- **Comprehensive Unit Testing**
  - Each module has corresponding tests under `tests/`.
- **High Test Coverage**
  - Achieves over **95% coverage** across all modules with `pytest-cov`.
- **Robust Validation**
  - Detects missing fields, wrong data types, invalid totals, and more.
- **Scalable Design**
  - Each component can run independently or be integrated via `pipeline.py`.

---

##  Modules Overview

| Module | Responsibility |
|--------|----------------|
| **reader.py** | Reads JSON files and ensures valid format (list of dictionaries). |
| **validator.py** | Checks for missing or invalid data and enforces logical consistency. |
| **transformer.py** | Cleans and computes derived values such as revenue or normalized fields. |
| **analyzer.py** | Summarizes key metrics (total sales, averages, top items). |
| **exporter.py** | Saves the processed data into new formats (JSON, CSV). |
| **pipeline.py** | Coordinates the execution of all modules to process a dataset from start to finish. |

---

##  Running Tests

To execute all tests:
```bash
python -m pytest
```
To run with coverage reporting:
```bash
python -m pytest --cov=order_pipeline --cov-report=term-missing
```

