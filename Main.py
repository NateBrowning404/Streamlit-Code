import streamlit as st
from streamlit_option_menu import option_menu
from multiapp import MultiApp
from Pages import Home

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options = ["Home","Background","Contact"],
        icons= ["house","book","envelope"],
        menu_icon="cast"
        default_index=0,
        orientation="horizontal",
    )

if selected == "Home":
    st.title(f"You have selected Home")
if selected == "Background":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")

st.title("Test Site")
st.write("Please work, please")