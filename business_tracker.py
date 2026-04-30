import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [50000, 62000, 58000, 70000],
    "Expenses": [30000, 35000, 32000, 40000]
}

df = pd.DataFrame(data)
df["Profit"] = df["Sales"] - df["Expenses"]

print("Business Report:")
print(df)

print("\nTotal Profit:", df["Profit"].sum())