import streamlit as st
import pandas as pd
import numpy as np
import time

def layout(page):
    '''Layout Streamlit commands'''
    st.title(page)
    st.write('''This page lists the layout commands (currently in beta) that are available in Streamlit. They are not yet integrated 
    into the basic Streamlit functions and therefore may not always work in unique (edge) cases. If you believe you have 
    encountered such a case please let us know on the [Streamlit Community Platform](https://discuss.streamlit.io/)''')

# ***************** COLUMNS SECTION ****************
    st.header('Columns')
    st.subheader('Columns of Equal Size')
    st.code('''
col1,col2 = st.beta_columns(2)
col1.image('img/brain.png', caption= "This ia a blue brain!")
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['a', 'b', 'c'])
col2.write(data)''')
    
    col1,col2 = st.beta_columns(2)
    col1.image('img/brain.png', caption= "This ia a blue brain!")
    data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['a', 'b', 'c'])
    col2.subheader('A Dataframe')
    col2.write(data)

    st.subheader('Columns of Different Sizes')
    st.code('''
col3,col4,col5 = st.beta_columns([1,2,3]) 
# 3 columns where first is the smallest, the second is 2x the size of the first and 3rd is 3x the first
col3.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
with col4: 
    st.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
with col5: 
    st.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
    ''')
    col3,col4,col5 = st.beta_columns([1,2,3]) 
    # 3 columns where first is the smallest, the second is 2x the size of the first and 3rd is 3x the first
    col3.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
    with col4: 
        st.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
    with col5: 
        st.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")

    st.subheader('Columns to Make a Grid')
    st.code('''
for i in range(1,3): # number of rows in your table! = 2
    cols = st.beta_columns(2) # number of columns in each row! = 2
    # first colum if the ith row
    cols[0].image('img/row_%i_col_0.png' %i, use_column_width=True)
    cols[1].image('img/row_%i_col_1.jpg' %i, use_column_width=True)
    ''')
    for i in range(1,3): # number of rows in your table! = 2
        cols = st.beta_columns(2) # number of columns in each row! = 2
        # first colum if the ith row
        cols[0].image('img/row_%i_col_0.png' %i, use_column_width=True)
        cols[1].image('img/row_%i_col_1.jpg' %i, use_column_width=True)

# ***************** CONTAINERS SECTION *************************
    st.header('Containers')
    st.write('''you may want to create a container to _________. A cool feature of containers, 
    it that it allows you to place things 'out of order'. ''')
    st.subheader('Container using with')
    st.code(''' 
with st.beta_container():
    st.write("This bar graph is inside the container")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))
    ''')
    with st.beta_container():
        st.write("This bar graph is inside the container")
        st.bar_chart(np.random.randn(50, 3))

    st.subheader('Container out of order')
    st.code(''' 
container = st.beta_container() 
container.write("This button is inside a container")
button = container.button('Press Me and see something to blow your mind!')
if button:
    st.header("Voila!! The order is backwards!")
   
container.write("This is _after_ the if button statement, but comes _before_ the 'Voila!!'")
    ''')
    container = st.beta_container() 
    container.write("This button is inside a container")
    button = container.button('Press Me and see something to blow your mind!', key='container_button_run')
    if button:
        st.header("Voila!! The order is backwards!")
   
    container.write("This is _after_ the if button statement, but comes _before_ the 'Voila!!'")

# ********************* EXPANDER SECTION *******************
    st.header("Expander")
    st.write('''The expander allows you to hide sections that you may not always want expanded. 
    When the user clicks the expander, it *__does not__* rerun the script, so this can be useful 
    for housing additional widgets.''')
    st.code(''' 
with st.beta_expander('Expand Me'): 
    st.write('Well hello there!')
    st.balloons()''')

    with st.beta_expander('Expand Me'): 
        st.write('Well hello there!')
        st.balloons()

# ********************* SIDEBAR SECTION *******************
    st.header('Sidebar')
    st.write(''' 
You may have noticed the handy sidebar to your left :point_left:

If you would like to create your own you simply need to add `sidebar` before you call a streamlit function. For example:''')

    st.code('''
# use st.sidebar.<widget> notation
sidebar_button = st.sidebar.button("Your button added to the sidebar!")
if not sidebar_button: # if the button is NOT clicked display this message
    st.sidebar.markdown('You added a widget to the sidebar!')

    ''')
    add_sidebar = st.button('Run this code to add to the sidebar')
    if add_sidebar: 
        a = st.sidebar.button("Click here to remove your button", key='sidebar_button_run')
        if not a:
            st.sidebar.markdown('You added a widget to the sidebar!')
    
    st.write('''
NOTE: The `st.sidebar.<function>`notation works for basically ALL the streamlit functions. However, there are a few that it _doesn't_
work with, those we have listed here (as it's shorter to list the few it doesn't work with): 

functions that will cause an error (and their workarounds):

-  :exclamation: :x: `st.sidebar.echo()`
    - :white_check_mark: `st.sidebar.code()`
- :exclamation: `st.sidebar.spinner()`
    - :white_check_mark: no current workarounds :disappointed:
    ''') #:heavy_multiplication_x: ideal: :X: (big red X from slack)
    return