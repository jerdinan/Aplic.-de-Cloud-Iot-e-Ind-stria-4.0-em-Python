"""
Store Management System

This module provides endpoints for managing inventory, sales, and debtors using Flask.
"""

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

class StoreData:
    """
    A class to handle store data including inventory, sales, and debtors.
    """
    def __init__(self):
        self.inventory = pd.DataFrame(columns=["id", "product_name", "quantity"])
        self.sales = pd.DataFrame(columns=["id", "product_name", "quantity_sold"])
        self.debtors = pd.DataFrame(columns=["id", "customer_name", "amount_due"])

store_data = StoreData()

@app.route('/')
def home():
    """
    Home route that returns a welcome message.
    """
    return "Bem-vindo"

@app.route('/add_product', methods=['POST'])
def add_product():
    """
    Add a product to the inventory.

    Returns:
        JSON: The updated inventory.
    """
    data = request.get_json()
    store_data.inventory = store_data.inventory.append(data, ignore_index=True)
    return jsonify(store_data.inventory.to_dict(orient='records')), 201

@app.route('/record_sale', methods=['POST'])
def record_sale():
    """
    Record a sale in the sales data.

    Returns:
        JSON: The updated sales data.
    """
    data = request.get_json()
    store_data.sales = store_data.sales.append(data, ignore_index=True)
    return jsonify(store_data.sales.to_dict(orient='records')), 201

@app.route('/add_debtor', methods=['POST'])
def add_debtor():
    """
    Add a debtor to the debtors list.

    Returns:
        JSON: The updated debtors list.
    """
    data = request.get_json()
    store_data.debtors = store_data.debtors.append(data, ignore_index=True)
    return jsonify(store_data.debtors.to_dict(orient='records')), 201

@app.route('/get_inventory', methods=['GET'])
def get_inventory():
    """
    Retrieve the current inventory data.
    
    Returns:
        JSON: The current inventory data.
    """
    return jsonify(store_data.inventory.to_dict(orient='records')), 200

@app.route('/get_sales', methods=['GET'])
def get_sales():
    """
    Retrieve the current sales data.
    
    Returns:
        JSON: The current sales data.
    """
    return jsonify(store_data.sales.to_dict(orient='records')), 200

@app.route('/get_debtors', methods=['GET'])
def get_debtors():
    """
    Retrieve the current debtors data.
    
    Returns:
        JSON: The current debtors data.
    """
    return jsonify(store_data.debtors.to_dict(orient='records')), 200

if __name__ == '__main__':
    app.run(debug=True)
