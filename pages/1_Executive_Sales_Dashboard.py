import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Executive Sales Dashboard", page_icon="📊", layout="wide")

st.title("📊 Executive Sales Dashboard")

df = pd.read_csv("uploads/cleaned_superstore.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

df["Year"] = df["Order Date"].dt.year
df["Month_Name"] = df["Order Date"].dt.month_name()

st.sidebar.header("Filters")

year = st.sidebar.multiselect("Year", sorted(df["Year"].dropna().unique()))
region = st.sidebar.multiselect("Region", sorted(df["Region"].dropna().unique()))
category = st.sidebar.multiselect("Category", sorted(df["Category"].dropna().unique()))
segment = st.sidebar.multiselect("Segment", sorted(df["Segment"].dropna().unique()))

filtered_df = df.copy()

if year:
    filtered_df = filtered_df[filtered_df["Year"].isin(year)]
if region:
    filtered_df = filtered_df[filtered_df["Region"].isin(region)]
if category:
    filtered_df = filtered_df[filtered_df["Category"].isin(category)]
if segment:
    filtered_df = filtered_df[filtered_df["Segment"].isin(segment)]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
col3.metric("Total Orders", f"{filtered_df['Order ID'].nunique():,}")
col4.metric("Total Customers", f"{filtered_df['Customer ID'].nunique():,}")

st.divider()

left, right = st.columns(2)

with left:
    sales_region = filtered_df.groupby("Region")["Sales"].sum().reset_index()
    fig = px.bar(sales_region, x="Region", y="Sales", title="Sales by Region")
    st.plotly_chart(fig, use_container_width=True)

with right:
    profit_category = filtered_df.groupby("Category")["Profit"].sum().reset_index()
    fig = px.bar(profit_category, x="Category", y="Profit", title="Profit by Category")
    st.plotly_chart(fig, use_container_width=True)

monthly_sales = filtered_df.groupby("Month_Name")["Sales"].sum().reset_index()

month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

monthly_sales["Month_Name"] = pd.Categorical(
    monthly_sales["Month_Name"],
    categories=month_order,
    ordered=True
)

monthly_sales = monthly_sales.sort_values("Month_Name")

fig = px.line(
    monthly_sales,
    x="Month_Name",
    y="Sales",
    markers=True,
    title="Sales Trend by Month"
)

st.plotly_chart(fig, use_container_width=True)

left2, right2 = st.columns(2)

with left2:
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

with right2:
    sales_profit = filtered_df.groupby("Category")[["Sales", "Profit"]].sum().reset_index()

    fig = px.bar(
        sales_profit,
        x="Category",
        y=["Sales", "Profit"],
        barmode="group",
        title="Sales and Profit by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("🤖 AI-Generated Business Insights")

st.write("""
- West region leads overall sales performance.
- Technology delivers the strongest profitability.
- Consumer customers generate the highest revenue.
- Furniture sales are strong, but profit margins remain relatively low.
""")

st.subheader("💡 Recommended Actions")

st.write("""
1. Increase investment in Technology products.
2. Optimize Furniture pricing and discount strategies.
3. Replicate West Region sales strategies across other regions.
""")