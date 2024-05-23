import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Initialize session state for storing product data
if 'products' not in st.session_state:
    st.session_state['products'] = []

def predict_sales(data, quantity_col, cost_col, price_col):
    # Predict sales after a month and a year
    today = datetime.today()
    one_month_later = today + timedelta(days=30)
    one_year_later = today + timedelta(days=365)
    
    # Filter data for predictions
    data['Date'] = pd.to_datetime(data['Date'])
    data_month = data[(data['Date'] > today) & (data['Date'] <= one_month_later)]
    data_year = data[(data['Date'] > today) & (data['Date'] <= one_year_later)]
    
    # Calculate predicted sales
    sales_month = (data_month[quantity_col] * data_month[price_col]).sum()
    sales_year = (data_year[quantity_col] * data_year[price_col]).sum()
    
    return sales_month, sales_year

def calculate_financials(data, quantity_col, cost_col, price_col):
    # Calculate total profit, total loss, and total earnings
    today = datetime.today().strftime("%Y-%m-%d")
    today_data = data[data['Date'] == today]
    today_data['Total'] = today_data[quantity_col] * (today_data[price_col] - today_data[cost_col])
    
    total_profit = today_data[today_data['Total'] > 0]['Total'].sum()
    total_loss = today_data[today_data['Total'] < 0]['Total'].sum()
    total_earnings = today_data['Total'].sum()
    
    return total_profit, total_loss, total_earnings

# Display image and title side by side
col1, col2 = st.columns([1, 3])
with col1:
    st.image("sales.jpg", use_column_width=True)
with col2:
    st.title("Product Sales Analysis")

# Add Product Data Button
add_product_button = st.button('Add Product Data')

if add_product_button:
    st.session_state['add_product'] = True

# Product addition form
if 'add_product' in st.session_state and st.session_state['add_product']:
    st.header('Add Product Details')
    
    product_id = st.number_input('Product ID', min_value=1, step=1)
    product_name = st.text_input('Product Name')
    product_description = st.text_area('Product Description')
    quantity_type = st.selectbox('Quantity Type', ['Dozen', 'Feet', 'Gallon', 'Gram', 'Hours', 'Inch', 'Kilogram', 'Kilometer', 'Litre'])
    sku = st.text_input('SKU')
    quantity = st.number_input('Quantity', min_value=0, step=1)
    product_cost = st.number_input('Product Cost (in rupees)', min_value=0, step=1)
    sell_price = st.number_input('Sell Price (in rupees)', min_value=0, step=1)
    selected_date = st.date_input('Select Date', datetime.today())
    
    save_details_button = st.button('Save Details')
    
    if save_details_button:
        # Save the product details to session state
        new_product = {
            'ID': product_id,
            'Name': product_name,
            'Description': product_description,
            'Quantity Type': quantity_type,
            'SKU': sku,
            'Quantity': quantity,
            'Cost Price': product_cost,
            'Selling Price': sell_price,
            'Date': selected_date.strftime("%Y-%m-%d")
        }
        st.session_state['products'].append(new_product)
        st.session_state['add_product'] = False
        st.success('Product details saved successfully!')

# Display products and generate report button
if st.session_state['products']:
    st.header('Products Added')
    for i, product in enumerate(st.session_state['products']):
        st.subheader(f"Product {i + 1}")
        st.write(f"**ID:** {product['ID']}")
        st.write(f"**Name:** {product['Name']}")
        st.write(f"**Description:** {product['Description']}")
        st.write(f"**Quantity Type:** {product['Quantity Type']}")
        st.write(f"**SKU:** {product['SKU']}")
        st.write(f"**Quantity:** {product['Quantity']}")
        st.write(f"**Cost Price:** {product['Cost Price']}")
        st.write(f"**Selling Price:** {product['Selling Price']}")
        st.write(f"**Date:** {product['Date']}")
        
    generate_report_button = st.button('Generate Report')
    
    if generate_report_button:
        # Convert session state products to DataFrame
        df = pd.DataFrame(st.session_state['products'])
        
        # Predict sales after a month and a year
        sales_month, sales_year = predict_sales(df, 'Quantity', 'Cost Price', 'Selling Price')
        
        # Calculate total profit, total loss, and total earnings
        total_profit, total_loss, total_earnings = calculate_financials(df, 'Quantity', 'Cost Price', 'Selling Price')
        
        # Generate report
        st.header('Report')
        st.subheader('Sales Prediction')
        st.write(f'Sales after a month: {sales_month}')
        st.write(f'Sales after a year: {sales_year}')
        
        st.subheader('Financials')
        st.write(f'Today\'s Total Profit: {total_profit}')
        st.write(f'Today\'s Total Loss: {total_loss}')
        st.write(f'Total Earnings: {total_earnings}')
        
        # Calculate customer satisfaction
        top_products = df.groupby('Name').sum().sort_values(by='Quantity', ascending=False).head(5)
        st.subheader('Customer Satisfaction (Top 5 Products)')
        st.write(top_products[['Quantity']])
