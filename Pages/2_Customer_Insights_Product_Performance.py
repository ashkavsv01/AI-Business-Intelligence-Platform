import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Insights & Product Performance", page_icon="👥", layout="wide")

st.title("👥 Customer Insights & Product Performance")

df = pd.read_csv("uploads/cleaned_superstore.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

st.sidebar.header("Filters")

region = st.sidebar.multiselect("Region", sorted(df["Region"].dropna().unique()))
category = st.sidebar.multiselect("Category", sorted(df["Category"].dropna().unique()))
segment = st.sidebar.multiselect("Segment", sorted(df["Segment"].dropna().unique()))

filtered_df = df.copy()

if region:
    filtered_df = filtered_df[filtered_df["Region"].isin(region)]
if category:
    filtered_df = filtered_df[filtered_df["Category"].isin(category)]
if segment:
    filtered_df = filtered_df[filtered_df["Segment"].isin(segment)]

top_customer_sales = filtered_df.groupby("Customer Name")["Sales"].sum().max()
top_product_sales = filtered_df.groupby("Product Name")["Sales"].sum().max()

col1, col2 = st.columns(2)
col1.metric("Top Customer Sales", f"${top_customer_sales:,.2f}")
col2.metric("Top Product Sales", f"${top_product_sales:,.2f}")

st.divider()

left, right = st.columns(2)

with left:
    top_products = (
        filtered_df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Sales"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    segment_sales = filtered_df.groupby("Segment")["Sales"].sum().reset_index()

    fig = px.bar(
        segment_sales,
        x="Segment",
        y="Sales",
        title="Sales by Customer Segment"
    )
    st.plotly_chart(fig, use_container_width=True)

customer_table = (
    filtered_df.groupby("Customer Name")
    .agg({"Sales": "sum", "Profit": "sum"})
    .sort_values("Sales", ascending=False)
    .head(10)
    .reset_index()
)

st.subheader("Top 10 Customers by Sales")
st.dataframe(customer_table, use_container_width=True)

st.subheader("Customer & Product Insights")

st.write("""
- Consumer customers generate the highest revenue.
- Corporate customers contribute strong sales performance.
- Home Office customers represent the smallest revenue segment.
- Technology-related products dominate the top-selling product list.
- Sean Miller is one of the highest revenue customers in the dataset.
""")

st.subheader("Recommendations")

st.write("""
1. Focus retention efforts on high-value customers.
2. Increase marketing campaigns targeting Home Office customers.
3. Maintain inventory levels for top-performing products.
4. Expand successful sales strategies within the Consumer segment.
""")