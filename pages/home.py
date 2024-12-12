import streamlit as st

st.set_page_config(
    page_title="Celerates's Group 5",
    layout="centered",
    initial_sidebar_state="expanded",
    page_icon="icons/coffee_ic.png")

data_source = 'https://drive.google.com/drive/folders/1N9Trq6S8WoboCGiyi7dHoeXu4HrPo2YH'
welcome = ''' This app proudly showcases our teamwork and the power of machine learning through a **Coffee Shop Transaction** dashboard. You can access the Dataset [here](%s)

 🎉Coffee Shop Transaction Dataset, brought to life by the talented\n
:green-background[Team Project 5 from the Celerates Data Science Track], under the expert guidance of ***Mentor Rusnanda Farhan***. 🌟

Dive into the visualization of insights, where every click unravels the journey of coffeeshop analysis. Whether you're a data enthusiast, a curious learner, or just exploring, this space is built for discovery and inspiration.'''



st.title("Welcome to Our Dashboard")
st.markdown(welcome % data_source, unsafe_allow_html=True)

feat, tech = st.columns(2, gap="medium")
feat.markdown("### Features:")
feat.markdown("1.Home page")
feat.markdown("2.Visualization of insights")
feat.markdown("3.Chatbot of our Analysis")
feat.markdown("4.About us Page")


tech.markdown("### Technologies:")
tech.markdown("1. Python")
tech.markdown("2. Pandas")
tech.markdown("3. Matplotlib")
tech.markdown("4. Plotly")
tech.markdown("5. Streamlit")
tech.markdown("6. Streamlit-Extras")
tech.markdown("7. Streamlit-Elements")
tech.markdown("8. Langchain")
tech.markdown("9. Langchain-Google-Ai")


st.divider()

col1, col2, col3 = st.columns(3)


with col1:
    st.caption("You can see About Us page here")
    st.page_link("pages/about_us.py",label=":material/info: About Us", use_container_width=True)
with col2:
    st.caption("You can see our Analysis in Dashboard here")
    st.page_link("pages/dashboard.py",label=":material/bar_chart_4_bars: Dashboard", use_container_width=True)
    st.page_link("pages/ml_dashboard.py",label=":material/settings_applications: Clustering", use_container_width=True)
with col3:
    st.caption("You can ask questions to our Chatbot here")
    st.page_link("pages/chatbot.py", label=":material/smart_toy: Chatbot", use_container_width=True)