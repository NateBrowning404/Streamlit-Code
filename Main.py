import streamlit as st
from streamlit_option_menu import option_menu
import Home, Background,Contact


class MultiApp: 

    def __init__(self):
        self.apps = []
    def add_app(self,title,function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        selected = option_menu(
            menu_title = None,
            options = ["Home","Background","Contact"],
            icons= ["house","book","envelope"],
            #menu_icon="cast",
            default_index=1,
            styles={
                "container": {"background-color":'blue'},
                "icon": {"color": "white"},
                "nav-link": {"color": "white"},
                "nav-link-selected": {"background-color": "yellow"},
            }
            orientation="horizontal",

            if app == 'Home':
                Home.app()
            if app == 'Background':
                Background.app()
            if app == 'Contact':
                Contact.app()

    run()
)

