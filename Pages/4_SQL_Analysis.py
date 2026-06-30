import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(
    page_title="SQL Analysis",
    page_icon="💾",
    layout="wide"
)

st.title("💾 SQL Analysis Dashboard")

st.write("Run SQL queries on the cleaned retail sales dataset.")

# Load dataset
df = pd.read_csv("uploads/cleaned_superstore.csv")

# Create SQLite database in memory
conn = sqlite3.connect(":memory:")
df.to_sql("sales", conn, if_exists="replace", index=False)

st.subheader("Sample SQL Queries")

sample_query = st.selectbox(
    "Choose a sample query",
    [
        "SELECT * FROM sales LIMIT 10;",
        "SELECT Region, SUM(Sales) AS Total_Sales FROM sales GROUP BY Region;",
        "SELECT Category, SUM(Profit) AS Total_Profit FROM sales GROUP BY Category;",
        "SELECT Segment, SUM(Sales) AS Total_Sales FROM sales GROUP BY Segment;",
        "SELECT `Customer Name`, SUM(Sales) AS Total_Sales FROM sales GROUP BY `Customer Name` ORDER BY Total_Sales DESC LIMIT 10;",
        "SELECT `Product Name`, SUM(Sales) AS Total_Sales FROM sales GROUP BY `Product Name` ORDER BY Total_Sales DESC LIMIT 10;",
        "SELECT State, SUM(Sales) AS Total_Sales FROM sales GROUP BY State ORDER BY Total_Sales DESC;",
        "SELECT Year, SUM(Sales) AS Total_Sales FROM sales GROUP BY Year;"
    ]
)

query = st.text_area(
    "Write or edit SQL query",
    sample_query,
    height=150
)

if st.button("Run Query"):

    try:
        result = pd.read_sql_query(query, conn)

        st.success("Query executed successfully!")

        st.dataframe(result, use_container_width=True)

        csv = result.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Result",
            csv,
            "query_result.csv",
            "text/csv"
        )

    except Exception as e:
        st.error(e)