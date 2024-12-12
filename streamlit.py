import streamlit as st

pages = {
    "Main Menus":
    [
        st.Page("pages/home.py", title="Home", icon=":material/home:"),
        st.Page("pages/about_us.py", title="About Us", icon=":material/info:"),
    ],

    "Dashboard":
    [
        st.Page("pages/dashboard.py", title="Insight Dashboard", icon=":material/bar_chart_4_bars:"),
        st.Page("pages/ml_dashboard.py", title="Clustering Dashboard", icon=":material/settings_applications:")
    ],
    "Chatbot":
    [
        st.Page("pages/chatbot.py", title="Chatbot", icon=":material/smart_toy:")
    ]
}



pg = st.navigation(pages)
pg.run()
st.logo("icons/coffee_ic.png", size="large")