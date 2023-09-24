import sys

from st_pages import Page, _show_pages, _show_pages_from_config
from streamlit_extras.switch_page_button import switch_page
sys.path.append('..')
from mongo.dbconfig import DbConnection, ImagesDao, LeaderboardDao, UsersDao
import streamlit as st
import pandas as pd

from st_aggrid import AgGrid

@st.cache_resource
def cache_db_conn():
       return DbConnection()

DB_CONN = cache_db_conn()

@st.cache_resource
def cache_daos(_db_conn):
    return {
        'USERS_DAO': UsersDao(_db_conn),
        'IMAGES_DAO': ImagesDao(_db_conn),
        'LEADERBOARD_DAO': LeaderboardDao(_db_conn)
    }

DAOS = cache_daos(DB_CONN)

leaderboard_dao = DAOS['LEADERBOARD_DAO']

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Leaderboard</h1>", unsafe_allow_html=True)

data = sorted(leaderboard_dao.find_any(), key=lambda stat: stat['time'], reverse=False)
stats = pd.DataFrame(data, [i + 1 for i in range(len(data))]) # [i + 1 for i in range(len(data))]
stats.columns = ['Position', 'Username', 'Time', 'Number of Images']
stats.drop(stats.columns[[0]], axis=1, inplace=True)
stats.drop(stats.index[10:], axis=0)
html = stats.to_html(classes='center_df')
print(stats)

if st.session_state.logged_in:
        st.sidebar.markdown("Logged in as: " + st.session_state.username)
        log_out = st.sidebar.button("Log Out")
        if log_out:
                _show_pages(
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

style = """
<style>
    .center_df {
        margin: auto;
    }
</style>
"""
st.markdown(f'{style}{html}', unsafe_allow_html=True)