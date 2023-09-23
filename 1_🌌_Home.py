import streamlit as st
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

st.set_page_config (
   page_title="Find My Alien!!!",
   page_icon="👽"
)

st.markdown("<h1 style='text-align: center;'>Find My Alien!!!</h1>", unsafe_allow_html=True)
st.sidebar.success("Select a page above.")
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

if st.button("Login"):
    # session_state.key = True
        switch_page('login')


