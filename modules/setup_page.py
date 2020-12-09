import streamlit as st

def setup(page):
    '''Main page for Streamlit Setup and Command line'''

    st.title(page)
    st.markdown('''
    Streamlit was created to bring data science insights and app making together into one easy to use, seamless environment. 
    Here are some ways streamlit might be useful in your life: 

    - Demo a complex subject interactively to help people learn
        - [Like this Monte Carlo app](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)
    - Share machine learning algorithms 
        - example machine learning dashboard
    - 
    ''')

    col1, col2 = st.beta_columns(2)
    with col1:
        st.markdown('''
        
        ''')

    with col2: 
        st.markdown('__Import convention__')

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
    return