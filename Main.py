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

if selected == "Home":
    st.switch_page("Pages/Home.py")
if selected == "Background":
    st.switch_page("Pages/Background.py")
if selected == "Contact":
    st.switch_page("Pages/Contact.py")