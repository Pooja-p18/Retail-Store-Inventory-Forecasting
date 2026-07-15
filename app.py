import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Retail Store Inventory Forecasting",
    page_icon="📦",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("📦 Retail Store Inventory Forecasting Dashboard")

st.markdown("""
### End-to-End Machine Learning Project

This project predicts **Retail Store Inventory Demand** using Machine Learning techniques.

The objective is to help retailers estimate future product demand, optimize inventory levels, and support data-driven business decisions.

---

### 🎯 Project Objective

Build a machine learning model capable of predicting **Units Sold** using historical inventory, pricing, promotion, weather, and seasonal information.

---

### 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib
- Git & GitHub
""")

st.success("Use the navigation menu on the left to explore the project.")