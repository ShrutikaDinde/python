import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Miami']
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:\n", df)

# Filter the DataFrame for people aged 25 or older
filtered_df = df[df['Age'] >= 25]
print("\nFiltered DataFrame (Age >= 25):\n", filtered_df)



