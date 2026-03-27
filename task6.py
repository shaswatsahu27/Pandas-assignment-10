import pandas as pd

# ---- Task 6: Filtering & Conditional Selection ----

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
df = pd.DataFrame(students)

# 1. Students who scored more than 75 marks
print("Students with Marks > 75:")
print(df[df['Marks'] > 75])

# 2. Students belonging to subject Math
print("\nMath Students:")
print(df[df['Subject'] == 'Math'])

# 3. Students who scored more than average marks
avg = df['Marks'].mean()
print(f"\nAverage Marks: {avg}")
print("Students above average:")
print(df[df['Marks'] > avg])

# 4. Students who failed (marks < 70)
print("\nFailed Students (Marks < 70):")
print(df[df['Marks'] < 70])