import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

st.title("📊 Customer Segmentation for Online Retail")
st.sidebar.header("Filters")

# Sample Insight
st.info("This dashboard visualizes customer segments based on RFM Analysis.")

# Placeholder for Data Loading
# df = pd.read_csv('data/cleaned_data.csv')

# Global Filter Example
# country = st.sidebar.multiselect("Select Country", options=df['Country'].unique())

# Charts
col1, col2 = st.columns(2)
with col1:
    st.subheader("Customer Segments Distribution")
    # st.plotly_chart(fig_pie)

with col2:
    st.subheader("RFM 3D Clusters")
    # st.plotly_chart(fig_scatter)

st.markdown("""
### 💡 Business Recommendations
- **Champions:** Target with new arrivals and loyalty programs.
- **At Risk:** Send personalized discount emails to re-engage.
""")
