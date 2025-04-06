import pandas as pd
import numpy as np

class DemandForecastingAgent:
    def __init__(self):
        df_demand = pd.read_csv("demand_forecasting.csv")
        self.sales_data = df_demand["Sales Quantity"]

    def predict_demand(self):
        predicted = int(np.mean(self.sales_data))
        print(f"Predicted demand based on sales data: {predicted}")
        return predicted

if __name__ == "__main__":
    predictor = DemandForecastingAgent()
    predictor.predict_demand()