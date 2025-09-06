import pandas as pd

# Create a DataFrame (table-like structure)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [85, 90, 95]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

 
# Access column
print("Names:", df['Name'])

# Filter rows
print("Scores above 90:")
print(df[df['Score'] > 90]) 
 
