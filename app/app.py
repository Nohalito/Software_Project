# Basic libraries
import pandas as pd

# Streamlit app
import streamlit as st

# Visualization library
import plotly.express as px

# Syntax
import re

# Path managment
import os
import sys
sys.path.append('.')
sys.path.append('./src')

# Custom libraries
import config as c
import function as f

# Multi page inspiration :
# https://mclachapp.streamlit.app/
# Multi page tutorial :
# https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation

gallery = st.Page("pages/gallery.py", title = "gallery", icon = "📸", default = True)
player_stat = st.Page("pages/player_stat.py", title = "Player stat", icon="🧮")
player_comparison = st.Page("pages/player_comparison.py", title = "Player comparison", icon = "⚖")

pg = st.navigation(
    {
        "Homepage": [gallery],
        "Player stat": [player_stat, player_comparison]
    }
)

pg.run()