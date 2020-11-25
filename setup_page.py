import streamlit as st

def setup(page):
    '''Main page for Streamlit Setup and Command line'''

    st.title(page)
    col1, col2 = st.beta_columns(2)

    with col1: 
        st.markdown('__How to install and import__')

        st.code('$ pip install streamlit')

        st.markdown('Import convention')
        st.code('>>> import streamlit as st')

        st.markdown('__How to uninstall__')
        st.code('''
pip uninstall streamlit
        ''')

        st.markdown('__Command line__')
        st.code('''
$ streamlit --help
$ streamlit run your_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version
$ pip install streamlit-nightly --upgrade
        ''')

    with col2:
        st.markdown('''
        1. What did I make and why: 
            * expansion on Daniel's popular Cheat Sheet
            * I felt that it needed 
                * some more use case examples
                * pictures of what the functions/widgets actually create
                * Streamlit is ALL about beautiful visuals!
        2. What parts of Streamlit does it showcase?
            * Ease of use
            * Demo aspects to new users 
            * print each page and create "cheat sheets"
        3. What did you learn?
            * Literally all the basic function calls 
            * Beta functions
            * there is no place to find experimental_ functions ([on docs](https://docs.streamlit.io/en/stable/#))!?
                * how do our users try out new things?
        ''')
    return