import streamlit as st
import streamlit.components.v1 as components
from st_pages import Page, show_pages, add_page_title
import streamlit_component.my_game_component as my_game_component

st.markdown("# Where's My Alien?!")
result = my_game_component.my_game_component()
st.write(result)
st.markdown("## Instructions")
st.markdown("Look for and click on all the aliens!")
st.markdown("Your time will be submitted on the leaderboard once you finish!")

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
                    ]
                )
                switch_page("Home")