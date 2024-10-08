import pandas as pd
import os

# Define the file path for the CSV file
file_path = 'C:\AIML\database.csv'  # Update the path as needed

# Verify if the file exists before proceeding
if os.path.exists(file_path):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(file_path)
    
    # Show details about the dataset
    print(f"Total rows: {df.shape[0]}")     # Display number of rows
    print(f"Total columns: {df.shape[1]}")  # Display number of columns

    # Show the first 5 rows of the dataset
    print("\nFirst 5 entries:\n", df.head())
    
    # Display the total size of the dataset
    print(f"\nDataset size: {df.size}")
    
    # Check for missing values in each column
    print("\nMissing values per column:\n", df.isnull().sum())

    # Generate summary statistics for numeric columns
    print("\nSum of numeric columns:\n", df.sum(numeric_only=True))
    print("\nAverage of numeric columns:\n", df.mean(numeric_only=True))
    print("\nMinimum values in numeric columns:\n", df.min(numeric_only=True))
    print("\nMaximum values in numeric columns:\n", df.max(numeric_only=True))

    # Export the modified dataset to a new CSV file
    df.to_csv('output.csv', index=False)
    print("\nDataset successfully exported to 'output.csv'")
else:
    print(f"Error: The file '{file_path}' could not be found.")
