import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Load the product sales data
df = pd.read_csv('ProductData.csv')

# Function to calculate total profit, total loss, and total earnings
def calculate_profit_loss(data):
    today = datetime.now().strftime("%Y-%m-%d")
    today_data = data[data['Sales Date'] == today]
    today_data['Total'] = today_data['Quantity'] * today_data['Sell Price (in rupees)']
    total_profit = today_data[today_data['Total'] > 0]['Total'].sum()
    total_loss = today_data[today_data['Total'] < 0]['Total'].sum()
    total_earnings = today_data['Total'].sum()
    
    return total_profit, total_loss, total_earnings

# Display the image and title side by side
col1, col2 = st.columns([1, 3])
col1.image('sales.jpg', width=150)
col2.title("PRODUCT SALES ANALYSIS")

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
    
    # Calculate total profit, total loss, and total earnings
    total_profit, total_loss, total_earnings = calculate_profit_loss(df)
    st.subheader('Financials')
    st.write(f'Today\'s Total Profit: {total_profit}')
    st.write(f'Today\'s Total Loss: {total_loss}')
    st.write(f'Total Earnings: {total_earnings}')
