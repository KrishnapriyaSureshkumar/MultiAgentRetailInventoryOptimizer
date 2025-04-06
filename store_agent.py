import requests
import pandas as pd
from forecast_agent import DemandForecastingAgent

# Load inventory data to extract product ID
df_inventory = pd.read_csv("inventory_monitoring.csv")
product_id = str(df_inventory["Product ID"].iloc[0])

class StoreAgent:
    def __init__(self):
        self.store_stock = {product_id: 5}  # Simulated store stock
        self.forecaster = DemandForecastingAgent()

    def check_and_request_stock(self):
        if self.store_stock[product_id] < 10:
            print("Store: Stock is low. Forecasting demand...")
            predicted_demand = int(self.forecaster.predict_demand())  # Convert to Python int
            print(f"Predicted demand based on sales data: {predicted_demand}")
            print(f"Store: Predicted demand is {predicted_demand}, requesting restock.")

            response = requests.post(
                "http://127.0.0.1:5000/request_stock",
                json={"item": str(product_id), "quantity": int(predicted_demand)}
            )
            print("Response from Warehouse:", response.json())
        else:
            print("Store: Stock level is sufficient.")

if __name__ == '__main__':
    store = StoreAgent()
    store.check_and_request_stock()
