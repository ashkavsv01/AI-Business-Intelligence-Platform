import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Sales Forecast Dashboard", page_icon="🤖", layout="wide")

st.title("🤖 AI Sales & Profit Forecast Dashboard")

forecast_df = pd.read_csv("uploads/sales_forecast.csv")

col1, col2 = st.columns(2)

col1.metric("Total Predicted Sales", f"${forecast_df['Predicted_Sales'].sum():,.2f}")
col2.metric("Total Predicted Profit", f"${forecast_df['Predicted_Profit'].sum():,.2f}")

st.divider()

fig = px.line(
    forecast_df,
    x="Forecast_Month",
    y="Predicted_Sales",
    markers=True,
    title="Predicted Sales by Forecast Month"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Forecast Data")
st.dataframe(forecast_df, use_container_width=True)

st.subheader("AI Forecast Summary")

st.write("""
- Sales are expected to show a steady upward trend over the next six months based on historical sales patterns.
- Profit is projected to grow alongside sales, indicating positive business performance.
- Current forecasts suggest stable demand with no significant decline in revenue.
- Business outlook shows positive growth.
""")

st.subheader("Recommended Actions")

st.write("""
1. Increase inventory planning for high-demand products.
2. Continue investing in top-performing product categories.
3. Monitor forecast accuracy regularly.
4. Update the model with new sales data.
""")

csv = forecast_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Forecast CSV",
    data=csv,
    file_name="sales_forecast.csv",
    mime="text/csv"
)