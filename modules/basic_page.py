import streamlit as st 
import pandas as pd
import numpy as np

def empty_line(num):
    for x in range(1,num+1):
        st.write('')
    return

def basic(page):
    '''Basic streamlit commands'''
    st.title(page)
    st.write(''' This page will run you through all the basic Streamlit functions. It will show you the name of 
    the function, what that function looks like rendered on a Streamlit app, the code to generate the function, 
    and, if it's something that the user can interact with- like a widget, will allow you to interact with the function
    so you will be able to directly see how to _use_ that feature to change your app based on user interaction.
    :smile:''')
    
    # start with the basics

    # WIDGETS
    st.header('Interactive Widgets')
    st.write('''Lets start with all the possible widgets that you can put in your app! There are many interactive 
    widgets that you can use to allow the user to interact with your app.''')
    st.markdown("---")

    # create columns to put all the functions in mid column buffer
    # for widgets section
    col1, mid, col2 = st.beta_columns([20,0.5,20])

    # __________Column 1 in Widgets__________
    with col1: 
        st.subheader('Button')
        a_button = st.button('Hit me', key='button_run')

        st.code('''
button = st.button('Hit me')
if button: # if it has been clicked
    st.write('TADA!')''')
        if a_button: # if it has been clicked
            st.write('TADA!')
    
        st.markdown("---")
        st.subheader('Checkbox')
        a_checkbox = st.checkbox('Check me out', key='check_run')
        st.code(''' 
checkbox = st.checkbox('Check me out') 
if checkbox: # if clicked
    st.write("I'm awesome!")''')

        if a_checkbox: # if clicked    
            st.write("I'm awesome!")

        st.markdown("---")  
        st.subheader('Radio Buttons')
        st.write('The options for a radio button can be a string, integer, float, or variable')
        variable = 12
        radio_selection = st.radio('Radio', ['Option 1',variable,3.14159], key='radio_run')
        st.code(''' 
variable = 12
radio_select = st.radio('Radio', ['Option 1',variable,3.14159]) 
if radio_select == 'Option 1': 
    st.write("great choice")
elif radio_select == variable:
    st.write("thats a number from a variable")
elif radio_select == 3.14159:
    st.write(np.pi)''')
        if radio_selection == 'Option 1': 
            st.write("great choice")
        elif radio_selection == variable:
            st.write("thats a number from a variable")
        elif radio_selection == 3.14159:
            st.write(np.pi)
        
        st.markdown("---")
        st.subheader('Sliders')
        st.markdown('__Single Slider__')
        slider_value = st.slider('Slide me', min_value=0, max_value=10, value=5, key='slider_run')
    
        st.code('''
variable = 12
slider_pick = st.slider('Slide me',  min_value=0, max_value=10, value=5)
st.write(slider_pick)''')
        st.write(slider_value)

        st.markdown("---")
        st.markdown('__Double Ended Slider__')
        double_slider = st.slider('A range', 0,100, (10,90), key='dslider_run')
        st.code('''
dble_slider = st.slider('A range', 0,100, (10,90))
st.write(dble_slider)''')
        st.write(double_slider)

        st.markdown("---")
        st.markdown('__Fixed Option Slider__')
        s_slider = st.select_slider('Slide to select', options=[1,'Middle', variable], value = 'Middle', key='sslider_run')
        st.code('''
fixed_slider = st.select_slider('Slide to select', 
    options=[1,'Middle', variable],value = 'Middle')
st.write(fixed_slider)''')
        st.write(s_slider)

        st.markdown("---")
        st.subheader('Odds & Ends')
        st.markdown("__Upload a file__")
        st.code(''' 
upload_file = st.file_uploader('File uploader')
        ''')
        upload_file = st.file_uploader('File uploader',key='file_run')

        st.markdown("---")
        st.markdown("__Colour Select__")
        st.code(''' 
colour = st.color_picker('Pick a color')
st.write(colour)''')
        color = st.color_picker('Pick a color',key='color_run')
        st.write(color)

    # __________Column 2 in Widgets__________
    with col2: 
        st.subheader('Selectbox')
        st.write('Select 1 option from a variety')
        single_select = st.selectbox('Single Select', ['what', 'will', 'you', 'choose?'], key='select_run')

        st.code(''' 
single_select_box = st.selectbox('Single Select', 
    ['what', 'will', 'you', 'choose?'])
    
if (single_select_box == 'what') or (single_select_box == 'you'): 
    st.write('You win! :smiley:')
else: 
    st.write('Winner Winner :chicken: Dinner!)''')
        if (single_select == 'what') or (single_select == 'you'): 
            st.write('You win! :smiley:')
        else: 
            st.write('Winner Winner :chicken: Dinner!')

        st.markdown("---")
        st.subheader('Multi-Select Box')
        st.write('Select 1 or more options from a variety')
        multi_select = st.multiselect('Multi-Select', ['what', 'will', 'you', 'choose?'],key='multi_run')
        st.code('''
multi_select_box = st.multiselect('Multi-Select', 
    ['what', 'will', 'you', 'choose?'])
st.write(multi_select_box)''')
        st.write(multi_select)

        st.markdown("---")
        st.subheader('Various Input fields')
        st.markdown('__Text Input__')
        st.code('''
title_limited = "Enter some text: limit to number of characters"
text_input_limited = st.text_input(title_limited, 'display text')
st.write(text_input_limited)
        
title_unlim = "Area for textual entry: no limit to number of characters"
text_area_unlim = st.text_area(title_unlim, "Text to Display")
st.write(text_area_unlim) ''')

        title_limited = "Enter some text: limit to number of characters"
        text_limited = st.text_input(title_limited, 'display text', key='text_run')
        st.write(text_limited)

        title_unlim = "Area for textual entry: no limit to number of characters"
        text_unlim = st.text_area(title_unlim, "Text to Display", key='tarea_run')
        st.write(text_unlim)

        st.markdown("---")
        st.markdown('__Number Input__')
        st.code(''' 
number = st.number_input('Enter a number')
st.write(number)''')
        a_number = st.number_input('Enter a number', key='number_run')
        st.write(a_number)

        st.markdown("---")
        st.markdown('__Date Input__')
        st.write("The date input is automatically the datetime class, default is the current date")
        st.code('''
date = st.date_input('Date input')
st.write(date)
st.write(type(date)) ''')
        a_date = st.date_input('Date input', key='date_run')
        st.write(a_date)
        st.write(type(a_date))

        st.markdown("---")
        st.markdown('__Time Input__')
        st.write("The time input is automatically the datetime class, default is the current time")
        st.code('''
time = st.time_input('Time entry')
st.write(time)
st.write(type(time))''')
        a_time = st.time_input('Time entry',key='time_run')
        st.write(a_time)
        st.write(type(a_time))

