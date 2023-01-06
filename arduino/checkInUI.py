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

if submit:
    html_string = """
    <p1> Please scan the RFID tag to register. </p>
    """
    instruction = st.markdown(html_string, unsafe_allow_html=True)
    if baggagecheckin.main(name, passport_no):
        instruction.empty()
        placeholder.empty()
        title.empty()

        title_string = """
        <h1> Thank You!</p>"""
        title = st.markdown(title_string, unsafe_allow_html=True)

        html_string = """
        <p style="font-size:18px;"> Baggage has been registered! You may use the following QR code to check the status of your bag! </p>
        <img width="350px" src="https://user-images.githubusercontent.com/77436548/211017791-556300da-f4d2-4801-b824-baa482e455d3.png" />
        """
        st.markdown(html_string, unsafe_allow_html=True)
        exitButton = st.button("Exit")

        if exitButton:
            exit()