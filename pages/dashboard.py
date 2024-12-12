import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Celerates's Group 9",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="icons/coffee_ic.png")

df = pd.read_csv("datasets/coffeeshop_kmeans_clustered.csv")

# Preprocessing
# Definisikan kategori produk
category_mapping = {
    'Coffee': ['Mocha', 'Cappuccino', 'Americano', 'Macchiato', 'Latte', 'Espresso', 'Flat White'],
    'Non-Coffee': ['Tea'],
    'Food': ['Cake', 'Sandwich']
}

# Fungsi untuk menetapkan kategori
def assign_category(product_name):
    for category, products in category_mapping.items():
        if product_name in products:
            return category
    return 'Other'

# Tambahkan kolom baru 'menu_category'
df['menu_category'] = df['product_name'].apply(assign_category)

# Convert transaction_date to datetime format
df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

# Fungsi untuk menetapkan periode berdasarkan tanggal transaksi
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['month'] = df['transaction_date'].dt.month

st.title("Coffee Transaction Insight Dashboard")
st.caption(" The Coffee Transaction Insight Dashboard provides a clear and concise overview of sales, products, operational and behavior performance. This dashboard isdesigned for easy data interpretation, the dashboard hopefully can helps management make informed decisions to improve business operations and enchance customer satisfaction")

monthly_sales = df.groupby('month').agg(
total_revenue=('unit_price', lambda x: (x * df.loc[x.index, 'total_qty']).sum())
).reset_index()

# Calculate total quantity per month
monthly_qty = df.groupby('month').agg(
    total_qty=('total_qty', 'sum')
).reset_index()

cluster_count = df['cluster'].value_counts().reset_index()
cluster_count.columns = ['Cluster', 'Jumlah']

# Create the figure
fig1 = go.Figure()

# Add total revenue trend
fig1.add_trace(go.Scatter(
    x=monthly_sales['month'].astype(str), 
    y=monthly_sales['total_revenue'], 
    mode='lines+markers',
    name='Total Pendapatan',
    line=dict(color='blue'),
    marker=dict(size=8)
))

# Add total quantity trend
fig1.add_trace(go.Scatter(
    x=monthly_qty['month'].astype(str), 
    y=monthly_qty['total_qty'], 
    mode='lines+markers',
    name='Jumlah Penjualan',
    line=dict(color='orange'),
    marker=dict(size=8)
))

# Update layout
fig1.update_layout(
    xaxis_title="Bulan",
    yaxis_title="Nilai",
    legend_title="Metode",
    hovermode="x unified"
)

# Display the chart
st.markdown("#### Comparison of Revenue Trends and Sales Amount per Month")
st.plotly_chart(fig1)


col1,col2 = st.columns(2)


with col1:
    category_sales = df.groupby('menu_category').agg(
        total_qty=('total_qty', 'sum')
    ).reset_index().sort_values(by='total_qty', ascending=False)
    # Create a Pie Chart
    fig_pie_chart = px.pie(
        category_sales, 
        names='menu_category', 
        values='total_qty', 
        labels={'menu_category': 'Category', 'total_qty': 'Jumlah Terjual'},
        color_discrete_sequence=[ '#714616','#F3CA7C', '#FFE7C9'],
    )
    fig_pie_chart.update_traces(textinfo='percent+label', textfont_size=18, marker=dict(line=dict(color='#000000',width=1)))
    st.markdown("#### Best Selling Category Menu")
    st.plotly_chart(fig_pie_chart)

    # Plotly Pie Chart
    fig_pie_chart = px.pie(
        cluster_count, 
        names='Cluster', 
        values='Jumlah',
        color='Cluster',
        color_discrete_sequence=['#207cb4', '#10346c', '#8CC1A9']
    )
    fig_pie_chart.update_traces(textinfo='percent+label', textfont_size=18, marker=dict(line=dict(color='#000000',width=1)))
    st.markdown("#### Product Category Distribution by Price")
    st.plotly_chart(fig_pie_chart)


with col2:
    # 2. Visualisasi Penjualan Produk Terlaris
    product_sales = df.groupby('product_name').agg(
        total_sold=('total_qty', 'sum')
    ).reset_index().sort_values(by='total_sold', ascending=False)

    fig2 = px.bar(
        product_sales, 
        x='product_name', 
        y='total_sold', 
        labels={'product_name': 'Produk', 'total_sold': 'Jumlah Terjual'},
        text='total_sold',
        color='total_sold',
        color_continuous_scale='GnBu'
    )
    st.markdown("#### Best Selling Product")
    st.plotly_chart(fig2)

        # 3. Visualisasi Pendapatan per Kota
    city_revenue = df.groupby('city').agg(
        total_revenue=('unit_price', lambda x: (x * df.loc[x.index, 'total_qty']).sum())
    ).reset_index().sort_values(by='total_revenue', ascending=False)

    fig3 = px.bar(
        city_revenue, 
        x='city', 
        y='total_revenue', 
        labels={'city': 'Kota', 'total_revenue': 'Total Pendapatan'},
        text='total_revenue',
        color='total_revenue',
        color_continuous_scale='Blues'
    )
    st.markdown("#### Total Revenue by City")
    st.plotly_chart(fig3)

st.markdown("#### Coffee Transaction 2023 Dataset table")
df = df.drop(['month'], axis=1)
st.dataframe(df, use_container_width=True)

