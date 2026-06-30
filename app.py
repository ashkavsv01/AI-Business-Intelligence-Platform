import streamlit as st

st.set_page_config(
    page_title="AI Retail BI Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Powered Retail Business Intelligence Platform")

st.write("""
This web application is the next phase of my Power BI project. It converts my retail analytics dashboard into an interactive Streamlit application where users can explore sales performance, customer insights, product performance, and AI-based sales forecasting.
""")

st.divider()

st.header("Project Overview")

st.write("""
In this project, I used retail sales data to build an end-to-end business intelligence solution. The workflow includes data cleaning, feature engineering, SQL analysis, Power BI dashboard development, sales forecasting, and now Streamlit web application development.
""")

st.header("Project Workflow")

st.markdown("""
1. **Google Colab / Python** – Cleaned the raw dataset and created new business features  
2. **Excel** – Reviewed and validated the dataset  
3. **SQL** – Performed business analysis queries  
4. **Power BI** – Built three interactive dashboard pages  
5. **Python Forecasting** – Predicted future sales and profit  
6. **Streamlit** – Converted the project into an interactive web application  
""")

st.header("Dashboard Pages")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Executive Sales Dashboard")
    st.write("""
    Shows overall sales performance using KPIs, regional sales, category profit, monthly sales trends, and business insights.
    """)

with col2:
    st.subheader("2. Customer Insights & Product Performance")
    st.write("""
    Analyzes top customers, top products, customer segments, and product-level performance.
    """)

with col3:
    st.subheader("3. AI Sales Forecast Dashboard")
    st.write("""
    Displays future sales and profit predictions using historical data and machine learning forecasting.
    """)

st.header("Tools & Technologies Used")

st.markdown("""
**Python | Pandas | NumPy | SQL | Excel | Power BI | Streamlit | Plotly | Machine Learning**
""")

st.info("Use the sidebar on the left to open each dashboard page.")