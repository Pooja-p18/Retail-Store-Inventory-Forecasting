import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Overview", page_icon="📊", layout="wide")

#Load data
raw_df =pd.read_csv("data/retail_store_inventory.csv")
raw_df.columns = raw_df.columns.str.strip() # Strip whitespace from column names
raw_df['Date'] = pd.to_datetime(raw_df['Date']) # Convert 'Date' column to datetime

st.title("📊 Date Overview")

st.write("Summary statistics and key information of the dataset.")

#KPI cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", f"{len(raw_df):,}")
    
with col2:
    st.metric("Stores", raw_df['Store ID'].nunique())
    
with col3:
    st.metric("Products", raw_df['Product ID'].nunique())
    
with col4:
    st.metric("Date Range", f"{raw_df['Date'].dt.year.min()} - {raw_df['Date'].dt.year.max()}")
    

st.divider()

st.subheader("Dataset Preview")
st.dataframe(raw_df.head())

st.subheader("Dataset Information")

info = pd.DataFrame({
    "Column": raw_df.columns,
    "Data Type": raw_df.dtypes.astype(str).values,
    "Missing Values": raw_df.isnull().sum().values
})

st.dataframe(info, use_container_width=True)

st.subheader("Summary Statistics")
st.dataframe(raw_df.describe())