# Customer Segmentation for Online Retail

## Project Overview
This project applies Data Mining techniques to segment customers of an online retail store based on their purchasing behavior using the **Online Retail II** dataset. We follow the **CRISP-DM** methodology to provide actionable business insights.

## Team Members
- **Ahmed Alham** (ID: 240103291)
- **Abdelhakim Nabil** (ID: 240103115)

## Domain & Dataset
- **Domain:** E-commerce / Retail Analytics
- **Dataset:** [Online Retail II dataset from UCI Machine Learning Repository]
- **Key Features:** Invoice, StockCode, Quantity, Price, CustomerID, Country.

## Methodology (CRISP-DM)
1. **Business Understanding:** Identify high-value customers and churn risks.
2. **Data Understanding:** EDA and quality check (Handling missing IDs and cancellations).
3. **Data Preparation:** RFM (Recency, Frequency, Monetary) feature engineering.
4. **Modeling:** K-Means Clustering.
5. **Evaluation:** Elbow Method & Silhouette Score.
6. **Deployment:** Interactive Streamlit Dashboard.

## Project Structure
- `notebooks/`: Contains the Jupyter Notebook with full Python pipeline.
- `app/`: Contains the Streamlit dashboard (`app.py`).
- `requirements.txt`: List of required libraries.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the dashboard: `python3 -m streamlit run app/dashboard.py`
