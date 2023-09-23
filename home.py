import streamlit as st
from PIL import Image

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

   # insert gif here
   
# with tab2:
#    st.header("Instructions")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#    st.header("Login")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)