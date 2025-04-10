import pandas as pd
import sqlite3
from flask import Flask, jsonify
import numpy as np
from ollama_tools import LLMQueryAgent
from forecast_agent import DemandForecastingAgent

app = Flask(__name__)

class PricingAgent:
    def __init__(self): 
        conn = sqlite3.connect("retail_data.db")
        df_pricing = pd.read_sql_query("SELECT * FROM pricing", conn)
        conn.close()
        self.df = df_pricing

        self.llm = LLMQueryAgent()

    def get_llm_suggestion(self, prompt = None):
        if not prompt:
            prompt = input("Enter a pricing question: ")
        return self.llm.query(prompt)
        

    #calculate how good pricing is compared to competitors by how much is the difference in pricing and bonus points for the discount
    def score_price_effectiveness(self):
        df = self.df
        score = (
            (df["Competitor Prices"] - df["Price"]) + df["Discounts"] * 10
        )
        return score.mean()
    
    def adjusted_restock_quantity(self):
        price_score = self.score_price_effectiveness()
        forecaster = DemandForecastingAgent()
        predicted_demand = forecaster.predict_demand()

        if price_score > 5:
            return int(predicted_demand * 1.2)
        elif price_score < 0:
            return int(predicted_demand * 0.8)
        else:
            return predicted_demand
        
@app.route("/get_pricing_recommendation", methods = ['POST'])
def get_pricing_recommendation():
    agent = PricingAgent()
    quantity = agent.adjusted_restock_quantity()
    score = agent.score_price_effectiveness()
    return jsonify({
        "adjusted_restock_quantity": quantity,
        "score": score
    })
        
if __name__ == "__main__":
    app.run(port=5003)