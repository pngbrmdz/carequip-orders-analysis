import pandas as pd

print("Loading orders data...")

df = pd.read_excel("orders_export_1.xlsx", sheet_name="orders_export_1")

print(f"Loaded {len(df)} rows of data")

print("\nDate range:", df["Created at"].min(), "to", df["Created at"].max())
print("Total value (AUD):", round(df["Total"].sum(), 2))

df.to_csv("orders_clean.csv", index=False)
print("\nSaved clean version as orders_clean.csv")
