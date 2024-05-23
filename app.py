import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor  # Example ML model

# Load the product sales data
df = pd.read_csv('ProductData.csv')

# Function to preprocess data and train ML model
def preprocess_data_and_train_model(df):
    # Data preprocessing steps (if any)
    # Feature engineering (if any)
    # Split data into features (X) and target (y)
    X = df[['Product ID', 'Product Cost (in rupees)', 'Sell Price (in rupees)']]
    y = df['Quantity Sold']
    
    # Train a machine learning model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model

# Function to predict sales after a month and a year
def predict_sales(data, model):
    # Get today's date
    today = datetime.now()
    
    # Predict sales after a month
    one_month_later = today + timedelta(days=30)
    month_data = data[data['Sales Date'] > today]
    month_sales = model.predict(month_data[['Product ID', 'Product Cost (in rupees)', 'Sell Price (in rupees)']])
    total_month_sales = month_sales.sum()
    
    # Predict sales after a year
    one_year_later = today + timedelta(days=365)
    year_data = data[data['Sales Date'] > today]
    year_sales = model.predict(year_data[['Product ID', 'Product Cost (in rupees)', 'Sell Price (in rupees)']])
    total_year_sales = year_sales.sum()
    
    return total_month_sales, total_year_sales

# Function to calculate total profit, total loss, and total earnings
def calculate_profit_loss(data):
    today = datetime.now().strftime("%Y-%m-%d")
    today_data = data[data['Sales Date'] == today]
    today_data['Total'] = today_data['Quantity Sold'] * today_data['Sell Price (in rupees)']
    total_profit = today_data[today_data['Total'] > 0]['Total'].sum()
    total_loss = today_data[today_data['Total'] < 0]['Total'].sum()
    total_earnings = today_data['Total'].sum()
    
    return total_profit, total_loss, total_earnings

# Load or train the machine learning model
model = preprocess_data_and_train_model(df)

# User interface
st.title("PRODUCT SALES ANALYSIS")

# User input form
st.header('Input Parameters')
product_id = st.number_input('Product ID')
product_cost = st.number_input('Product Cost (in rupees)', min_value=0, step=1)
sell_price = st.number_input('Sell Price (in rupees)', min_value=0, step=1)
submit_button = st.button('Generate Report')

# Generate report
if submit_button:
    st.header('Report')
    
    # Predict sales after a month and a year
    sales_month, sales_year = predict_sales(df, model)
    st.subheader('Sales Prediction')
    st.write(f'Sales after a month: {sales_month}')
    st.write(f'Sales after a year: {sales_year}')
    
    # Calculate total profit, total loss, and total earnings
    total_profit, total_loss, total_earnings = calculate_profit_loss(df)
    st.subheader('Financials')
    st.write(f'Today\'s Total Profit: {total_profit}')
    st.write(f'Today\'s Total Loss: {total_loss}')
    st.write(f'Total Earnings: {total_earnings}')
