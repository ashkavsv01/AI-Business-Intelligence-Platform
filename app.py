import streamlit as st

st.set_page_config(
    page_title="AI Retail BI Platform",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #f6f9ff 0%, #ffffff 100%);
}

.hero {
    background: linear-gradient(135deg, #061B44, #0B4FC3);
    padding: 42px;
    border-radius: 22px;
    color: white;
    margin-bottom: 35px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.18);
}

.main-title {
    font-size: 40px;
    font-weight: 850;
    line-height: 1.15;
}

.subtitle {
    font-size: 21px;
    font-weight: 600;
    margin-top: 16px;
}

.hero-text {
    font-size: 16px;
    max-width: 900px;
    line-height: 1.7;
}

.launch-btn {
    display: inline-block;
    background: #1E88FF;
    color: white !important;
    padding: 16px 36px;
    border-radius: 14px;
    text-decoration: none;
    font-weight: 800;
    font-size: 17px;
    margin-top: 18px;
}

.card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    min-height: 215px;
    border: 1px solid #EEF3FF;
}

.tool-card {
    background: #F8FBFF;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #DDEBFF;
    text-align: center;
    min-height: 105px;
}

.feature-box {
    background: #ffffff;
    padding: 20px;
    border-radius: 16px;
    border-left: 6px solid #1E88FF;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

.profile-box {
    background: linear-gradient(135deg, #EEF6FF, #FFFFFF);
    padding: 26px;
    border-radius: 18px;
    border: 1px solid #DDEBFF;
    margin-top: 15px;
}

.footer {
    background: #061B44;
    color: white;
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    margin-top: 45px;
    font-weight: 600;
}

.small-text {
    color: #5d6b82;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="main-title">📊 AI-Powered Retail Business Intelligence Platform</div>
    <div class="subtitle">Transforming Retail Data into Actionable Business Insights</div>
    <p class="hero-text">
    An end-to-end business intelligence solution that combines data cleaning,
    SQL analysis, Power BI dashboards, machine learning forecasting, and Streamlit deployment.
    This platform helps businesses monitor performance, identify trends, understand customers,
    and forecast future sales for smarter decision-making.
    </p>
    <p><b>End-to-End Data Analytics | SQL | Power BI | Machine Learning | Streamlit</b></p>
    <a class="launch-btn" href="/Executive_Sales_Dashboard" target="_self">🚀 Launch Dashboard</a>
</div>
""", unsafe_allow_html=True)

st.header("📌 Project Highlights")

m1, m2, m3, m4, m5 = st.columns(5)

m1.metric("Dashboards", "4")
m2.metric("SQL Queries", "12+")
m3.metric("KPIs", "8+")
m4.metric("Charts", "15+")
m5.metric("Forecast", "6 Months")

st.header("🔄 Project Workflow")

st.markdown("""
1. **Google Colab / Python** – Cleaned raw dataset and created business features  
2. **Excel** – Reviewed and validated the dataset  
3. **SQL** – Performed business analysis queries  
4. **Power BI** – Built three interactive dashboard pages  
5. **Python Forecasting** – Predicted future sales and profit using Linear Regression  
6. **Streamlit** – Converted the project into an interactive web application  
7. **GitHub + Streamlit Cloud** – Published and deployed the project online  
""")

st.header("📊 Dashboard Pages")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📈 Executive Sales Dashboard</h3>
        <p>High-level overview of total sales, profit, orders, customers, regional performance, category profit, and monthly trends.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>👥 Customer Insights & Product Performance</h3>
        <p>Analyzes top customers, best-selling products, customer segments, and product-level sales performance.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🤖 AI Sales Forecast Dashboard</h3>
        <p>Displays predicted sales and profit for the next six months using historical data and machine learning forecasting.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h3>💾 SQL Analysis</h3>
        <p>Allows users to run SQL-based business queries and explore retail sales data interactively.</p>
    </div>
    """, unsafe_allow_html=True)

st.header("✅ Key Features")

f1, f2 = st.columns(2)

with f1:
    st.markdown("""
    <div class="feature-box">
        <h4>Business Intelligence Features</h4>
        <p>✔ KPI monitoring<br>
        ✔ Sales and profit analysis<br>
        ✔ Customer segmentation<br>
        ✔ Product performance analysis<br>
        ✔ Regional and category insights</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-box">
        <h4>Technical Features</h4>
        <p>✔ Python data cleaning<br>
        ✔ SQL query runner<br>
        ✔ Interactive Plotly charts<br>
        ✔ Machine learning forecasting<br>
        ✔ Streamlit web deployment</p>
    </div>
    """, unsafe_allow_html=True)

st.header("🛠 Tools & Technologies Used")

t1, t2, t3, t4, t5, t6 = st.columns(6)

with t1:
    st.markdown('<div class="tool-card">🐍<br><b>Python</b><br><span class="small-text">Data Cleaning</span></div>', unsafe_allow_html=True)
with t2:
    st.markdown('<div class="tool-card">📊<br><b>Pandas</b><br><span class="small-text">Analysis</span></div>', unsafe_allow_html=True)
with t3:
    st.markdown('<div class="tool-card">💾<br><b>SQL</b><br><span class="small-text">Queries</span></div>', unsafe_allow_html=True)
with t4:
    st.markdown('<div class="tool-card">📈<br><b>Power BI</b><br><span class="small-text">Dashboards</span></div>', unsafe_allow_html=True)
with t5:
    st.markdown('<div class="tool-card">🚀<br><b>Streamlit</b><br><span class="small-text">Web App</span></div>', unsafe_allow_html=True)
with t6:
    st.markdown('<div class="tool-card">🤖<br><b>Machine Learning</b><br><span class="small-text">Forecasting</span></div>', unsafe_allow_html=True)

st.header("🏗 Project Architecture")

st.code("""
Raw Retail Dataset
        ↓
Google Colab / Python
        ↓
Cleaned Dataset
        ↓
Excel Validation + SQL Business Analysis
        ↓
Power BI Dashboards
        ↓
Machine Learning Forecasting
        ↓
Streamlit Web Application
        ↓
GitHub + Streamlit Cloud Deployment
""")

st.header("👩‍💻 Project Developer")

st.markdown("""
<div class="profile-box">
    <h3>Aashka Vasava</h3>
    <p><b>Aspiring Data Analyst | MS in Computer Science</b></p>
    <p>
    Passionate about transforming raw data into meaningful business insights through
    analytics, visualization, forecasting, and interactive web applications.
    </p>
    <p>
    🔗 <a href="https://github.com/ashkavsv01" target="_blank"><b>GitHub</b></a>
    &nbsp; | &nbsp;
    🔗 <a href="https://www.linkedin.com/" target="_blank"><b>LinkedIn</b></a>
    </p>
</div>
""", unsafe_allow_html=True)

st.success("Use the sidebar to explore each dashboard page.")

st.markdown("""
<div class="footer">
    © 2026 Aashka Vasava • AI-Business-Intelligence-Platform • Version 1.0.0 • Built with Streamlit
</div>
""", unsafe_allow_html=True)