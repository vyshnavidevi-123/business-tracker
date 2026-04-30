import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [50000, 62000, 58000, 70000, 75000, 80000],
    "Expenses": [30000, 35000, 32000, 40000, 42000, 45000]
}

df = pd.DataFrame(data)

# Calculate Profit
df["Profit"] = df["Sales"] - df["Expenses"]

# Calculate Profit Percentage
df["Profit %"] = (df["Profit"] / df["Sales"]) * 100

print("\n📊 Business Report\n")
print(df)

# Total Summary
total_sales = df["Sales"].sum()
total_expenses = df["Expenses"].sum()
total_profit = df["Profit"].sum()

print("\n📈 Summary")
print("Total Sales:", total_sales)
print("Total Expenses:", total_expenses)
print("Total Profit:", total_profit)

# Best Month
best_month = df.loc[df["Profit"].idxmax()]
print("\n🏆 Best Month:", best_month["Month"], "with profit", best_month["Profit"])

# Worst Month
worst_month = df.loc[df["Profit"].idxmin()]
print("⚠️ Worst Month:", worst_month["Month"], "with profit", worst_month["Profit"])


# GRAPH 1: Line Chart

plt.figure()
plt.plot(df["Month"], df["Sales"], marker="o", label="Sales")
plt.plot(df["Month"], df["Expenses"], marker="o", label="Expenses")
plt.plot(df["Month"], df["Profit"], marker="o", label="Profit")

plt.title("Business Performance Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.grid()


# GRAPH 2: Bar Chart

plt.figure()
plt.bar(df["Month"], df["Profit"])
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")


# GRAPH 3: Pie Chart

plt.figure()
plt.pie([total_sales, total_expenses],
        labels=["Sales", "Expenses"],
        autopct="%1.1f%%")
plt.title("Sales vs Expenses")

# To Show all graphs
plt.show()
