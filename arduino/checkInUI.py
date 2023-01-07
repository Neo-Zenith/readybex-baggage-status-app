import streamlit as st
from PIL import Image
import time
import baggagecheckin

im = Image.open("../client/public/favicon.ico")
st.set_page_config(page_title='ReadyBex Kiosk', page_icon = im)

title_string = 	"""
                <h1> Welcome to ReadyBex </h1>
                <p style="font-size:18px"> To begin, enter your name and passport number. </p>
                """
title = st.markdown(title_string, unsafe_allow_html=True)

placeholder = st.empty()
with placeholder.form(key='Kiosk Form', clear_on_submit=True):
    name = st.text_input("Name: ")
    passport_no = st.text_input("Passport Number: ")
    submit = st.form_submit_button("Submit")

placeholder2 = st.empty()
if submit:
    instruction = st.warning('Please scan the RFID tag to register.', icon="⚠️")
    animation = st.image("https://www.thermaltransfersolutions.com/wp-content/uploads/2019/06/RFID_as_gif.gif", width=150)
    if baggagecheckin.main(name, passport_no):
        instruction.empty()
        placeholder.empty()
        placeholder2.empty()
        animation.empty()
        title.empty()

        title_string = """
        <h1> Thank You!</p>"""
        title = st.markdown(title_string, unsafe_allow_html=True)

        html_string = """
        <img width="350px" src="https://user-images.githubusercontent.com/77436548/211039550-047d4928-2383-405a-9e07-7a59dcc3b6b4.png" />
        """
        st.success("Baggage has been registered! You may use the following QR code to check the status of your bag!", icon="✅")
        st.markdown(html_string, unsafe_allow_html=True)
        exitButton = st.button("Exit")

        if exitButton:
            exit()
    else:
        instruction.empty()
        animation.empty()
        placeholder = st.error('RFID tag has already been registered!', icon="🚨")