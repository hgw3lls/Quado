# frontend/main.py

import streamlit as st
import requests

# defines an h1 header
st.title("Quado MVP")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def remote_css(url):
    st.markdown(
        f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True
    )


def icon(icon_name):
    st.markdown(
        f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True
    )


local_css("style.css")
remote_css("https://fonts.googleapis.com/icon?family=Material+Icons")

# icon("search")
selected = st.text_input("", "Enter research topic...")
# button_clicked = st.button("OK")

if st.button("search"):
    res = requests.get(
        "http://backend:8080/"
    )  # TO DO: LINK FRONT END AND BACKEND!
    # res = requests.get("http://0.0.0.0:8080")
    st.title(res.json())
