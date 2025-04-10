import pandas as pd
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

conn = sqlite3.connect("retail_data.db")
df_inventory = pd.read_sql_query("SELECT * FROM inventory", conn)
conn.close()

product_id = str(df_inventory["Product ID"].iloc[0])
warehouse_stock = {product_id: df_inventory["Stock Levels"].iloc[0]}


@app.route('/request_stock', methods=['POST'])
def handle_stock_request():
    data = request.get_json()
    item = data.get("item")
    quantity = int(data.get("quantity"))

    if item not in warehouse_stock:
        return jsonify({
            "status": "fail",
            "message": f"{item} not found in warehouse"
        }), 404

    if warehouse_stock[item] >= quantity:
        warehouse_stock[item] -= quantity
        return jsonify({
            "status": "success",
            "message": f"Sent {quantity} units of {item} to store",
            "remaining_stock": warehouse_stock[item]
        })
    else:
        return jsonify({
            "status": "fail",
            "message": "Not enough stock in warehouse"
        }), 400
if __name__ == '__main__':
    app.run(debug=True, port=5000)
