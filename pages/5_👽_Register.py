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
st.markdown("<h1 style='text-align: center;'>Register</h1>", unsafe_allow_html=True)

def verify(register_username, register_password):
	if register_username and register_password:
		users_dao = UsersDao()
		user = {
			'username': register_username,
			'pass': register_password,
		}

		if (len(users_dao.find_any(user)) == False):
			users_dao.insert_one(user)
			print("success in creating account")
			st.success('Account created successfully')
		else:
			st.error('Account already exists')
	else:
		st.warning("Missing username/password")
with st.form("Register"):
	register_username = st.text_input('Username')
	register_password = st.text_input('Password', type='password')
	flag = st.form_submit_button('Login')

if flag:
        verify(register_username, register_password)  


  