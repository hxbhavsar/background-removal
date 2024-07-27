import streamlit as st

# Set page config for better mobile experience
# This must be the first Streamlit command
st.set_page_config(layout="wide", page_title="Image Background Remover", initial_sidebar_state="expanded")

# Now import other necessary libraries
from rembg import remove
from PIL import Image, ImageFilter
from io import BytesIO
import base64
import time
import json
import os

# Function definitions
def display_logo(logo_path):
    with open(logo_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .logo {{
            position: absolute;
            top: 10px;
            left: 10px;
            width: 150px;
            height: auto;
        }}
        </style>
        <img class="logo" src="data:image/png;base64,{encoded_string}">
        """,
        unsafe_allow_html=True
    )

@st.cache(allow_output_mutation=True)
def remove_background(image):
    return remove(image)

def create_preview(image, size=(300, 300)):
    preview = image.copy()
    preview.thumbnail(size)
    return preview

def apply_custom_background(foreground, background):
    if background.mode != 'RGBA':
        background = background.convert('RGBA')
    background = background.resize(foreground.size, Image.LANCZOS)
    composite = Image.alpha_composite(background, foreground)
    return composite

def save_settings(settings):
    with open('settings.json', 'w') as f:
        json.dump(settings, f)

def load_settings():
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as f:
            return json.load(f)
    return {}

st.sidebar.write("## Upload and Download :gear:")

MAX_FILE_SIZE = 20 * 1024 * 1024  # 5MB

# Convert image to bytes
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG", quality=95)  # Save with high quality
    byte_im = buf.getvalue()
    return byte_im

# Process and remove background from image
def fix_image(upload, blur_radius):
    try:
        image = Image.open(upload)
        col1.write("Original Image :camera:")
        col1.image(image)

        # Remove background
        fixed = remove(image)

        # Apply blur if specified
        if blur_radius > 0:
            fixed = fixed.filter(ImageFilter.GaussianBlur(blur_radius))
            
        col2.write("Transformed Image :wrench:")
        col2.image(fixed)
        st.sidebar.markdown("\n")
        st.sidebar.download_button("Download transformed image", convert_image(fixed), "transformed.png", "image/png")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit columns for image display
col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Blur radius input
blur_radius = st.sidebar.slider("Select blur radius", 0, 10, 0)

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload, blur_radius=blur_radius)
else:
    st.write("Please upload an image to see the background removal and blur effect.")
