import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Load the product sales data
df = pd.read_csv('ProductData.csv')

def predict_sales(data, quantity_col, cost_col, price_col):
    # Predict sales after a month and a year
    today = datetime.today()
    one_month_later = today + timedelta(days=30)
    one_year_later = today + timedelta(days=365)
    
    # Filter data for predictions
    data_month = data[(data['Sales Date'] > today) & (data['Sales Date'] <= one_month_later)]
    data_year = data[(data['Sales Date'] > today) & (data['Sales Date'] <= one_year_later)]
    
    # Calculate predicted sales
    sales_month = (data_month[quantity_col] * data_month[price_col]).sum()
    sales_year = (data_year[quantity_col] * data_year[price_col]).sum()
    
    return sales_month, sales_year

def calculate_financials(data, quantity_col, cost_col, price_col):
    # Calculate total profit, total loss, and total earnings
    today = datetime.today().strftime("%Y-%m-%d")
    today_data = data[data['Sales Date'] == today]
    today_data['Total'] = today_data[quantity_col] * (today_data[price_col] - today_data[cost_col])
    
    total_profit = today_data[today_data['Total'] > 0]['Total'].sum()
    total_loss = today_data[today_data['Total'] < 0]['Total'].sum()
    total_earnings = today_data['Total'].sum()
    
    return total_profit, total_loss, total_earnings

# Display the title
st.title("Product Sales Analysis")

# User input form
st.header('Input Parameters')
product_id = st.number_input('Product ID')
product_name = st.text_input('Product Name')
product_description = st.text_area('Product Description')
quantity_type = st.selectbox('Quantity Type', ['Dozen', 'Feet', 'Galloon', 'Gram', 'Hours', 'Inch', 'Kilogram', 'Kilometer', 'Litre'])
sku = st.text_input('SKU')
quantity = st.number_input('Quantity', min_value=0, step=1)
product_cost = st.number_input('Product Cost (in rupees)', min_value=0, step=1)
sell_price = st.number_input('Sell Price (in rupees)', min_value=0, step=1)
submit_button = st.button('Generate Report')

# Generate report
if submit_button:
    st.header('Report')
    
    # Predict sales after a month and a year
    sales_month, sales_year = predict_sales(df, 'Quantity', 'Product Cost (in rupees)', 'Sell Price (in rupees)')
    st.subheader('Sales Prediction')
    st.write(f'Sales after a month: {sales_month}')
    st.write(f'Sales after a year: {sales_year}')
    
    # Calculate total profit, total loss, and total earnings
    total_profit, total_loss, total_earnings = calculate_financials(df, 'Quantity', 'Product Cost (in rupees)', 'Sell Price (in rupees)')
    st.subheader('Financials')
    st.write(f'Today\'s Total Profit: {total_profit}')
    st.write(f'Today\'s Total Loss: {total_loss}')
    st.write(f'Total Earnings: {total_earnings}')
