import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load dataset
df = pd.read_csv("../data/train.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Title
st.title("📊 Sales Dashboard")

# Display first few rows
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Bar Plot - Total Sales by Category
st.subheader("Total Sales by Category")
category_sales = df.groupby('Category')['Sales'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=category_sales, x='Category', y='Sales', palette='viridis', ax=ax)
ax.set_title("Total Sales by Category", fontsize=14, fontweight='bold')
st.pyplot(fig)
st.caption("💡 Insight: Technology category leads in sales, followed by Furniture and Office Supplies.")

# Histogram - Distribution of Sales
st.subheader("Distribution of Sales")
fig, ax = plt.subplots(figsize=(8,5))
sns.histplot(df["Sales"], bins=20, kde=True, color='blue', ax=ax)
ax.set_title("Distribution of Sales")
st.pyplot(fig)

# Bar Plot - Sales by Region
st.subheader("Total Sales by Region")
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=region_sales, x='Region', y='Sales', palette='coolwarm', ax=ax)
ax.set_title("Total Sales by Region", fontsize=14, fontweight='bold')
st.pyplot(fig)
st.caption("💡 Insight: The West region dominates in sales, indicating a strong customer base.")

# Scatter Plot - Sales vs Quantity
st.subheader("Sales vs Postal Code by Category")
fig, ax = plt.subplots(figsize=(8,5))
sns.scatterplot(data=df, x="Sales", y="Postal Code", hue="Category", palette="Set1", ax=ax)
ax.set_title("Sales vs Quantity")
st.pyplot(fig)

# Sales Trend Over Time
st.subheader("Sales Trend Over Time")
sales_by_date = df.groupby('Order Date')['Sales'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=sales_by_date, x='Order Date', y='Sales', color='blue', ax=ax)
ax.set_title("Sales Trend Over Time", fontsize=14, fontweight='bold')
st.pyplot(fig)
st.caption("💡 Insight: Sales show seasonal spikes, possibly around holidays or year-end promotions.")

# Top 10 products by sales
st.subheader("Top 10 Products by Sales")
top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_products, x='Sales', y='Product Name', palette='magma', ax=ax)
ax.set_title("Top 10 Products by Sales", fontsize=14, fontweight='bold')
st.pyplot(fig)
st.caption("💡 Insight: A small set of products generate disproportionately high sales.")

# Heatmap - Correlation
st.subheader("Correlation Heatmap (Numeric Columns)")
numeric_df = df.select_dtypes(include=['float64', 'int64'])
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="YlGnBu", ax=ax)
ax.set_title("Correlation Heatmap")
st.pyplot(fig)
