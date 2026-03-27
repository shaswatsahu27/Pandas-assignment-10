import pandas as pd

# ---- Task 9: Mini Use Case - Sales Data Analysis ----

# Create a DataFrame
sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}
df = pd.DataFrame(sales)

print("Sales DataFrame:")
print(df)

# 1. Total revenue
total = df['Revenue'].sum()
print(f"\nTotal Weekly Revenue: {total}")

# 2. Average daily revenue
avg = df['Revenue'].mean()
print(f"Average Daily Revenue: {avg}")

# 3. Day with highest revenue
max_day = df.loc[df['Revenue'].idxmax(), 'Day']
max_rev = df['Revenue'].max()
print(f"Day with Highest Revenue: {max_day} (Revenue: {max_rev})")

# 4. Days where revenue > average
print(f"\nDays with Revenue > Average ({avg}):")
print(df[df['Revenue'] > avg])

# 5. Plot revenue vs day
df.plot(x='Day', y='Revenue', kind='bar', title='Daily Revenue')
print("\nRevenue vs Day plot generated successfully!")