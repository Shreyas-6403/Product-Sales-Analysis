# 🛍️ ProductSalesAnalysis

> **Transform Data into Strategic Sales Power**

ProductSalesAnalysis is an intelligent Streamlit-powered analytics platform that transforms raw sales data into actionable business insights. Designed for data analysts, business teams, and sales strategists, it offers features for trend analysis, predictive modeling, and real-time dashboard visualization.

---

### 📌 Built With

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Data%20Apps-red)
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange)
![Plotly](https://img.shields.io/badge/Viz-Plotly-blueviolet)
![Markdown](https://img.shields.io/badge/docs-Markdown-black)
![TOML](https://img.shields.io/badge/config-TOML-brown)

---

## 📚 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Screenshots](#screenshots)
- [License](#license)

---

## 🧠 Overview

ProductSalesAnalysis simplifies complex sales workflows by providing:
- Clean dashboards for financial KPIs.
- Forecasting models to identify trends.
- Visualization tools to track product-level performance.

The project streamlines:
- **Data Ingestion**
- **Sales Forecasting**
- **Real-time Visualization**
- **Predictive Analytics**

---

## ✨ Features

- 📊 **Real-time Metrics**: Generate up-to-date financial KPIs and performance indicators.
- 📈 **Interactive Visualization**: Use Plotly and Streamlit for live data dashboards.
- 🧠 **Forecasting Capabilities**: Machine learning predictions using scikit-learn.
- 🎛️ **Customizable UI**: Modular configuration with `config.toml`.
- 🔗 **Seamless Integration**: Adaptable for integration with CSVs, APIs, and databases.

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have the following installed:
- Python 3.8+
- pip (Python package installer)

---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
# 1. Clone the repo
git clone https://github.com/Shreyas-6403/ProductSalesAnalysis.git

# 2. Navigate to project directory
cd ProductSalesAnalysis

# 3. Install requirements
pip install -r requirements.txt
```

---

## 🧪 Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

Customize configuration using the `config.toml` file if needed.

---

## ⚙️ Configuration

`config.toml` allows you to:
- Change dataset paths
- Switch model parameters
- Update UI elements
- Set chart preferences

Example (inside `config.toml`):

```toml
[data]
file_path = "data/sales_data.csv"

[model]
type = "RandomForest"
train_split = 0.8
```

---

## 🧪 Testing

Tests are written using `pytest`. To run all tests:

```bash
pytest
```

---

## 📸 Screenshots

### 🔹 Home Screen

<p align="center"> <img src="https://blogger.googleusercontent.com/img/a/AVvXsEh5v3sCzgyYpeeEA3wiLCRU_8tLNSIM2KDp-ljFODgg4JcfM5J5z7okUO_ZXiHRjxxG4NWgMHmwcMe9_TlO4RfDTwRzTyomVlO5tW56ILnRnUSuLazmXiF6NWe6Qf1nMbxDuGAiuGmntl9zZ5Ak_NqDVAxSlDfWsu4D2TqYQVLrpDTEswi0ZSNw87id_SzJ=w372-h349" alt="Home Screen" width="400"/> </p>

### 🔹 Sales Report View

![Sales Report](https://blogger.googleusercontent.com/img/a/AVvXsEivMWaPapDogBYRXjmkfROBfqWVtb6ajMeNSgCtd0BfQZyXxHkTra2Hn0Lj9RiiuBkjU40nL3XvqpcS0uzpJrYlGdu1Roxvu3gFC1liTqlqaui_7Sf-JHM86ysYqoWVZuGi7QOCq8B1dvXeFF0s9ypLeiNBIa7qfFOJOawHk8RLHqnYvlS6uk5QHCS-8r_O=w383-h238)

### 🔹 Insights Dashboard

![Insights](https://blogger.googleusercontent.com/img/a/AVvXsEjUedbNOtHFyu-ZFPk70CHS-HtVpAUFcXA9XBQuVxeK0wbrwdRUm3xNmch80ebGUx7uf12hR-Fa7kUcoFL7BhGWfrSkZBwNzXrNGlKcKuZYucmoRyONbb7OjoqzjdYCKaBbkP38dAjXj9kJiud_DvfJK467lUg22j3tOBqqYOPiyxREiybAKX80ZB7kv1gk=w390-h314)

---
## 🙋‍♂️ Author

**Shreyas Kulkarni**  
Connect on [LinkedIn](https://www.linkedin.com/in/shreyas-kulkarni-dev)

---

## ⭐️ Show your support

If you like this project, please consider starring 🌟 the repository. Your feedback helps it grow!
