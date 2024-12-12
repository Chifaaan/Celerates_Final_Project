import streamlit as st
import numpy as np
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


tab1,tab2,tab3 = st.tabs(["Evaluation","Clustering","Custom Plot"])
highest_scores_df = pd.read_csv("evaluation/coffeeshop_best_eval.csv")
kmean_eval_df = pd.read_csv("evaluation/coffeeshop_kmeans_eval.csv")
AGG_eval_df = pd.read_csv("evaluation/coffeeshop_agg_eval.csv")
DBSCAN_eval_df = pd.read_csv("evaluation/coffeeshop_dbscan_eval.csv")


with tab1:
    # Membuat bar plot dengan Plotly
    fig = px.bar(
        highest_scores_df, 
        x='Method', 
        y='Max_Silhouette_Score', 
        color='Max_Silhouette_Score',
        color_continuous_scale='Tealgrn',
        title='Highest Silhouette Scores for Different Clustering Methods',
        labels={'Method': 'Clustering Method', 'Max_Silhouette_Score': 'Max Silhouette Score'},
        text='Max_Silhouette_Score',
        height=800
    )
    fig.update_layout(yaxis=dict(range=[0, 1]))

    # Menampilkan visualisasi pada Streamlit
    st.title("Clustering Evaluation Visualization")
    st.caption("The Clustering Evaluation Visualization dashboard provides an interactive and intuitive representation of clustering model performance. It showcases key evaluation metrics such as silhouette scores and cluster distributions, helping users assess the effectiveness of different clustering algorithms. Through clear visualizations, it simplifies the comparison of models, enabling data-driven decisions for optimal clustering solutions.")
    st.plotly_chart(fig)



        # Selectbox for clustering methods
    selected_method = st.selectbox("Select Clustering Method Evaluation", [
        'KMeans Clustering', 
        'Agglomerative Clustering', 
        'DBSCAN Clustering'
    ])

    if selected_method == 'KMeans Clustering':
        fig = px.bar(
            kmean_eval_df, 
            x='Feature Type', 
            y='Silhouette_score',
            color='Silhouette_score',
            color_continuous_scale='Tealgrn',
            title='Highest Silhouette Scores for KMeans Clustering',
            text='Silhouette_score',
            height=600
        )
        fig.update_layout(yaxis=dict(range=[0, 1]))
        st.plotly_chart(fig)
        with st.expander("See KMeans Dataframe"):
            st.dataframe(kmean_eval_df, use_container_width=True)

    elif selected_method == 'Agglomerative Clustering':
        fig = px.bar(
            AGG_eval_df, 
            x="linkage", 
            y="Silhouette_score", 
            color="Features Type",
            color_discrete_sequence=['#b8f4bc','#2596be'],
            barmode="group",
            title="Evaluation for Agglomerative Clustering",
            labels={"linkage": "Linkage Type", "Silhouette_score": "Silhouette Score"},
            text='Silhouette_score',
            height=600
        )
        st.plotly_chart(fig)
        with st.expander("See Agglomerative Dataframe"):
            st.dataframe(AGG_eval_df, use_container_width=True)

    elif selected_method == 'DBSCAN Clustering':
        fig = px.bar(
            DBSCAN_eval_df, 
            x='eps', 
            y='Silhouette_score', 
            color='min_samples',
            color_continuous_scale='Tealgrn',
            barmode='group',
            title='Evaluation for DBSCAN Clustering (Epsilon vs Min Samples)',
            labels={'eps': 'Epsilon', 'Silhouette_score': 'Silhouette Score'},
            height=600,
        )
        st.plotly_chart(fig)
        with st.expander("See DBSCAN Dataframe"):
            st.dataframe(DBSCAN_eval_df, use_container_width=True)

                                                                                                                                                        
    


