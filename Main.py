import streamlit as st
from streamlit_option_menu import option_menu


selected = option_menu(
    #menu_title="Main Menu",
    options = ["Home","Background","Contact"],
    icons= ["house","book","envelope"],
    #menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)


st.title("Test Site")
st.write("Please work, please")