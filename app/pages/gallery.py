import os

# Streamlit app
import streamlit as st

# Pillow
from PIL import Image

# ----------------------------
# => Page config
# ----------------------------
st.set_page_config(
    page_title = "NBA Player Explorer",
    layout = "centered"
)

st.title("📸 NBA gallery")

# CAROUSELLLLLLL MI AMOR

# Load images
image_dir = "app/assets/"
images = [os.path.join(image_dir, img) for img in os.listdir(image_dir)]
images.sort()

# Session state to track index
if "img_index" not in st.session_state:
    st.session_state.img_index = 0

# Navigation buttons
col1, col2, col3 = st.columns([1, 5, 1])

with col1:
    if st.button("⬅️ Prev"):
        st.session_state.img_index = (st.session_state.img_index - 1) % len(images)

with col3:
    if st.button("Next ➡️"):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(images)

# Display image
image = Image.open(images[st.session_state.img_index])
st.image(image, use_container_width=True)