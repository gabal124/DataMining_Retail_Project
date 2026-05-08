import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retail Insights Dashboard", layout="wide")

st.title("🛍️ Customer Segmentation Dashboard")
st.markdown("""
هذه اللوحة تعرض نتائج تقسيم العملاء باستخدام منهجية **CRISP-DM** وتقنية **K-Means Clustering**.
""")

@st.cache_data
def load_data():
    return pd.read_csv('data/rfm_clusters.csv') 

try:
    df = load_data()

    st.sidebar.header("Global Filters")
    selected_cluster = st.sidebar.multiselect("Select Segments", 
                                            options=df['Cluster'].unique(), 
                                            default=df['Cluster'].unique())
    
    filtered_data = df[df['Cluster'].isin(selected_cluster)]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Clusters Visualization (3D)")
        fig_3d = px.scatter_3d(filtered_data, x='Recency', y='Frequency', z='Monetary',
                               color='Cluster', opacity=0.7, title="RFM Clusters")
        st.plotly_chart(fig_3d, use_container_width=True)

    with col2:
        st.subheader("Segment Sizes")
        fig_pie = px.pie(filtered_data, names='Cluster', title="Distribution of Customers")
        st.plotly_chart(fig_pie, use_container_width=True)

    st.divider()
    st.subheader("💡 Business Insights & Recommendations")
    
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Total Customers", len(filtered_data))
    col_b.metric("Avg Monetary Value", f"£{filtered_data['Monetary'].mean():.2f}")
    
    st.info("""
    **Top Recommendations:**
    1. **VIP Group:** Focus on loyalty rewards and early access to new collections.
    2. **At Risk Group:** Re-engage with 'We Miss You' email campaigns and personalized discounts.
    3. **New Customers:** Provide a welcome discount to encourage a second purchase.
    """)

except FileNotFoundError:
    st.error("Please run the Notebook first to generate 'rfm_clusters.csv' in the data folder.")
