import streamlit as st
from utils.ui_components import render_pillar_page

st.set_page_config(page_title="Third-Party Risk — DORA", page_icon="🔗", layout="wide")
render_pillar_page("third_party")
