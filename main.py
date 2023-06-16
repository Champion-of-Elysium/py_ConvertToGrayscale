import streamlit as stlit
from PIL import Image

stlit.write('<span style="color:green; font-size:25px">` Here you can either <u>take a picture</u> or <u>upload an '
            'image</u> and '
            'deliver the <b>Grayscale image</b></span>.',
            unsafe_allow_html=True)

with stlit.expander("Start Camera"):
    # Start the camera
    camera_image = stlit.camera_input("Smile :)")

with stlit.expander("Upload Image"):
    # Upload Image
    uploaded_image = stlit.file_uploader("")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Display the grayscale image on the Webpage
    stlit.subheader('Result Image :')
    stlit.image(gray_img)

if uploaded_image:
    # Create a pillow image instance
    img = Image.open(uploaded_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Display the grayscale image on the Webpage
    stlit.subheader('Result Image :')
    stlit.image(gray_img)