import streamlit as st
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, add_page_title

from PIL import Image

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Instructions</h1>", unsafe_allow_html=True)
st.markdown('''To use **Find My Alien**, you must create an account. This can be done by going to the Login page, and selecting **Create Account**.
               
Once signed in, you can:
- **Create a new Find My Alien Puzzle**:
  1. Select the **Create** button
  2. Take a picture of anything you want
  3. Drag/drop the image of your choice
  4. Place the alien anywhere on your image (as hidden as possible!)
  5. Once you are happy, click **Publish** and wait for people to play on your image!

- **Play custom-made Where's My Alien Puzzles**:
  1. Select the **Browse** button
  2. Look through all the available puzzles and find the one you like most
  3. Press **Find Alien** and have fun!''')


# if st.button("Login"):
#     # session_state.key = True
#         switch_page('login')

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