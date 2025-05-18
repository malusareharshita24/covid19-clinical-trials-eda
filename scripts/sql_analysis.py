
import pandas as pd
import sqlite3

# Load CSV data
df = pd.read_csv('data/COVID clinical trials.csv')

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Load data into SQL table
df.to_sql('clinical_trials', conn, index=False, if_exists='replace')

# 1. Total number of trials
print("1. Total number of trials:")
print(pd.read_sql("SELECT COUNT(*) AS total_trials FROM clinical_trials", conn))

# 2. Trials by study type
print("\n2. Trials by study type:")
print(pd.read_sql("""
SELECT [Study Type], COUNT(*) AS count 
FROM clinical_trials 
GROUP BY [Study Type]
ORDER BY count DESC
""", conn))

# 3. Number of COVID-related trials
print("\n3. COVID-related trials:")
print(pd.read_sql("""
SELECT COUNT(*) AS covid_trials 
FROM clinical_trials 
WHERE Title LIKE '%COVID%'
""", conn))

# 4. Top 10 locations by number of trials
print("\n4. Top 10 trial locations:")
print(pd.read_sql("""
SELECT Location, COUNT(*) AS count 
FROM clinical_trials 
GROUP BY Location 
ORDER BY count DESC 
LIMIT 10
""", conn))

conn.close()
