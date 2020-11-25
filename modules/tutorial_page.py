import streamlit as st
from streamlit_ace import st_ace
import pandas as pd
import numpy as np
from modules.basic_page import basic
from modules.layout_page import layout 
from modules.advanced_page import advanced

def tutorial(page):
    '''Tutorial to learn how to run Streamlit commands'''
    st.title(page)
    st.write("Now you can have a chance to try yourself! Combine things together and see what you get!")
    st.write("## Happy Streamlit-ing! :tada: :clap:")

    # make a container to hold the st_ace editor, so that the pages can be desplayed below as sample code 
    # may not need this but going to try and see 
    container = st.beta_container() 
    with container: 
        trial_code = st_ace('st.balloons()', font_size=15) 
        # need to save the work of people who input stuff 
        # checkbox to save work? 
        # button to put it back to start 
        exec(trial_code)

    # choose to display any of the pages to see code
    st.markdown("---")
    st.write('Pick the page you want displayed below to list commands')
    page = st.radio('Navigation', [
        'Basic Commands',
        'Layout Commands',
        'Advanced Commands'])
    if page == 'Basic Commands':
        basic(page)
    elif page == 'Layout Commands':
        layout(page)
    elif page == 'Advanced Commands':
        advanced(page)
    return
