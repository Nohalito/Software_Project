# Streamlit app
import streamlit as st
import streamlit.components.v1 as components

# ----------------------------
# => Page config
# ----------------------------
st.set_page_config(
    page_title = "NBA Player Explorer",
    layout = "wide"
)

st.title("📸 NBA gallery")

# Gallery :
st.image("app/assets/Wade-Lebron-Dunk.jpg")

st.image("app/assets/Lebron-is-absolutely-charming.png")

st.image("app/assets/lebron.gif")