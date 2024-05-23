import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Initialize session state for storing product data
if 'products' not in st.session_state:
    st.session_state['products'] = []

def predict_sales(data, start_date, end_date, quantity_col, price_col):
    data['Date'] = pd.to_datetime(data['Date'])
    data_period = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
    sales = (data_period[quantity_col] * data_period[price_col]).sum()
    return sales

def calculate_financials(data, date, quantity_col, cost_col, price_col):
    data['Date'] = pd.to_datetime(data['Date'])
    today_data = data[data['Date'] == date]
    today_data['Total'] = today_data[quantity_col] * (today_data[price_col] - today_data[cost_col])
    total_profit = today_data[today_data['Total'] > 0]['Total'].sum()
    total_loss = today_data[today_data['Total'] < 0]['Total'].sum()
    total_earnings = today_data['Total'].sum()
    return total_profit, total_loss, total_earnings

def evaluate_model(data, train_end_date, test_end_date, quantity_col, price_col):
    train_start_date = data['Date'].min()
    test_start_date = train_end_date + timedelta(days=1)
    
    actual_sales = []
    predicted_sales = []
    
    for date in pd.date_range(test_start_date, test_end_date):
        actual = predict_sales(data, date, date, quantity_col, price_col)
        predicted = predict_sales(data[data['Date'] <= train_end_date], date, date, quantity_col, price_col)
        actual_sales.append(actual)
        predicted_sales.append(predicted)
    
    mae = mean_absolute_error(actual_sales, predicted_sales)
    mse = mean_squared_error(actual_sales, predicted_sales)
    rmse = np.sqrt(mse)
    
    return mae, mse, rmse

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
        with st.expander(f"Product {i + 1}: {product['Name']}"):
            st.markdown(f"""
            <div style="background-color: #f9f9f9; padding: 10px; border-radius: 5px; color: black;">
                <strong>ID:</strong> {product['ID']}<br>
                <strong>Name:</strong> {product['Name']}<br>
                <strong>Description:</strong> {product['Description']}<br>
                <strong>Quantity Type:</strong> {product['Quantity Type']}<br>
                <strong>SKU:</strong> {product['SKU']}<br>
                <strong>Quantity:</strong> {product['Quantity']}<br>
                <strong>Cost Price:</strong> ₹{product['Cost Price']}<br>
                <strong>Selling Price:</strong> ₹{product['Selling Price']}<br>
                <strong>Date:</strong> {product['Date']}
            </div>
            """, unsafe_allow_html=True)
        
    generate_report_button = st.button('Generate Report')
    
    if generate_report_button:
        df = pd.DataFrame(st.session_state['products'])
        
        # Predict sales after a month and a year
        today = datetime.today()
        sales_month = predict_sales(df, today, today + timedelta(days=30), 'Quantity', 'Selling Price')
        sales_year = predict_sales(df, today, today + timedelta(days=365), 'Quantity', 'Selling Price')
        
        # Calculate total profit, total loss, and total earnings
        total_profit, total_loss, total_earnings = calculate_financials(df, today, 'Quantity', 'Cost Price', 'Selling Price')
        
        # Evaluate model
        mae, mse, rmse = evaluate_model(df, today - timedelta(days=365), today, 'Quantity', 'Selling Price')
        
        # Generate report
        st.header('Report')
        
        st.markdown("""
        <style>
        .report-section {
            background-color: #2a151a;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }
        .report-section:hover {
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        .report-section h3 {
            color: #ffab40;
            font-size: 24px;
        }
        .report-section p {
            color: white;
            font-size: 18px;
        }
        .table-section {
            background-color: #1b1b2f;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
            color: white;
        }
        .table-section:hover {
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        .table-section table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        .table-section th, .table-section td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .table-section th {
            background-color: #162447;
            color: #ffab40;
        }
        .table-section td {
            background-color: #1b1b2f;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="report-section">
            <h3>Sales Prediction</h3>
            <p><strong>Sales after a month:</strong> ₹{sales_month}</p>
            <p><strong>Sales after a year:</strong> ₹{sales_year}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="report-section">
            <h3>Financials</h3>
            <p><strong>Today's Total Profit:</strong> ₹{total_profit}</p>
            <p><strong>Today's Total Loss:</strong> ₹{total_loss}</p>
            <p><strong>Total Earnings:</strong> ₹{total_earnings}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="report-section">
            <h3>Model Evaluation</h3>
            <p><strong>Mean Absolute Error (MAE):</strong> ₹{mae}</p>
            <p><strong>Mean Squared Error (MSE):</strong> ₹{mse}</p>
            <p><strong>Root Mean Squared Error (RMSE):</strong> ₹{rmse}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Calculate top rated products and customer satisfaction
        numeric_columns = df.select_dtypes(include='number').columns
        top_products = df.groupby('Name', as_index=False)[numeric_columns].sum().sort_values(by='Quantity', ascending=False).head(5)
        
        st.markdown(f"""
        <div class="table-section">
            <h3>Top Rated Products & Customer Satisfaction (Top 5 Products)</h3>
            <table>
                <tr>
                    <th>Product Name</th>
                    <th>Total Quantity Sold</th>
                </tr>
                {''.join([f"<tr><td>{row['Name']}</td><td>{row['Quantity']}</td></tr>" for index, row in top_products.iterrows()])}
            </table>
        </div>
        """, unsafe_allow_html=True)
