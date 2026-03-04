import pytest
import sqlite3
import pandas as pd
import os
import sys

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from kpi_city import city_kpi

@pytest.fixture
def setup_test_db():
    """Setup test database with sample data"""
    # Ensure test db directory exists
    os.makedirs('data/db', exist_ok=True)
    
    # Create test data
    test_data = pd.DataFrame({
        'customer_id': [1, 2, 3, 4, 5],
        'city': ['Mumbai', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi'],
        'monthly_spend': [100.0, 200.0, 150.0, 300.0, 120.0],
        'churned': [0, 1, 0, 0, 1]
    })
    
    # Load to test database
    conn = sqlite3.connect('data/db/analytics.db')
    test_data.to_sql('customers_raw', conn, if_exists='replace', index=False)
    conn.close()
    
    yield
    
    # Cleanup (optional)
    if os.path.exists('data/db/analytics.db'):
        os.remove('data/db/analytics.db')

def test_city_kpi_happy_path(setup_test_db, capsys):
    """Test normal city KPI calculation"""
    city_kpi("Mumbai")
    
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify Mumbai KPIs are calculated correctly
    assert "KPI Report for Mumbai" in output
    assert "Total Customers: 3" in output
    assert "Average Monthly Spend: $200.00" in output
    assert "Churned Customers: 1" in output
    assert "Churn Rate: 33.33%" in output

def test_city_kpi_injection_attempt(setup_test_db, capsys):
    """Test SQL injection attempt fails safely"""
    city_kpi("Mumbai' OR 1=1 --")
    
    captured = capsys.readouterr()
    output = captured.out
    
    # Should return no data for injection attempt
    assert "No data found for city: Mumbai' OR 1=1 --" in output
    # Should NOT return all customers data
    assert "KPI Report for Mumbai" not in output
    assert "Total Customers: 5" not in output
