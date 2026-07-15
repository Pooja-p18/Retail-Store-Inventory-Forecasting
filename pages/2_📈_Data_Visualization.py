import streamlit as st
import pandas as pd
import plotly.express as px

#Page Configuration
st.set_page_config(page_title="Data Visualization", page_icon="📈",layout="wide")

#Load data
def load_data():
    df = pd.read_csv("data/retail_store_inventory.csv")
    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"])
    return df
raw_df = load_data()

#Sidebar Filters
st.sidebar.header("Filters")
selected_region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(raw_df["Region"].unique().tolist())
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(raw_df["Category"].unique().tolist())
)

selected_store = st.sidebar.selectbox(
    "Store",
    ["All"] + sorted(raw_df["Store ID"].unique().tolist())
)

#Apply Filters
filtered_df = raw_df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]
    
if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]
    
if selected_store != "All":
    filtered_df = filtered_df[
        filtered_df["Store ID"] == selected_store
    ]
    
#Title
st.title("📈 Data Visualisation")
st.markdown("Explore retails trends using interactive charts.")

#KPI cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Units Sold",
        f"{filtered_df['Units Sold'].sum():,}"
    )
    
with col2:
    st.metric(
        "Average Price",
        f"${filtered_df['Price'].mean():.2f}"
    )
    
with col3:
    st.metric(
        "Average Inventory",
        f"{filtered_df['Inventory Level'].mean():.0f}"
    )
    
st.divider()

#Daily Sales Trend
daily_sales = (
    filtered_df.groupby("Date")["Units Sold"]
    .sum()
    .reset_index()
)

fig = px.line(
    daily_sales,
    x= "Date",
    y="Units Sold",
    title= "Daily Sales Trend"
)

st.plotly_chart(fig, use_container_width=True)

#Two charts side by side
col1, col2 = st.columns(2)

with col1:
    category_sales = (
        filtered_df.groupby("Category")["Units Sold"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Units Sold",
        title="Sales by Category"
    )

    st.plotly_chart(fig, use_container_width=True)
    
with col2:
    region_sales = (
        filtered_df.groupby("Region")["Units Sold"]
        .sum()
        .reset_index()
    )
    
    fig = px.pie(
        region_sales, 
        values="Units Sold",
        names="Region",
        title="Sales by Region"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
#Inventory Distribution
fig = px.histogram(
    filtered_df,
    x="Inventory Level",
    nbins=30,
    title="Inventory Level Distribution"
)

st.plotly_chart(fig, use_container_width= True)

#Price Distribution
fig = px.box(
    filtered_df,
    y="Price",
    title="Price Distribution"
)
st.plotly_chart(fig, use_container_width=True)