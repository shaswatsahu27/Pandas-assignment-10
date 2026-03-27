import pandas as pd

# ---- Task 7: Grouping & Basic Analysis ----

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
df = pd.DataFrame(students)

# 1. Find average marks per subject using groupby()
print("Average Marks per Subject:")
print(df.groupby('Subject')['Marks'].mean())

# 2. Count number of students per subject
print("\nNumber of Students per Subject:")
print(df.groupby('Subject')['Name'].count())

# 3. Find maximum marks per subject
print("\nMaximum Marks per Subject:")
print(df.groupby('Subject')['Marks'].max())