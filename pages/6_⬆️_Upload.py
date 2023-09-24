import streamlit as st
import pandas as pd
import sys
from io import StringIO
from pymongo import MongoClient
import base64
sys.path.append('..')
from mongo.dbconfig import ImagesDao
from mongo.dbconfig import DbConnection, ImagesDao, LeaderboardDao, UsersDao
import streamlit.components.v1 as components
import streamlit_component.my_component as my_component
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page

@st.cache_resource
def cache_db_conn():
       return DbConnection()

DB_CONN = cache_db_conn()

@st.cache_resource
def cache_daos(_db_conn):
    return {
        'USERS_DAO': UsersDao(_db_conn),
        'IMAGES_DAO': ImagesDao(_db_conn),
        'LEADERBOARD_DAO': LeaderboardDao(_db_conn)
    }

DAOS = cache_daos(DB_CONN)

images_dao = DAOS['IMAGES_DAO']

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

st.write(st.session_state.username)


if submit_button:
    if uploaded_file is not None:
        # convert to Base64
        bytes_data = uploaded_file.getvalue()
        image_base64 = base64.b64encode(bytes_data).decode()
        st.markdown(result)
        # insert into mongo
        image_data = {
            "username": st.session_state.username,
            "img_bson": bytes_data,
            "coordinates": result
        }


        try:
            images_dao.insert_one(image_data)
            st.success(f'Successfully Uploaded: {uploaded_file.name}')
        except:
            st.error(f'Failed Upload: {uploaded_file.name}')

    else:
        st.warning("Please upload a file before submitting.")


if st.session_state.logged_in:
        st.sidebar.markdown("Logged in as: " + st.session_state.username)
        log_out = st.sidebar.button("Log Out")
        if log_out:
                show_pages(
                    [
                        Page("1_🌌_Home.py", "Home", "🌌"),
                        Page("pages/2_👾_Instructions.py", "Instructions", "👾"),
                        Page("pages/3_👽_Login.py", "Login", "👽"),
                        # Page("pages\4_🎮_Play.py", "Instructions", "🎮"),
                        Page("pages/5_🛸_Register.py", "Register", "🛸"),
                        Page("pages/6_⬆️_Upload.py", "Upload", "⬆️"),
                        Page("pages/7_Leaderboard.py", "Leaderboard", "⬆️")
                    ]
                )
                switch_page("Home")