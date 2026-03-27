import pandas as pd

# ---- Task 5: Important DataFrame Functions ----

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
df = pd.DataFrame(students)

# 1. .info()
print("DataFrame Info:")
print(df.info())

# 2. .describe()
print("\nDescribe:")
print(df.describe())

# 3. .head()
print("\nHead (default 5 rows):")
print(df.head())

# 4. .tail()
print("\nTail (default 5 rows):")
print(df.tail())

# 5. Sort students by Marks in descending order
sorted_df = df.sort_values(by='Marks', ascending=False)
print("\nSorted by Marks (Descending):")
print(sorted_df)

# 6. Reset index after sorting
sorted_df = sorted_df.reset_index(drop=True)
print("\nAfter Resetting Index:")
print(sorted_df)