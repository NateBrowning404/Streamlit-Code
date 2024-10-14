import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options = ["Home","Background","Contact"],
    )

if selected == "Home":
    st.title(f"You have selected Home")
if selected == "Background":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")

st.title("Test Site")
st.write("Please work, please")