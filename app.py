
from dotenv import load_dotenv
import streamlit as st



load_dotenv()

st.set_page_config(page_title= "DBChat", page_icon=":speech_balloon:")

st.title("DBChat")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat app with SQL")
    
    st.text_input("host", value="localhost")
    st.text_input("Port", value="3306")
    st.text_input("User", value="root")
    st.text_input("Password", value="admin" type="password")
    st.text_input("Database", value="chinook")