import streamlit as st
from utils.ui_components import render_pillar_page

st.set_page_config(page_title="ICT Risk Management — DORA", page_icon="🛡️", layout="wide")
render_pillar_page("ict_risk")