with tab2:
    kmean_df = pd.read_csv("datasets/coffeeshop_kmeans_clustered.csv")
    kmean_sorted = kmean_df.sort_values(by='cluster', ascending=False)
    st.title("Clustering Segmentation Visualization")
    st.caption("The Clustering Segmentation Visualization dashboard offers a detailed view of data segmented into distinct clusters. It visually represents how data points are grouped, highlighting patterns and relationships within the segments. The dashboard helps users understand the characteristics of each cluster, enabling better decision-making for targeted strategies, such as marketing or customer profiling, based on the segmented data.")
    st.subheader("KMeans Clustering")
    kmean1,kmean2,kmean3 = st.columns(3, gap="medium")

    with kmean1: 

        fig = px.scatter(
            kmean_sorted, 
            x='product_name', 
            y='unit_price', 
            color='cluster',
            title='Product Name vs Unit Price Scatterplot',
            labels={'product_name': 'Product Name', 'unit_price': 'Unit Price'},
            color_discrete_sequence=['#207cb4', '#10346c', '#8CC1A9']
        )
        # Display in Streamlit
        st.plotly_chart(fig)

    with kmean2:
        # Create scatter plot
        fig = px.scatter(
            kmean_sorted, 
            x='total_qty', 
            y='unit_price', 
            color='cluster',
            title='Total Qty vs Unit Price Scatter Plot',
            labels={'total_qty': 'Total Quantity', 'unit_price': 'Unit Price'},
            color_discrete_sequence=['#207cb4', '#10346c', '#8CC1A9']
        )
        # Display in Streamlit
        st.plotly_chart(fig)


    with kmean3:
        # Create scatter plot
        fig = px.scatter(
            kmean_sorted, 
            x='city', 
            y='cluster', 
            color='total_qty',
            title='Scatter Plot of City vs Total Quantity by Cluster',
            labels={'city': 'City', 'cluster': 'Kategori Cluster'},
            color_discrete_sequence=['#207cb4', '#10346c', '#8CC1A9']
        )
        # Display in Streamlit
        st.plotly_chart(fig)

    with st.expander("Kmeans Conclusion"):
        kmeans_conclusion = """Berdasarkan Clustering Kmeans Clustering, terdapat 3 Cluster yang memberikan Segmentasi terhadap Kriteria Produk berdasarkan Harganya

    Cluster Standart merupakan Cluster Produk yang memiliki rentang harga 25.000 - 35.000.
    Cluster Standart merupakan Cluster Produk yang terdiri dari produk kopi seperti Espresso, Cappuccino, Macchiato, Latte dan Flat White.
        
    Cluster Premium merupakan Cluster Produk yang memiliki rentang harga 40.000 - 50.000.
    Cluster Premium merupakan Cluster Produk yang terdiri dari produk Makanan dan kopi seperti Cake, Sandwich dan Mocca.
        
    Cluster Cheap merupakan Cluster Produk yang memiliki rentang harga 15.000 - 20.000.
    Cluster Cheap merupakan Cluster Produk yang terdiri produk kopi dan non-kopi seperti Teh dan Americano.
        """
        st.markdown(kmeans_conclusion)

    add_vertical_space(3)
    st.subheader("Agglomerative Clustering Visualization")
    agg_df = pd.read_csv("datasets/coffeeshop_agg_clustered.csv")
    agg_sorted = agg_df.sort_values(by='cluster', ascending=False)
    agg1,agg2,agg3 = st.columns(3, gap="medium")

    with agg1:
        # Create scatter plot
        fig = px.scatter(
            agg_sorted, 
            x='product_name', 
            y='unit_price', 
            color='cluster',
            title='Product Name vs Unit Price Scatterplot',
            labels={'product_name': 'Product Name', 'unit_price': 'Unit Price'},
            color_discrete_sequence=['#207cb4', '#10346c', '#8CC1A9']
        )
        st.plotly_chart(fig)

    with agg2:
        # Create scatter plot
        fig = px.scatter(
            agg_sorted, 
            x='total_qty', 
            y='unit_price', 
            color='cluster',
            title='Total Qty vs Unit Price Scatter Plot',
            labels={'total_qty': 'Total Quantity', 'unit_price': 'Unit Price'},
            color_discrete_sequence=['#207cb4', '#10346c', '#8CC1A9']
        )
        # Display in Streamlit
        st.plotly_chart(fig)

    with agg3:
        # Create scatter plot
        fig = px.scatter(
            agg_sorted, 
            x='city', 
            y='cluster', 
            color='total_qty',
            title='Scatter Plot of City vs Total Quantity by Cluster',
            labels={'city': 'City', 'cluster': 'Kategori Cluster'},
            color_discrete_sequence=['#207cb4', '#10346c', '#8CC1A9']
        )
        # Display in Streamlit
        st.plotly_chart(fig)

    with st.expander("Agglomerative Clustering Conclusion"):
        agg_conclusion = """Berdasarkan Clustering Kmeans Clustering, terdapat 3 Cluster yang memberikan Segmentasi terhadap Kriteria Produk berdasarkan Harganya

    Cluster Standart merupakan Cluster Produk yang memiliki rentang harga 30.000 - 40.000.
    Cluster Standart merupakan Cluster Produk yang terdiri dari produk kopi seperti Cappuccino, Macchiato, Latte dan Flat White.
        
    Cluster Premium merupakan Cluster Produk yang memiliki rentang harga 45.000 dan 50.000.
    Cluster Premium merupakan Cluster Produk yang terdiri dari produk Makanan dan kopi seperti Cake, Sandwich dan Mocca.
        
    Cluster Cheap merupakan Cluster Produk yang memiliki rentang harga 15.000 - 25.000.
    Cluster Cheap merupakan Cluster Produk yang terdiri produk kopi dan non-kopi seperti Teh, Espresso dan Americano.
        """
        st.markdown(agg_conclusion)


    add_vertical_space(3)
    st.subheader("DBSCAN Clustering Visualization")
    dbscan_df = pd.read_csv("datasets/coffeeshop_dbscan_clustered.csv")
    dbscan_df = dbscan_df.sort_values(by='cluster', ascending=False)
    dbscan1,dbscan2,dbscan3 = st.columns(3, gap="medium")

    with dbscan1:
        # Create scatter plot
        fig = px.scatter(
            dbscan_df, 
            x='product_name', 
            y='unit_price', 
            color='cluster',
            title='Product Name vs Unit Price Scatterplot',
            labels={'product_name': 'Product Name', 'unit_price': 'Unit Price'},
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig)

    with dbscan2:
        # Create scatter plot
        fig = px.scatter(
            dbscan_df, 
            x='total_qty', 
            y='unit_price', 
            color='cluster',
            title='Total Qty vs Unit Price Scatter Plot',
            labels={'total_qty': 'Total Quantity', 'unit_price': 'Unit Price'},
            color_continuous_scale='Viridis'
        )
        # Display in Streamlit
        st.plotly_chart(fig)

    with dbscan3:
        # Create scatter plot
        fig = px.scatter(
            dbscan_df, 
            x='city', 
            y='cluster', 
            color='total_qty',
            title='Scatter Plot of City vs Total Quantity by Cluster',
            labels={'city': 'City', 'cluster': 'Kategori Cluster'},
            color_continuous_scale='Viridis'
        )
        # Display in Streamlit
        st.plotly_chart(fig)

    with st.expander("DBSCAN Conclusion"):
        dbscan_conclusion = """
    Berdasarkan Hasil Clustering dari DBSCAN, Algoritma DBSCAN gagal untuk membentuk Cluster yang sesuai sehingga semua data dianggap sebagai Noise.
    Hal ini disebabkan oleh karena data memiliki distribusi yang tidak teratur dan tidak memiliki hubungan yang signifikan antar data.
        """
        st.markdown(dbscan_conclusion)



