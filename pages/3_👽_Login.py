import streamlit as st
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
import sys
sys.path.append('..')
from PIL import Image
from mongo.dbconfig import UsersDao

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Login</h1>", unsafe_allow_html=True)

def verify(login_username, login_password):
   users_dao = UsersDao()
   user = {
      'username': login_username,
      'pass': login_password,
    }

   print(users_dao.find_any(user))
   
with st.form("Login"):
        login_username = st.text_input('Username')
        login_password = st.text_input('Password', type='password')
        st.form_submit_button('Login', on_click=verify(login_username, login_password))