import streamlit as st
import pandas as pd
import sys
from io import StringIO
from pymongo import MongoClient
import base64
sys.path.append('..')
from mongo.dbconfig import ImagesDao
import streamlit.components.v1 as components
import streamlit_component.my_component as my_component

# connect to mongodb
users_dao = ImagesDao()

uploaded_file = st.file_uploader("Choose an image", type=["png","jpg"])

if uploaded_file is not None:
    # Display the uploaded image as HTML
    # Read the image file as bytes
    image_bytes = uploaded_file.read()
    # Encode the image bytes as base64
    image_base64 = base64.b64encode(image_bytes).decode()
    result = my_component.my_component("https://cdn.discordapp.com/attachments/1153737878099218473/1155351824736456785/alien.png", image_base64)
    # st.markdown(f'<img src="data:image/png;base64,{image_base64}" alt="Uploaded Image">', unsafe_allow_html=True)


submit_button = st.button("Submit")


if submit_button:
    if uploaded_file is not None:
        # convert to Base64
        bytes_data = uploaded_file.getvalue()
        image_base64 = base64.b64encode(bytes_data).decode()
        st.markdown(result)
        # insert into mongo
        image_data = {
            "username": "testname",
            "img_bson": image_base64,
            "coordinates": result
        }

        try:
            users_dao.insert_one(image_data)
            st.success(f'Successfully Uploaded: {uploaded_file.name}')
        except:
            st.error(f'Failed Upload: {uploaded_file.name}')

    else:
        st.warning("Please upload a file before submitting.")