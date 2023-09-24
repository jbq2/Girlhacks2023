import streamlit as st
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from streamlit_extras.let_it_rain import rain
from st_pages import Page, show_pages, add_page_title

st.set_page_config (
   page_title="Find My Alien!!!",
   page_icon="👽"
)

rain(
    emoji="🛸",
    font_size=54,
    falling_speed=8,
    animation_length="infinite",
)


# class SessionState:
#     def __init__(self):
#         self.logged_in = False

# # Initialize the session state
# session_state = SessionState()

# @st.cache_resource
# st.session_state.logged_in = False

# if not st.session_state.logged_in:
#     show_pages(
#         [
#             Page("1_🌌_Home.py", "Home", "🌌"),
#             # Page("1_🌌_HomeLogIn.py", "Home", "🌌"),
#             Page("pages/2_👾_Instructions.py", "Instructions", "👾"),
#             Page("pages/3_👽_Login.py", "Login", "👽"),
#             # Page("pages\4_🎮_Play.py", "Instructions", "🎮"),
#             Page("pages/5_🛸_Register.py", "Register", "🛸"),
#         ]
#     )
st.markdown("<h1 style='text-align: center;'>Find My Alien!!!</h1>", unsafe_allow_html=True)
# st.sidebar.success("Select a page above.")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

# st.markdown("<h1 style='text-align: center;'>Find My Alien!!!</h1>", unsafe_allow_html=True)

# st.header("Home")
description = '''Welcome to **Find My Alien!!!**

Find a cheeky little alien in these user-uploaded images and get the best time!

Upload your own images and send it to friends to see if they can find your alien!

May the alien hunt begin!
'''
st.markdown('''Welcome to **Find My Alien!!!**

Find a cheeky little alien in these user-uploaded images and get the best time!

Upload your own images and send it to friends to see if they can find your alien!

May the alien hunt begin!''')

st.markdown("insert login and instruction buttons here")

# st.button("Login", type="primary")
# st.button("Instructions", type="primary")




if st.button("Instructions"):
    # session_state.key = True
        switch_page('instructions')

# if st.button("Login"):
#     # session_state.key = True
#         switch_page('login')


