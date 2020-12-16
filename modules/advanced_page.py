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
# ****************** PROGRESS AND STATUS  ******************
    st.header('Progress and Status') 
    st.write("""These commands can be very useful for managing a users expectation if you are loading a large data set, running 
    an expensive computation or just wanting to keep your app user updates on whats happening behind the scenes! :eyes: 
    Lets see what cool things you can do to keep your user occupied while your app is updating.
    """)
    col1, mid, col2 = st.beta_columns([20,0.5,20])
    
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

        st.subheader("Information")
        st.write("You can use this to display info to your app user")
        st.code("""
st.info("You need to know this bit of info before continuing!")
        """)
        st.info("You need to know this bit of info before continuing!")
        st.markdown("---")

        st.subheader("Balloons")
        st.write("While this doesn't strictly tell the user information, it is a fun way to let them know something has happened!")
        st.code("""
st.balloons() 
        """)
        check = st.checkbox("See what balloons do", key = "balloon_run")
        if check: 
            st.balloons()

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
st.warning("Something may happen that I can't control....")
n = np.random.normal()
if n < 0: 
    st.write(n)
else: 
    st.write('Yup something happened!')
        """)

        st.warning("Something may happen that I can't control....")
        n = np.random.normal()
        if n < 0: 
            st.write(n)
        else: 
            st.write('Yup something happened!')
        st.markdown("---")

        st.subheader("Progress")
        st.write("This is similar to spinner, but allows you to increment how complete your task is!")
        st.code("""
my_bar = st.progress(0)  
for amount_complete in range(100): 
    time.sleep(0.1)
    my_bar.progress(amount_complete +1)
        """) 
        progress = st.checkbox("Run Progress code", key="progress_run")
        if progress: 
            my_bar = st.progress(0)  
            for amount_complete in range(100): 
                time.sleep(0.1)
                my_bar.progress(amount_complete +1)
        
        st.markdown("---")

        st.subheader("Exception")
        st.write("")
        st.code("""
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
        """)
        e = RuntimeError('This is an exception of type RuntimeError')
        st.exception(e)

# ****************** CONTROL FLOW  ******************
    st.markdown("---")
    st.header("Control Flow")
    # st.cache 
    # st.stop()
    # st.empty()
    # st.help()

# ****************** EXPERIMENTAL  ******************
    st.markdown("---")
    st.header("Experimental")

    exp1, mid, exp2 = st.beta_columns([20,0.5,20])

    with exp1: 
        st.subheader("show")

        st.subheader("rerun")


    with exp2:
        st.subheader("get query parameters")

        st.subheader("set query parameters")

    
   
    return
