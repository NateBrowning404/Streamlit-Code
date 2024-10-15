import streamlit as st
from streamlit_option_menu import option_menu
import Home, Background,Contact


class MultiApp: 

    selected = option_menu(
        menu_title = None,
        options = ["Home","Background","Contact"],
        icons= ["house","book","envelope"],
        #menu_icon="cast",
        default_index=0,
        orientation="horizontal",
)

