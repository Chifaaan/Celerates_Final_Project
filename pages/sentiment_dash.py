import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Celerates's Group 9",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="icons/smart_toy.svg")

df = pd.read_csv("sentiment_analysis.csv")

# Data Distribution
sentiment_counts = df['sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['Sentiment', 'Count']

df['Platform'] = df['Platform'].str.strip().str.lower()
platform_counts = df['Platform'].value_counts().reset_index()
platform_counts.columns = ['Platform', 'Count']

# Calculate texts per year
texts_per_year = df.groupby('Year').size().reset_index(name='Text Count')

st.title("Sentiment Analysis Dashboard")

col1,col2,col3 = st.columns([2, 4, 2.5], gap="medium")


with col1:
    # Create a Pie Chart
    fig = px.pie(
        sentiment_counts, 
        names='Sentiment', 
        values='Count',
        color_discrete_sequence=[ '#377eb8','#5BC66D', '#e41a1c'],
        title='Sentiment Distribution',
    )
    fig.update_traces(textinfo='percent+label', textfont_size=18, marker=dict(line=dict(color='#000000',width=1)))
    st.plotly_chart(fig)

    fig = px.pie(
        platform_counts, 
        names='Platform', 
        values='Count', 
        color_discrete_sequence=[ '#DD2A7B','#0068c9', '#83c9ff'],
        title='Platform Distribution',
        
)
    fig.update_traces(textinfo='percent+label', textfont_size=18, marker=dict(line=dict(color='#000000',width=1)))
    st.plotly_chart(fig)

with col2:
    fig = px.bar(
        texts_per_year,
        x='Year',
        y='Text Count',
        title='Number of Texts Sent Per Year',
        labels={'Year': 'Year', 'Text Count': 'Number of Texts'},
        text='Text Count'
    )
    # Update layout for better visualization
    fig.update_layout(xaxis=dict(tickmode='linear'))    
    fig.update_traces(textposition='outside')

    st.plotly_chart(fig)

    # Group by Year and Sentiment, and count occurrences
    sentiment_trend = df.groupby(['Year', 'sentiment']).size().reset_index(name='Count')

    # Create a Plotly line chart
    fig = px.line(
        sentiment_trend,
        x='Year',
        y='Count',
        color='sentiment',
        markers=True,
        title='Sentiment Trends Per Year',
        labels={'Year': 'Year', 'Count': 'Number of Texts', 'sentiment': 'Sentiment'}
    )
    fig.update_layout(
        xaxis=dict(tickmode='linear'),
        legend=dict(yanchor="top",xanchor="left",x=0.01, y=0.99)
        )
    st.plotly_chart(fig)


with col3:
    # Group the data by Platform and Sentiment to get counts
    platform_sentiment_counts = df.groupby(['Platform', 'sentiment']).size().reset_index(name='Count')
    # Create a bar chart for Platform vs Sentiment
    fig = px.bar(
        platform_sentiment_counts,
        x='Platform',
        y='Count',
        color='sentiment',
        color_discrete_sequence=[ '#e41a1c','#377eb8','#5BC66D' ],
        barmode='group',
        title='Platform vs Sentiment Distribution',
        labels={'Platform': 'Platform', 'Count': 'Number of Texts', 'sentiment': 'Sentiment'}
    )


    # Show the plot
    st.plotly_chart(fig)


    # Group by 'Time of Tweet' and 'Platform' to get counts
    time_platform_counts = df.groupby(['Time of Tweet', 'Platform']).size().reset_index(name='Count')

    # Create a Plotly bar chart
    fig = px.bar(
        time_platform_counts,
        x='Time of Tweet',
        y='Count',
        color='Platform',
        color_discrete_sequence=[ '#0068c9','#DD2A7B', '#83c9ff'],
        barmode='group',
        title='Time of Tweet vs Platform',
        labels={'Time of Tweet': 'Time of Tweet', 'Count': 'Number of Tweets', 'Platform': 'Platform'}
    )

    st.plotly_chart(fig)



st.markdown("#### Sentiment Analysis Dataset table")
st.dataframe(df, use_container_width=True)