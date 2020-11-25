import streamlit as st
from streamlit_ace import st_ace
import pandas as pd
import numpy as np

def tutorial(page):
    '''Tutorial to learn how to run Streamlit commands'''
    st.title(page)
    st.write("Now you can have a chance to try yourself! Combine things together and see what you get!")
    st.write(" ## Happy Streamlit-ing! :tada: :clap:")

    trial_code = st_ace('st.balloons()', font_size=15) 
    # need to save the work of people who input stuff 
    # checkbox to save work? 
    # button to put it back to start 
    exec(trial_code)
    return