# ****************** END OF WIDGETS ******************

    # CREATING TEXT
    st.markdown("---")
    st.header('Display text')
    st.write('There are various ways to display text in Streamlit')
    st.markdown("---")

    text1, mid, text2 = st.beta_columns([20,1,20])

    # __________Column 1 in Text__________
    with text1: 
       
        st.title('A title')
        st.code("st.title('A title')")
        st.markdown("---")

        st.header('A basic header')
        st.code("st.header('A basic header')")

        st.markdown("---")
        st.subheader('My subheader')
        st.code("st.subheader('My subheader')")

        st.markdown("---")
        st.markdown('_Markdown_, __Markdown__:')
        st.code("st.markdown('_Markdown_, __Markdown__')")
  
     # __________Column 2 in Text__________
    with text2: 
        empty_line(2)
        st.write('The write command, also works when passing most objects:')
        an_object = ['list', 3.14159,0]
        st.code('''
an_object = ['list', 3.14159,0]
st.write('The write command, also works when passing most objects:')
st.write(an_object) #this is a list
         ''')
        st.write(an_object)
        st.markdown("---")
        
        st.write('LaTeX equations:')
        st.code("st.latex('e^{i\pi} + 1 = 0')")
        st.latex('e^{i\pi} + 1 = 0')
        st.markdown("---")

        st.text('Fixed width text command:')
        st.code("st.text('Fixed width text command:')")     
    
