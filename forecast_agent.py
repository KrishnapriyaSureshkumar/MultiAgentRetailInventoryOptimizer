import pandas as pd
import numpy as np
import sqlite3
from ollama_tools import LLMQueryAgent

class DemandForecastingAgent:
    def __init__(self):
        
        conn = sqlite3.connect("retail_data.db")
        df_demand = pd.read_sql_query("SELECT * FROM demand", conn)
        conn.close()
        self.sales_data = df_demand["Sales Quantity"]

        self.llm = LLMQueryAgent(model="phi")

    def predict_demand(self):
        predicted = int(np.mean(self.sales_data))
        print(f"Predicted demand based on sales data: {predicted}")
        return predicted
    
    def get_llm_suggestion(self, prompt=None):
        if not prompt:
            prompt = input("Enter a forecasting question: ")
        return self.llm.query(prompt)

if __name__ == "__main__":
    predictor = DemandForecastingAgent()
    predictor.predict_demand()