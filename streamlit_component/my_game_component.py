import streamlit as st
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    game_component_func = components.declare_component(
        "mygamecomponent", 
        url="http://localhost:3000"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "dist")
    game_component_func = components.declare_component(
        "mygamecomponent", path=build_dir
    )

def my_game_component():
    return game_component_func()