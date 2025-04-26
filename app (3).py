
import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Deforestation Detection App",
    page_icon=":deciduous_tree:",
    layout="wide"
)

# Title and subheader
st.markdown("<h1 style='text-align: center; color: green;'>🌳 Deforestation Detection App 🌳</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: darkgreen;'>Upload your satellite image to check for deforestation! </h4>", unsafe_allow_html=True)

# Upload section
uploaded_file = st.file_uploader("🌍 Choose a satellite image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='📸 Uploaded Satellite Image', use_column_width=True)
    st.markdown("<h3 style='color: green;'>Analyzing the Image...</h3>", unsafe_allow_html=True)

    # Dummy "Deforestation" Detection
    img_array = np.array(image)
    green_pixels = np.sum((img_array[:, :, 1] > img_array[:, :, 0]) & (img_array[:, :, 1] > img_array[:, :, 2]))

    if green_pixels < 5000:
        st.error("⚠️ WARNING: Deforestation detected. Please take action!")
    else:
        # Added healthier forest message if more green pixels are detected
        st.success("✅ Healthy Forest: No signs of deforestation!")
        st.write("🌱 Keep it up! Consider planting more trees to maintain the health of this forest!")

    # Show Pie Chart
    green = green_pixels
    not_green = img_array.shape[0] * img_array.shape[1] - green_pixels

    st.markdown("<h4 style='color: darkgreen;'>🌱 Forest Health Analysis:</h4>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    ax.pie(
        [green, not_green], 
        labels=['Green Area', 'Non-Green Area'], 
        autopct='%1.1f%%',
        colors=['limegreen', 'saddlebrown']
    )
    st.pyplot(fig)

    st.balloons()
