import streamlit as st
import baggagecheckin

html_string = 	"""
                <h1> Welcome to ReadyBex </h1>
                """
st.markdown(html_string, unsafe_allow_html=True)
name = st.text_input("Name: ")
passport_no = st.text_input("Passport Number: ")
submit = st.button("Submit")

if submit:
    html_string = """
    <p1> Please scan the RFID tag to register. </p>
    """
    st.markdown(html_string, unsafe_allow_html=True)
    if baggagecheckin.main(name, passport_no):
        html_string = """
        <p1> Baggage has been registered! You may use the following QR code to check the status of your bag! </p>
        <img src="https://user-images.githubusercontent.com/77436548/210952368-686d03b8-aa95-450a-a8b2-91b06540d2c2.png" />
        """
        st.markdown(html_string, unsafe_allow_html=True)