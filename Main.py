import streamlit as st
from streamlit_option_menu import option_menu


selected = option_menu(
    menu_title = None,
    options = ["Home","Background","Contact"],
    icons= ["house","book","envelope"],
    #menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if st.button("Home"):
    st.switch_page("Home.py")
if st.button("Background"):
    st.switch_page("Background.py")
if st.button("Contact"):
    st.switch_page("Contact.py")