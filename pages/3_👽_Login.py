import streamlit as st
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
from PIL import Image

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Login</h1>", unsafe_allow_html=True)