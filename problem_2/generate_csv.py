import pandas as pd
import numpy as np

num_rows = 1000000  # tested for 2.08 GB data of 8000000000 rows

# Define a manageable range of dates
start_date = pd.to_datetime('1950-01-01')
end_date = pd.to_datetime('2023-12-31')
date_range = pd.date_range(start=start_date, end=end_date)

# Sample dates from the range
dates = np.random.choice(date_range, size=num_rows)

# Convert dates to strings
dates_str = pd.Series(dates).dt.strftime('%Y-%m-%d').tolist()

# Generate sample data
data = {
    'first_name': np.random.choice(['John', 'Jane', 'Alice', 'Bob', 'Charlie'], num_rows),
    'last_name': np.random.choice(['Smith', 'Doe', 'Johnson', 'Williams', 'Brown'], num_rows),
    'address': np.random.choice(['123 Elm St', '456 Oak Ave', '789 Pine Rd', '101 Maple Dr', '202 Birch Blvd'], num_rows),
    'date_of_birth': dates_str
}

df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)
