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
    page_icon="icons/smart_toy.svg")

df = pd.read_csv("coffeeshop.csv")


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
def categorize_day(date):
    day_of_month = date.day
    if 1 <= day_of_month <= 10:
        return 'Awal Bulan'
    elif 11 <= day_of_month <= 20:
        return 'Tengah Bulan'
    else:
        return 'Akhir Bulan'

# Tambahkan kolom baru 'transaction_period'
df['transaction_period'] = df['transaction_date'].apply(categorize_day)

# Preprocessing
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['month'] = df['transaction_date'].dt.month

st.title("Sentiment Analysis Dashboard")

monthly_sales = df.groupby('month').agg(
total_revenue=('unit_price', lambda x: (x * df.loc[x.index, 'total_qty']).sum())
).reset_index()

# Calculate total quantity per month
monthly_qty = df.groupby('month').agg(
    total_qty=('total_qty', 'sum')
).reset_index()

# Group data by transaction_period
period_sales = df.groupby('transaction_period').agg(
    total_qty=('total_qty', 'sum')
).reset_index()

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
    title="Perbandingan Tren Pendapatan vs Jumlah Penjualan per Bulan",
    xaxis_title="Bulan",
    yaxis_title="Nilai",
    legend_title="Metode",
    hovermode="x unified"
)

# Display the chart
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
        title="Menu Kategori Terlaris",
        labels={'menu_category': 'Category', 'total_qty': 'Jumlah Terjual'},
        color_discrete_sequence=[ '#714616','#F3CA7C', '#FFE7C9'],
    )
    fig_pie_chart.update_traces(textinfo='percent+label', textfont_size=18, marker=dict(line=dict(color='#000000',width=1)))

    st.plotly_chart(fig_pie_chart)

    # Create a Pie Chart
    fig_pie_chart = px.pie(
        period_sales, 
        names='transaction_period', 
        values='total_qty', 
        title="Total Jumlah Penjualan Berdasarkan Periode Transaksi",
        labels={'transaction_period': 'Periode Transaksi', 'total_qty': 'Jumlah Terjual'},
        color_discrete_sequence=px.colors.sequential.Blues
    )
    fig_pie_chart.update_traces(textinfo='percent+label', textfont_size=18, marker=dict(line=dict(color='#000000',width=1)))
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
        title="Penjualan Produk Terlaris", 
        labels={'product_name': 'Produk', 'total_sold': 'Jumlah Terjual'},
        text='total_sold',
        color='total_sold',
        color_continuous_scale='GnBu'
    )
    st.plotly_chart(fig2)

        # 3. Visualisasi Pendapatan per Kota
    city_revenue = df.groupby('city').agg(
        total_revenue=('unit_price', lambda x: (x * df.loc[x.index, 'total_qty']).sum())
    ).reset_index().sort_values(by='total_revenue', ascending=False)

    fig3 = px.bar(
        city_revenue, 
        x='city', 
        y='total_revenue', 
        title="Pendapatan per Kota", 
        labels={'city': 'Kota', 'total_revenue': 'Total Pendapatan'},
        text='total_revenue',
        color='total_revenue',
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig3)

st.markdown("#### Coffee Transaction 2023 Dataset table")
df = df.drop(['month'], axis=1)
st.dataframe(df, use_container_width=True)