import streamlit as st

def setup(page):
    '''Main page for Streamlit Setup and Command line'''

    st.title(page)
    st.markdown('''
    Streamlit was created to bring data science insights and app making together into one easy to use, seamless environment. 
    __Fun fact:__ Streamlit got its name [from a typo](https://discuss.streamlit.io/t/why-is-streamlit-called-streamlit/339)! :laughing:
    ''')

    col1, mid, col2 = st.beta_columns([20,0.5,20])
    with col1:
        st.markdown('''
    Here are some ways Streamlit might be useful in your life: 
    - Demo a complex subject interactively to help people learn
        - [Like this Monte Carlo app](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)
    - Share machine learning algorithms 
        - [Checkout this Emoji Recommender](https://share.streamlit.io/rensdimmendaal/emoji-recommender/main/app/streamlit.py)
    - Create a interactive resume/portfolio that dynamically showcases your skills! 
        - link to resume template

    As you become more advanced, you can publish your apps for __free__ with Streamlit Sharing! :smile: Checkout how to get an invite to the 
    [Sharing platform here](https://www.streamlit.io/sharing)

    If you run into any issues, want to show off what you have built, or you just want to hangout with other Streamlit community members 
    checkout our [community forum](https://discuss.streamlit.io/). There, you can create an account, hear about official announcements, 
    participate in asking and answering questions from other Stremalit app creators and interact with our team members!
        ''')

    with col2: 
        st.write('''
        Here is some useful information on the typical convention of importing Streamlit into any projects your making,
        along with commands that can be run in your terminal: 
        ''')
        st.markdown('__Import convention:__')

        st.code('>>> import streamlit as st')

        st.markdown('__Command line:__')
        st.code('''
$ streamlit --help 
# gives you a list of possible streamlit command line options,  
# commands and arguements

$ streamlit run your_script.py 
# use in the directory of the webapp your developing to run your app 
# locally

$ streamlit hello
# how to get here! 

$ streamlit demos
# launches a webapp that shows you 4 demos that you can try

$ streamlit config show
# what does this do 

$ streamlit cache clear
# what does this do 

$ streamlit docs
# opens a link to our documentation in your default web browser

$ streamlit --version
# returns the current version of Streamlit you have installed

$ pip install streamlit-nightly --upgrade
# what does this do 
        ''')    

        st.markdown('__How to uninstall:__')
        st.code('''
pip uninstall streamlit
        ''')
    return