# ****************** END OF TEXT ******************

    # DISPLAY OTHER INFORMATION
    st.markdown("---")
    st.header('Display Other Information')
    st.write('You can display other information, such as code and data, with specific function calls')
    st.markdown("---")

    other1, mid, other2 = st.beta_columns([20,1,20])
    with other1: 
        st.subheader("Display Code")
        st.write('You can display code using __st.code__:')
        st.code(''' 
st.code('st.write("a line of code")')
st.code( ' ' '  # use triple quotes to create a block (no spaces)
st.write("A block of code")
code_button = st.button('Click Me')
if code_button: 
    success!
' ' ')
        ''')
        st.write('this output looks like:')
        st.code('st.write("a line of code")')
        st.code( '''  # use triple quotes to create a block (no spaces)
        st.write("A block of code")
        code_button = st.button('Click Me')
        if code_button: 
            st.text('success!')
        ''')

        st.write('''Another way is with __st.echo__, this is unique because anything after the echo function
        will first be displayed in a code box, then executed directly below. It will save extra lines if 
        your looking to show someone how you coded your app and then have it run automatically without 
        having to retype everything''')
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
    with other2: 
        st.subheader("Display Data")
        st.write("__Pandas DataFrame__")
        st.code(''' 
column_names = ['a','b','c','d','e']
pandas_data = pd.DataFrame(np.random.randn(50,5), columns=column_names)
st.dataframe(pandas_data)
        ''')
        column_names = ['a','b','c','d','e']
        pandas_data = pd.DataFrame(np.random.randn(50,5), columns=column_names)
        st.dataframe(pandas_data)
    
        st.write("you can also use the __st.table__ function:")
        st.code(''' 
column_names = ['a','b','c','d','e']
pandas_data = pd.DataFrame(np.random.randn(50,5), columns=column_names)
st.table(pandas_data.iloc[0:5])
        ''')
        st.table(pandas_data.iloc[0:5])

        st.write('__Json data__')
        st.code(''' 
json_data = {'Dictionary':True ,'Format':342}
st.json(json_data)''')
        json_data = {'Dictionary':True ,'Format':342}
        st.json(json_data)

# ****************** END OF OTHER ******************

    # MEDIA
    st.markdown("---")
    st.header("Media")
    st.write('''Media has its own unique finctions calls to create images, audio files and embedded videos. 
    Hyperlinks simply uses a markdown command, but is included here as an example.''')
    st.markdown("---")

    media1, mid, media2 = st.beta_columns([20,1,20])
    with media1: 
    
        st.subheader("Image")
        st.code('''
st.image('img/MC.png',use_column_width = True)
        ''')
        st.image('img/MC.png',use_column_width = True)

        st.markdown("---")
        st.subheader("Audio file")
        st.code(''' 
st.audio('img/audio_example.wav')
        ''')
        st.audio('img/audio_example.wav')

    with media2:
        st.subheader("Video")
        st.code(''' 
st.video('img/balloon_video.webm')
        ''')
        st.video('img/balloon_video.webm')

        st.markdown("---")
        st.subheader("Hyperlink")
        st.write("You can add hyperlinks in by using standard markdown notation")
        st.code('''
st.write('[Check this out](https://www.streamlit.io/sharing)')
st.markdown("[Tweet us!](https://twitter.com/streamlit)") ''')

        st.write('[Check this out](https://www.streamlit.io/sharing)')
        st.markdown("[Tweet us!](https://twitter.com/streamlit)")

    st.markdown("---")
 # ****************** END OF MEDIA ******************       

    # PLOT COMMANDS -> maybe they have their own section

    return
