import streamlit as st

st.set_page_config(
    page_title="DORA Compliance Tracker",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

pg = st.navigation([
    st.Page("views/home.py",                          title="Home",                    icon="🏠", default=True),
    st.Page("pages/1_ICT_Risk_Management.py",         title="ICT Risk Management",     icon="🛡️"),
    st.Page("pages/2_Incident_Management.py",         title="Incident Management",     icon="🚨"),
    st.Page("pages/3_Resilience_Testing.py",          title="Resilience Testing",      icon="🧪"),
    st.Page("pages/4_Third_Party_Risk.py",            title="Third-Party Risk",        icon="🔗"),
    st.Page("pages/5_Information_Sharing.py",         title="Information Sharing",     icon="🔄"),
])
pg.run()
