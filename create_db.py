import pandas as pd
import sqlite3

inventory_df = pd.read_csv("inventory_monitoring.csv")
pricing_df = pd.read_csv("pricing_optimization.csv")
demand_df = pd.read_csv("demand_forecasting.csv")

conn = sqlite3.connect("retail_data.db")

inventory_df.to_sql("inventory", conn, if_exists="replace", index=False)
pricing_df.to_sql("pricing", conn, if_exists="replace", index=False)
demand_df.to_sql("demand", conn, if_exists="replace", index=False)

conn.close()
print("retail_data.db created successfully.")
