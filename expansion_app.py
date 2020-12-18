import streamlit as st
import os 
import pickle as pkle
# unique modules 
from modules.setup_page import setup 
from modules.basic_page import basic
from modules.layout_page import layout 
from modules.advanced_page import advanced
from modules.tutorial_page import tutorial
from modules.my_sidebar import sidebar

# Run the program
if __name__ == '__main__':

    # determine page layout 
    if os.path.isfile('format.txt'):
        page_code = pkle.load(open('format.txt', 'rb'))
        exec(page_code)
        os.remove('format.txt')
    else: 
        st.set_page_config(page_title='Streamlit cheat sheet',layout="wide")

    # create the sidebar
    page = sidebar()

    # run associated page program for each selection
    if page == 'Information and Command line':
        setup(page)
    elif page == 'Basic Commands':
        basic(page)
    elif page == 'Layout Commands':
        layout(page)
    elif page == 'Advanced Commands':
        advanced(page)
    elif page == 'Try it Yourself!':
        tutorial(page)
