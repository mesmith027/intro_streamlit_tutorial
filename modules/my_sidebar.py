import streamlit as st

def sidebar():
    
    # Create a sidebar with all the page options for the expansion
    st.sidebar.markdown('Pick the page you wish to visit for a list of all the \
    possible functions and commands in Streamlit')
    page = st.sidebar.radio('Navigation', [
        'Information and Command line',
        'Basic Commands',
        'Layout Commands',
        'Advanced Commands',
        'Try it Yourself!'])

    # in sidebar add links to the documentation and version this is based on
    st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v0.71.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    #add streamlit logo
    #st.sidebar.image("img/row_1_col_0.png", width=100 )


    # return the page choice made by the user
    return page