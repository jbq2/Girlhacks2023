import streamlit as st
# import streamlit_authenticator as stauth
import streamlit.components.v1 as components
from mongo.dbconfig import UsersDao

users_dao = UsersDao()

st.markdown("# Where's My Alien?!")
components.html('''  
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body, html {
            margin: 0;  
            padding: 0;
            height: 100%;
            overflow: hidden; /* To prevent scroll if image is too big */
        }

        #background-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1; /* Place the image behind content */

            /* Adjust the image's opacity and brightness */
            opacity: 0.5;
            filter: brightness(50%);
        }

        .content {
            padding: 20px;
        }
    </style>
   <img id="background-image" src=https://media.tenor.com/IIQ-ca9nBu0AAAAd/space.gif alt="Background">

</head>
</html>
''' )

tab1, tab2, tab3, tab4= st.tabs(["Home", "Instructions", "Login", "Test"])

with tab1:
   st.header("Home")
   st.image("https://media.tenor.com/IIQ-ca9nBu0AAAAd/space.gif")
   description = '''Welcome to **Find My Alien!**

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
   
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


def verify():
   user = {
      'username': st.session_state.login_username,
      'pass': st.session_state.login_password,
    }
   print(users_dao.find_any(user))

with tab3:
   with st.form("Login"):
      login_username = st.text_input('Username')
      login_password = st.text_input('Password', type='password')
      st.form_submit_button('Login', on_click=verify)
   

with tab4:
   st.header("Test")


