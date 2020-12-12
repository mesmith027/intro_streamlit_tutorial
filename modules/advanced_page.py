import streamlit as st
import pandas as pd
import numpy as np
import time

def advanced(page):
    '''Advanced Streamlit commands'''
    st.title(page)
    st.write("""
    Blurb about advanced commands

    - not just for advanced users can be for anyone 
    - just give you advanced features and control over app and function
    """)

    st.header('Progress and Status') 
    st.write("""These commands can be very useful for managing a users expectation if you are loading a large data set, running 
    an expensive computation or just wanting to keep your app user updates on whats happening behind the scenes! :eyes: 
    Lets see what cool things you can do to keep your user occupied while your app is updating.
    """)
    col1, mid, col2 = st.beta_columns([20,0.5,20])
    #  progress, balloons, info, success, exception,
    
    with col1:
        st.subheader('Spinner')
        st.write("Use this when you want to let your user know things are happening in the backend")
        st.code(""" 
with st.spinner('working on it'): 
    time.sleep(5)
    st.write('done!')
        """)
        run_spinner = st.button("Run Spinner code?", key="spinner_run")
        if run_spinner: 
            with st.spinner('working on it'): 
                time.sleep(3)
                st.write("done!")
        
        st.markdown("---")

        st.subheader("Error")
        st.write("Use this to let your user know something went wrong, without breaking your app!")
        st.code("""
text = st.text_input("Type your name here")
if len(text) == 0: 
    st.error('You must enter your name to continue')
else: 
    st.write("Hey %s :wave:" %text)
        """)

        text = st.text_input("Type your name here")

        if len(text) == 0: 
            st.error('You must enter your name to continue')
        else: 
            st.write("Hey %s :wave:" %text)
        st.markdown("---")

    with col2: 
        st.subheader("Success")
        st.write("Use this when you want to let your user know that a task as been successful")
        st.code("""
column_names = ['a', 'b']
data = pd.DataFrame(np.random.randn(10,2), columns=column_names)
st.success("Created Pandas DataFrame")
        """)
        run_success = st.button("Run Success code?", key="success_run")
        if run_success:
            column_names = ['a', 'b']
            data = pd.DataFrame(np.random.randn(10,2), columns=column_names)
            st.success("Created Pandas DataFrame")
        st.markdown("---")

        st.subheader("Warning")
        st.write("Use this to let your user know something could go wrong")
        st.code("""
check = st.checkbox("Run this code")
if check: 
    st.info("Something may happen that I can't control....")
    n = np.random.normal()
    if n < 0: 
        st.write(n)
    else: 
        st.write('Yup something happened!')
        """)

        check = st.checkbox("Run this code", key="info_run")
        if check: 
            st.info("Something may happen that I can't control....")
            n = np.random.normal()
            if n < 0: 
                st.write(n)
            else: 
                st.write('Yup something happened!')
        st.markdown("---")

    # st.cache 
    # st.stop()
    # st.empty()
   
    return
