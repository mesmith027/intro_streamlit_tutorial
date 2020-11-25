import streamlit as st
#from streamlit_ace import st_ace
#import pandas as pd
#import numpy as np
from setup_page import setup 
from basic_page import basic
from layout_page import layout 
from advanced_page import advanced
from tutorial_page import tutorial

# Run the program
if __name__ == '__main__':

    # Create a wide layout for the pages
    st.set_page_config(page_title='Streamlit cheat sheet',layout="wide")

    # Create a sidebar with all the page options for the expansion
    st.sidebar.markdown('Pick the page you wish to visit for a list of all the \
    possible functions and commands in Streamlit')
    page = st.sidebar.radio('Navigation', [
        'Setup and Command line',
        'Basic Commands',
        'Layout Commands',
        'Advanced Commands',
        'Tutorial'])

    # in side bar add links to the documentation and version this is based on
    st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v0.71.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    # run associated page program for each selection
    if page == 'Setup and Command line':
        setup(page)
    elif page == 'Basic Commands':
        basic(page)
    elif page == 'Layout Commands':
        layout(page)
    elif page == 'Advanced Commands':
        advanced(page)
    elif page == 'Tutorial':
        tutorial(page)
