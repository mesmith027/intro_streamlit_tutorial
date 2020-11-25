import streamlit as st 
import pandas as pd
import numpy as np

def basic(page):
    '''Basic streamlit commands'''
    st.title(page)

    col1, col2 = st.beta_columns(2)
    # start with the basics

    # WIDGETS
    col2.header('Interactive Widgets')
    col2.write('There are many interactive widgets that you can use to allow the user \
        to interact with your app')

    col2.subheader('Button')
    a_button = col2.button('Hit me')

    col2.code('''
a_button = st.button('Hit me')
if a_button: # if it has been clicked
    st.write('TADA!')''')
    if a_button: # if it has been clicked
        col2.write('TADA!')

    col2.subheader('Checkbox')
    a_checkbox = col2.checkbox('Check me out')
    col2.code(''' 
a_checkbox = st.checkbox('Check me out') 
if a_checkbox: # if clicked
    st.write("Check me out I'm awesome!")''')

    if a_checkbox: # if clicked    
        col2.write("Check me out I'm awesome!")

    col2.subheader('Radio Buttons')
    col2.write('The options for a radio button can be a string, integer, float, or variable')
    variable = 12
    radio_selection = col2.radio('Radio', ['Option 1',variable,3.14159])
    col2.code(''' 
variable = 12
radio_selection = col2.radio('Radio', ['Option 1',variable,3.14159]) 
if radio_selection == 'Option 1': 
    st.write("great choice")
elif radio_selection == variable:
    st.write("thats a number from a variable")
elif radio_selection == 3.14159:
    st.write(np.pi)''')
    if radio_selection == 'Option 1': 
        col2.write("great choice")
    elif radio_selection == variable:
        col2.write("thats a number from a variable")
    elif radio_selection == 3.14159:
        col2.write(np.pi)

    col2.subheader('Selectbox')
    col2.write('Select 1 option from a variety')
    single_select = col2.selectbox('Single Select', ['what', 'will', 'you', 'choose?'])

    col2.code(''' 
single_select = st.selectbox('Single Select', 
    ['what', 'will', 'you', 'choose?'])
    
if (single_select == 'what') or (single_select == 'you'): 
    st.write('You win! :smiley:')
else: 
    st.write('Winner Winner :chicken: Dinner!)''')
    if (single_select == 'what') or (single_select == 'you'): 
        col2.write('You win! :smiley:')
    else: 
        col2.write('Winner Winner :chicken: Dinner!')

    col2.subheader('Multi-Select Box')
    col2.write('Select 1 or more options from a variety')
    multi_select = col2.multiselect('Multi-Select', ['what', 'will', 'you', 'choose?'])
    col2.code('''
multi_select = st.multiselect('Multi-Select', 
    ['what', 'will', 'you', 'choose?'])
st.write(multi_select)''')
    col2.write(multi_select)

    col2.subheader('Sliders')
    col2.markdown('__Single Slider__')
    slider_value = col2.slider('Slide me', min_value=0, max_value=10, value=5)
    
    col2.code('''
slider_value = st.slider('Slide me',  min_value=0, max_value=10, value=5)
st.write(slider_value)''')
    col2.write(slider_value)

    col2.markdown('__Double Ended Slider__')
    double_slider = col2.slider('A range', 0,100, (10,90))
    col2.code('''
double_slider = col2.slider('A range', 0,100, (10,90))
st.write(double_slider)''')
    col2.write(double_slider)

    col2.markdown('__Fixed Option Slider__')
    s_slider = col2.select_slider('Slide to select', options=[1,'Middle', variable], value = 'Middle')
    col2.code('''
s_slider = st.select_slider('Slide to select', 
    options=[1,'Middle', variable],value = 'Middle')
st.write(s_slider)''')
    col2.write(s_slider)

    with col2: 
        st.subheader('Various Input fields')
        st.markdown('__Text Input__')
        st.code('''
title_limited = "Enter some text: limit to number of characters"
text_limited = col2.text_input(title_limited, 'display text')
st.write(text_limited)
        
title_unlim = "Area for textual entry: no limit to number of characters"
text_unlim = col2.text_area(title_unlim, "Text to Display")
st.write(text_unlim) ''')

        title_limited = "Enter some text: limit to number of characters"
        text_limited = col2.text_input(title_limited, 'display text')
        st.write(text_limited)

        title_unlim = "Area for textual entry: no limit to number of characters"
        text_unlim = col2.text_area(title_unlim, "Text to Display")
        st.write(text_unlim)
    
        st.markdown('__Number Input__')
        st.code(''' 
a_number = st.number_input('Enter a number')
st.write(a_number)''')
        a_number = st.number_input('Enter a number')
        st.write(a_number)

        st.markdown('__Date Input__')
        st.write("The date input is automatically the datetime class, default is the current date")
        st.code('''
a_date = st.date_input('Date input')
st.write(a_date)
st.write(type(a_date)) ''')
        a_date = st.date_input('Date input')
        st.write(a_date)
        st.write(type(a_date))

        st.markdown('__Time Input__')
        st.write("The time input is automatically the datetime class, default is the current time")
        st.code('''
a_time = st.time_input('Time entry')
st.write(a_time)
st.write(type(a_time))''')
        a_time = st.time_input('Time entry')
        st.write(a_time)
        st.write(type(a_time))

        st.subheader('Odds & Ends')
        st.markdown("__Upload a file__")
        st.code(''' 
upload_file = st.file_uploader('File uploader')
        ''')
        upload_file = st.file_uploader('File uploader')

        st.markdown("__Colour Select__")
        st.code(''' 
color = st.color_picker('Pick a color')
st.write(color)''')
        color = st.color_picker('Pick a color')
        st.write(color)

    # CREATING TEXT
    with col1: 
        st.header('Display text')
        st.write('There are various ways to display text in Streamlit')
    
        st.markdown("---")
        st.title('A title')
        st.code("st.title('A title')")
        st.markdown("---")
        st.header('A basic header')
        st.code("st.header('A basic header')")

        st.subheader('My subheader')
        st.code("st.subheader('My subheader')")

        st.text('Fixed width text command:')
        st.code("st.text('Fixed width text command:')")

        st.write('The write command, also works when passing most objects:')
        an_object = ['list', 3.14159,0]
        st.code('''
st.write('The write command, also works when passing most objects:')
st.write(an_object) #this is a list
         ''')
        st.write(an_object)

        st.markdown('_Markdown_, __Markdown__:')
        st.code("st.markdown('_Markdown_, __Markdown__')")

        st.write('LaTeX equations:')
        st.code("st.latex('e^{i\pi} + 1 = 0')")
        st.latex('e^{i\pi} + 1 = 0')

    # DISPLAY CODE
    with col1: 
        st.header("Display Code")
        st.text('You can display code using st.code:')
        st.code(''' 
st.code('st.write("a line of code")')
st.code( ' ' '  # use triple quotes to create a block (no spaces)
st.write("A block of code")
code_button = st.button('Click Me')
if code_button: 
    success!
' ' ')
        ''')
        st.text('this output looks like:')
        st.code('st.write("a line of code")')
        st.code( '''  # use triple quotes to create a block (no spaces)
        st.write("A block of code")
        code_button = st.button('Click Me')
        if code_button: 
            st.text('success!')
        ''')

        st.write("Another way is with echo:")
        st.code(''' 
with st.echo(): # everything after this line will be printed
    st.text("Code to be executed and printed")
    echo = st.button("a button")
            if echo:
                st.write('__Here you go__')
        ''')
        st.write("Here it is in practice:")
        with st.echo(): # everything after this line will be printed
            st.text("Code to be executed and printed")
            echo = st.button("a button")
            if echo:
                st.write('__Here you go__')
            
    # DISPLAY DATA
    with col1: 
        st.header("Display Data")
        st.subheader("Pandas DataFrame")
        st.code(''' 
column_names = ['a','b','c','d','e']
pandas_data = pd.DataFrame(np.random.randn(50,5), columns=column_names)
st.dataframe(pandas_data)
        ''')
        column_names = ['a','b','c','d','e']
        pandas_data = pd.DataFrame(np.random.randn(50,5), columns=column_names)
        st.dataframe(pandas_data)
    
        st.write("you can also use the table function:")
        st.code(''' 
st.table(pandas_data.iloc[0:10])
        ''')
        st.table(pandas_data.iloc[0:10])

        st.subheader('Json data')
        st.code(''' 
json_data = {'Dictionary':True ,'Format':342}
st.json(json_data)''')
        json_data = {'Dictionary':True ,'Format':342}
        st.json(json_data)

    # MEDIA
    with col1: 
        st.header("Media")

        st.subheader("Image")
        st.code('''
st.image('img/MC.png',use_column_width = True)
        ''')
        st.image('img/MC.png',use_column_width = True)

        st.subheader("audio file")
        st.code(''' 
st.audio('img/audio_example.wav')
        ''')
        st.audio('img/audio_example.wav')

        st.subheader("Video")
        st.code(''' 
st.video('img/balloon_video.webm')
        ''')
        st.video('img/balloon_video.webm')

        st.subheader("Hyperlink")
        st.write("You can add hyperlinks in by using standard markdown notation")
        st.code('''
st.write('[Check this out](https://www.streamlit.io/sharing)')
st.markdown("[Tweet us!](https://twitter.com/streamlit)") ''')

        st.write('[Check this out](https://www.streamlit.io/sharing)')
        st.markdown("[Tweet us!](https://twitter.com/streamlit)")
        
    
    # SIDEBAR COMMANDS
    with col2: 
        st.header('Sidebar')
        st.write('''
To add widgets or functions to the sidebar you simply have to add 'sidebar' before you call the function. 
NOTE: the write function is not callable from the sidebar, you mucst use markdown''')
        st.code('''
# use st.sidebar.<widget> notation
a = st.sidebar.button("Your button added to the sidebar!")
if not a:
    st.sidebar.markdown('You added a widget to the sidebar!')

    ''')
        add_sidebar = st.button('Run this code to add to the sidebar')
        if add_sidebar: 
            a = st.sidebar.button("Your button added to the sidebar!")
            if not a:
                st.sidebar.markdown('You added a widget to the sidebar!')
            
    

    # PLOT COMMANDS -> maybe they have their own section

    return
