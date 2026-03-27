import pandas as pd

# ---- Task 8: Pandas Plotting (Simple Graphs) ----

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
df = pd.DataFrame(students)

# 1. Plot a bar graph of student names vs marks
df.plot(x='Name', y='Marks', kind='bar', title='Student Marks (Bar Chart)')

# 2. Plot a line graph of marks
df['Marks'].plot(kind='line', title='Student Marks (Line Graph)', marker='o')

# 3. Plot a histogram of marks
df['Marks'].plot(kind='hist', title='Marks Distribution (Histogram)', bins=5)

# Note: Use only DataFrame.plot() and Series.plot()
# No matplotlib customization required.
print("Plots generated successfully!")
print("Note: Graphs will appear in separate windows when running locally.")