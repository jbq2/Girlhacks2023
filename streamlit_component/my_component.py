import streamlit as st
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "mycomponent",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "dist")
    _component_func = components.declare_component(
        "mycomponent", path=build_dir
    )

def my_component(image_src, base_image_src, key=None):
    component_value = _component_func(imageSrc=image_src, baseImageSrc=base_image_src, key=key)
    return component_value