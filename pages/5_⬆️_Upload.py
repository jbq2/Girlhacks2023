import streamlit as st
import pandas as pd
from io import StringIO
from pymongo import MongoClient
import base64

# connect to mongo
client = MongoClient("")

uploaded_file = st.file_uploader("Choose an image", type=["png","jpg"])
submit_button = st.button("Submit")
clear_button = st.button("Clear")

if clear_button:
    st.warning().empty()
if submit_button:
    if uploaded_file is not None:
        # convert to Base64
        bytes_data = uploaded_file.getvalue()
        base64.b64encode(bytes_data)

        # insert into mongo
        image_data = {
            "username": "testname",
            "img_bson": bytes_data
        }

        collection.insert(image_data)
        st.write("File uploaded:", uploaded_file.name)

    else:
        st.warning("Please upload a file before submitting.")