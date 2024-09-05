import pandas as pd

# Loading the bank data from CSV file
df = pd.read_csv('data.csv', sep=';')

# Converting age column to numeric, coercing errors
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Displaying the first few rows to confirm that data has been loaded correctly
print(df.head())

# Validation: Checking if there are any missing values
if df.isnull().values.any():
    print("Data contains missing values!")
else:
    print("Data is valid with no missing values.")

if (df['age'] < 18).any() or (df['age'] > 100).any():
    print("Data contains invalid age values.")
else:
    print("All ages are within the valid range (18-100).")
    
# Validation: Checking for valid balance values (assuming balance should be non-negative)
if (df['balance'] < 0).any():
    print("Data contains invalid balance values (negative balances).")
else:
    print("All balances are non-negative.")

# Checking for duplicate entries based on 'age', 'job', 'marital', and 'education'
if df.duplicated(subset=['age', 'job', 'marital', 'education']).any():
    print("Data contains duplicate entries.")
else:
    print("No duplicate entries found.")

# Printing a summary of the data
print("Summary of Data:\n", df.describe(include='all'))
