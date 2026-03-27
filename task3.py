import pandas as pd

# ---- Task 3: Python Functionalities on Series ----

marks = pd.Series([78, 85, 90, 66, 72])

# 1. Find Maximum marks
print("Maximum Marks:", marks.max())

# 2. Find Minimum marks
print("Minimum Marks:", marks.min())

# 3. Find Sum of marks
print("Sum of Marks:", marks.sum())

# 4. Find Mean marks
print("Mean Marks:", marks.mean())

# 5. Apply a lambda function to check whether each student has passed (>= 70)
passed = marks.apply(lambda x: "Pass" if x >= 70 else "Fail")
print("\nPass/Fail Status:")
print(passed)

# 6. Count how many students passed
pass_count = (marks >= 70).sum()
print("\nNumber of Students Passed:", pass_count)