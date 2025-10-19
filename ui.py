import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


st.set_page_config(page_title="🧠 OCR Text Extractor", page_icon="🧾", layout="wide")
st.title("🧾 Image to Text Extractor (OCR)")
st.write("Upload an image and extract text using **Tesseract OCR** 🧠")


uploaded_file = st.file_uploader("📁 Upload an image file", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image for OpenCV
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # OCR Extraction
    text = pytesseract.image_to_string(thresh)

    # Display extracted text
    st.subheader("📜 Extracted Text")
    st.text_area("Output Text", text, height=250)

    # Download button
    st.download_button(
        label="💾 Download Extracted Text",
        data=text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )

else:
    st.info("👆 Upload an image file to begin text extraction.")
