# Day 1: Setup & Load Data
import pandas as pd #[cite: 2]

# Load the dataset
df = pd.read_csv('sales_data.csv') #[cite: 2]

# Day 2: Explore Data
print("--- Data Exploration ---")
# Check shape, columns, and data types[cite: 2]
print(f"Dataset Shape: {df.shape}") 
print("\nData Types:")
print(df.dtypes)
# Display the first few rows[cite: 1]
print("\nFirst 5 rows:")
print(df.head())

# Day 3: Clean Data
print("\n--- Data Cleaning ---")
# Find and handle missing values appropriately[cite: 1, 2]
# Using .dropna() as a foundational method to remove incomplete rows
df = df.dropna() 
# Remove duplicate entries[cite: 2]
df = df.drop_duplicates()
print("Missing values and duplicates handled.")

# Day 4: Analyze Sales
print("\n--- Sales Analysis ---")
# Calculate total revenue using the provided sample code[cite: 2]
total_revenue = df['Total_Sales'].sum() #[cite: 2]
print(f'Total Revenue: ₹{total_revenue:,.2f}') #[cite: 2]

# Calculate at least 3 different metrics: average, highest, and lowest values[cite: 1, 2]
average_sales = df['Total_Sales'].mean()
max_sales = df['Total_Sales'].max()
min_sales = df['Total_Sales'].min()

print(f'Average Sale: ₹{average_sales:,.2f}')
print(f'Highest Sale: ₹{max_sales:,.2f}')
print(f'Lowest Sale: ₹{min_sales:,.2f}')

# Find the best-selling product[cite: 1, 2]
# (Assuming a 'Product' column exists based on standard sales datasets)
if 'Product' in df.columns:
    best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
    print(f'Best-Selling Product: {best_product}')
    
    