with tab3:

    # Sort dataset by cluster
    kmean_sorted = kmean_df.sort_values(by='cluster', ascending=False)

    # Streamlit UI
    st.title("Clustering Segmentation with Custom Plot")

    # Create select boxes for x and y columns
    columns = kmean_sorted.columns.tolist()
    cus1,cus2 = st.columns(2, gap="medium")
    with cus1:
        x_axis = st.selectbox("Select X-axis:", columns, index=columns.index('product_name'))
    with cus2:
        y_axis = st.selectbox("Select Y-axis:", [col for col in columns if col != x_axis], index=columns.index('unit_price')-1)

    # Create scatter plot

    fig = px.scatter(
        kmean_sorted, 
        x=x_axis, 
        y=y_axis, 
        color='cluster',
        labels={x_axis: x_axis.replace('_', ' ').title(), y_axis: y_axis.replace('_', ' ').title()},
        color_discrete_sequence=['#207cb4', '#10346c', '#8CC1A9']
    )

    # Display plot
    st.markdown(f"#### KMeans Clustering {x_axis} vs {y_axis}")
    st.plotly_chart(fig)
    st.divider()

    
    agg_sorted = agg_df.sort_values(by='cluster', ascending=False)
    fig = px.scatter(
    agg_sorted, 
    x=x_axis, 
    y=y_axis, 
    color='cluster',
    labels={x_axis: x_axis.replace('_', ' ').title(), y_axis: y_axis.replace('_', ' ').title()},
    color_discrete_sequence=['#207cb4', '#10346c', '#8CC1A9']
    )
    st.markdown(f"#### Agglomerative Clustering {x_axis} vs {y_axis}")
    st.plotly_chart(fig)
    st.divider()

    dbscan_sorted = dbscan_df.sort_values(by='cluster', ascending=False)
    fig = px.scatter(
    dbscan_sorted, 
    x=x_axis, 
    y=y_axis, 
    color='cluster',
    labels={x_axis: x_axis.replace('_', ' ').title(), y_axis: y_axis.replace('_', ' ').title()},
    color_continuous_scale='Viridis'
    )
    st.markdown(f"#### DBSCAN Clustering {x_axis} vs {y_axis}")
    st.plotly_chart(fig)