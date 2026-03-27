import pandas as pd

# ---- Task 1: Pandas Series Basics ----

# 1. Create a Pandas Series from the list
marks = [78, 85, 90, 66, 72]
series = pd.Series(marks)

# 2. Print the Series
print("Marks Series:")
print(series)

# 3. Print Series values
print("\nSeries Values:", series.values)

# 4. Print Index
print("Index:", series.index)

# 5. Print Data type
print("Data Type:", series.dtype)

# 6. Access first element
print("\nFirst Element:", series[0])

# 7. Access last two elements
print("Last Two Elements:")
print(series[-2:])