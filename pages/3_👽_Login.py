import streamlit as st
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
import sys
sys.path.append('..')
from PIL import Image
from mongo.dbconfig import UsersDao
from st_pages import Page, show_pages, add_page_title


st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Login</h1>", unsafe_allow_html=True)

class SessionState:
    def __init__(self):
        self.logged_in = False

# Initialize the session state
session_state = SessionState()

def verify(login_username, login_password):
   if login_username and login_password:
        users_dao = UsersDao()
        user = {
        'username': login_username,
        'pass': login_password,
        }

        if users_dao.find_any(user):
             print("Success")
             st.success('Success wooop woop')
             session_state.logged_in = True
        else:
             print("Failure")
             st.error('Username/Password Combination Invalid')
   else:
        st.warning("No credentials provided")
   
   
with st.form("Login"):
        login_username = st.text_input('Username')
        login_password = st.text_input('Password', type='password')
        flag = st.form_submit_button('Login')

if flag:
        verify(login_username, login_password)  

if session_state.logged_in:
        st.sidebar.markdown("Logged in as: " + login_username)
        show_pages(
        [
                # Page("1_🌌_Home.py", "Home", "🌌"),
                Page("1_🌌_HomeLogIn.py", "Home", "🌌"),
                Page("pages/2_👾_Instructions.py", "Instructions", "👾"),
                # Page("pages/3_👽_Login.py", "Login", "👽"),
                Page("pages/4_🎮_Play.py", "Play", "🎮"),
                # Page("pages/5_🛸_Register.py", "Register", "🛸"),
        ]
)
