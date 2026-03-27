import pandas as pd

# ---- Task 2: Mathematical Operations on Series ----

marks = pd.Series([78, 85, 90, 66, 72])

# 1. Add 5 grace marks to all students
grace_marks = marks + 5
print("After adding 5 grace marks:")
print(grace_marks)

# 2. Subtract 2 marks from all values
subtract_marks = marks - 2
print("\nAfter subtracting 2 marks:")
print(subtract_marks)

# 3. Multiply all marks by 1.05
scaled_marks = marks * 1.05
print("\nAfter multiplying by 1.05:")
print(scaled_marks)

# 4. Divide all marks by 2
half_marks = marks / 2
print("\nAfter dividing by 2:")
print(half_marks)