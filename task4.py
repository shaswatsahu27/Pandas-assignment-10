import pandas as pd

# ---- Task 4: Create a DataFrame ----

# Create a DataFrame
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

# 1. Print the DataFrame
print("Students DataFrame:")
print(df)

# 2. Print first 3 rows
print("\nFirst 3 Rows:")
print(df.head(3))

# 3. Print last 2 rows
print("\nLast 2 Rows:")
print(df.tail(2))

# 4. Print DataFrame shape
print("\nShape:", df.shape)

# 5. Print column names
print("Column Names:", df.columns.tolist())