# Vibe KPI Demo - Applied Analytics Mini Project

A beginner-friendly analytics project demonstrating ETL, SQL queries, and security best practices.

## Project Structure
```
vibe-kpi-demo/
├── data/
│   ├── raw/
│   │   └── customers_raw.csv      # Sample customer data
│   └── db/
│       └── analytics.db           # SQLite database (auto-generated)
├── src/
│   ├── etl_load_sqlite.py         # ETL script to load CSV into SQLite
│   └── kpi_city.py               # KPI calculation with SQL injection protection
├── tests/
│   └── test_kpi_city.py          # Pytest tests for KPI functions
├── requirements.txt               # Python dependencies
└── .gitignore                    # Git ignore rules
```

## Setup Instructions

### Prerequisites
- Python 3.7+ installed
- Virtual environment created and activated

### Installation & Run Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Load CSV data into SQLite database
python src/etl_load_sqlite.py

# Run KPI analysis (demonstrates SQL injection protection)
python src/kpi_city.py

# Run tests
pytest tests/ -v
```

## Features
- **ETL Pipeline**: Load CSV data into SQLite database
- **KPI Analytics**: Calculate city-level metrics (total customers, average spend, churn rate)
- **SQL Injection Protection**: Uses parameterized queries to prevent attacks
- **Testing**: Pytest suite with happy path and security tests

## Security Notes
- Uses parameterized SQL queries (`WHERE city = ?`) to prevent SQL injection
- Database files are excluded from Git via .gitignore
- No hardcoded credentials or sensitive data in code
