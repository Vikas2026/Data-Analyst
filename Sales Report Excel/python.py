# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the number of rows
num_rows = 1500

# Define sample data
products = ['OnePlus', 'iPhone', 'Oppo', 'Samsung', 'Realme']
categories = ['Cheap', 'Average', 'Costly']
sales_reps = ['Vikas', 'Sakiv', 'Zoro', 'Luffy', 'Chopper']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Generate data
data = {
    'Date': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_rows)],
    'Product': [random.choice(products) for _ in range(num_rows)],
    'Category': [random.choice(categories) for _ in range(num_rows)],
    'Sales Rep': [random.choice(sales_reps) for _ in range(num_rows)],
    'City': [random.choice(cities) for _ in range(num_rows)],
    'Price': [random.randint(10000, 150000) for _ in range(num_rows)],
    'Number of Units': [random.randint(1, 5) for _ in range(num_rows)]
}

data['Amount'] = [data['Price'][i] * data['Number of Units'][i] for i in range(num_rows)]
# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('sales_data.xlsx', index=False)

# Display the first few rows
print(df.head())
