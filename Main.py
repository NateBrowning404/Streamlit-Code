import streamlit as st
from streamlit_option_menu import option_menu


selected = option_menu(
    menu_title = None,
    options = ["Home","Background","Contact"],
    functions = [lambda: run_home(), lambda: run_background(), lambda:run_contact()]
    icons= ["house","book","envelope"],
    #menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

def run_home():
    st.write("Running Home.py")
def run_background():
    st.write("Running Background.py")
def run_contact():
    st.write("Running Contact.py")