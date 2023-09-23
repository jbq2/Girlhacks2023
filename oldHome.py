import streamlit as st
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
from PIL import Image

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Find My Alien!!!</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Home", "Instructions", "Login"])



with tab1:
   # st.header("Home")
   description = '''Welcome to **Find My Alien!!!**

   Find a cheeky little alien in these user-uploaded images and get the best time!

   Upload your own images and send it to friends to see if they can find your alien!
   
   May the alien hunt begin!
   '''
   st.markdown(description)

with tab2:
   st.header("Instructions")
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
        