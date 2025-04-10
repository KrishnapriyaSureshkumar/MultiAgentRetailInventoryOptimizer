import requests
import sqlite3
import pandas as pd
from forecast_agent import DemandForecastingAgent

conn = sqlite3.connect("retail_data.db")
df_inventory = pd.read_sql_query("SELECT * FROM inventory", conn)
conn.close()

product_id = str(df_inventory["Product ID"].iloc[0])

class StoreAgent:
    def __init__(self):
        self.store_stock = {product_id: 95}  
        self.forecaster = DemandForecastingAgent()

    def check_and_request_stock(self):
        if self.store_stock[product_id] < 100:
            print("Store: Stock is low.")

            try:
                pricing_response = requests.get("http://127.0.0.1:5003/get_pricing_recommendation")
                pricing_data = pricing_response.json()
                adjusted_demand = int(pricing_data["adjusted_restock_quantity"])
                print(f"Recommended restock qty based on sales data: {adjusted_demand}")

                response = requests.post(
                    "http://127.0.0.1:5000/request_stock",
                    json = {
                        "item": str(product_id),
                        "quantity": adjusted_demand
                    }
                )
                print("Response from warehouse:", response.json())

            except Exception as e:
                print("Failed to contact pricing agent or warehouse", e)
        else:
            print("Stock level is sufficient.")

if __name__ == '__main__':
    store = StoreAgent()
    store.check_and_request_stock()
