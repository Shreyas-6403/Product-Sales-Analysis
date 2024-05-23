import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Load the product sales data
df = pd.read_csv('ProductData.csv')

# Function to predict sales after a month and a year
def predict_sales(data, quantity_sold_col, sales_date_col):
    # Convert 'Sales Date' column to datetime
    data[sales_date_col] = pd.to_datetime(data[sales_date_col])
    
    # Calculate one month and one year from the last sales date
    last_date = data[sales_date_col].max()
    one_month_later = last_date + timedelta(days=30)
    one_year_later = last_date + timedelta(days=365)
    
    # Filter data for predictions
    data_month = data[data[sales_date_col] > last_date]
    data_year = data[data[sales_date_col] > last_date]
    
    # Predict sales after a month and a year
    sales_month = data_month[quantity_sold_col].sum()
    sales_year = data_year[quantity_sold_col].sum()
    
    return sales_month, sales_year

# Function to calculate total profit, total loss, and total earnings
def calculate_profit_loss(data, quantity_sold_col, unit_price_col):
    data['Total'] = data[quantity_sold_col] * data[unit_price_col]
    total_earnings = data['Total'].sum()
    today = datetime.now().strftime("%Y-%m-%d")
    today_data = data[data['Sales Date'] == today]
    total_profit = today_data[today_data['Total'] > 0]['Total'].sum()
    total_loss = today_data[today_data['Total'] < 0]['Total'].sum()
    
    return total_profit, total_loss, total_earnings

# Streamlit app layout
st.title('SALES ANALYSIS')

# Display the image
st.image('sales.jpg', width=100)

# User input form
st.header('Input Parameters')
product_id = st.number_input('Product ID')
product_name = st.text_input('Product Name')
product_description = st.text_area('Product Description')
quantity_type = st.selectbox('Quantity Type', ['None', 'Dozen', 'Feet', 'Galloon', 'Gram', 'Hours', 'Inch', 'Kilogram', 'Kilometer', 'Litre'], index=0)
sku = st.text_input('SKU')
quantity = st.number_input('Quantity', min_value=0, step=1)
product_cost = st.number_input('Product Cost (in rupees)', min_value=0, step=1)
sell_price = st.number_input('Sell Price (in rupees)', min_value=0, step=1)
submit_button = st.button('Generate Report')

# Generate report
if submit_button:
    st.header('Report')
    
    # Predict sales after a month and a year
    sales_month, sales_year = predict_sales(df, 'Quantity Sold', 'Sales Date')
    st.subheader('Sales Prediction')
    st.write(f'Sales after a month: {sales_month}')
    st.write(f'Sales after a year: {sales_year}')
    
    # Calculate total profit, total loss, and total earnings
    total_profit, total_loss, total_earnings = calculate_profit_loss(df, 'Quantity Sold', 'Unit Price')
    st.subheader('Financials')
    st.write(f'Today\'s Total Profit: {total_profit}')
    st.write(f'Today\'s Total Loss: {total_loss}')
    st.write(f'Total Earnings: {total_earnings}')
