import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime, timedelta

# Load the machine learning model
model = pickle.load(open('sales_prediction_model.pkl', 'rb'))

# Load the product data
df = pd.read_csv('ProductData.csv')

# Function to predict sales after a month and a year
def predict_sales(df, product_id, quantity, product_cost, sell_price):
    # Assume sales prediction model predicts sales directly based on provided features
    prediction_month = model.predict([[product_id, quantity, product_cost, sell_price]])[0]
    prediction_year = prediction_month * 12  # Assuming constant monthly sales over a year
    return prediction_month, prediction_year

# Function to calculate financial insights
def calculate_financial_insights(df, product_cost, sell_price):
    total_cost = product_cost * df['Quantity'].sum()
    total_earnings = sell_price * df['Quantity'].sum()
    total_profit = total_earnings - total_cost
    total_loss = 0  # Assuming there's no loss for now
    return total_profit, total_earnings, total_loss

# Display the title
st.title("PRODUCT SALES ANALYSIS")

# User input form
st.header('Input Parameters')
product_id = st.number_input('Product ID')
quantity = st.number_input('Quantity', min_value=0, step=1)
product_cost = st.number_input('Product Cost (in rupees)', min_value=0, step=1)
sell_price = st.number_input('Sell Price (in rupees)', min_value=0, step=1)
submit_button = st.button('Generate Report')

# Generate report
if submit_button:
    st.header('Report')
    
    # Predict sales after a month and a year
    sales_month, sales_year = predict_sales(df, product_id, quantity, product_cost, sell_price)
    st.subheader('Sales Prediction')
    st.write(f'Sales after a month: {sales_month}')
    st.write(f'Sales after a year: {sales_year}')
    
    # Calculate financial insights
    total_profit, total_earnings, total_loss = calculate_financial_insights(df, product_cost, sell_price)
    st.subheader('Financials')
    st.write(f'Total Profit: {total_profit}')
    st.write(f'Total Earnings: {total_earnings}')
    st.write(f'Total Loss: {total_loss}')
