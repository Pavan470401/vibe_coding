import sqlite3

def city_kpi(city: str):
    """Calculate KPIs for a specific city with SQL injection protection"""
    conn = sqlite3.connect('data/db/analytics.db')
    cursor = conn.cursor()
    
    # Parameterized query prevents SQL injection
    query = """
    SELECT 
        city,
        COUNT(*) as total_customers,
        AVG(monthly_spend) as avg_monthly_spend,
        SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) as churned_customers,
        ROUND(SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as churn_rate_pct
    FROM customers_raw 
    WHERE city = ?
    GROUP BY city
    """
    
    cursor.execute(query, (city,))
    result = cursor.fetchone()
    
    if result:
        city_name, total_customers, avg_spend, churned_customers, churn_rate = result
        print(f"\n=== KPI Report for {city_name} ===")
        print(f"Total Customers: {total_customers}")
        print(f"Average Monthly Spend: ${avg_spend:.2f}")
        print(f"Churned Customers: {churned_customers}")
        print(f"Churn Rate: {churn_rate}%")
    else:
        print(f"\nNo data found for city: {city}")
    
    conn.close()

if __name__ == "__main__":
    # Normal query
    city_kpi("Mumbai")
    
    # SQL injection attempt (should fail safely)
    city_kpi("Mumbai' OR 1=1 --")
