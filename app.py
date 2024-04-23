
from dotenv import load_dotenv
import streamlit as st
from langchain_community.utilities import SQLDatabase

def init_databse(
    user,
    password,
    host,
    port,
    database
):
    db_uri = f"mysql://{user}:{password}@{host}:{port}/{database}"
    
    return SQLDatabase.from_uri(db_uri)

load_dotenv()

st.set_page_config(page_title= "DBChat", page_icon=":speech_balloon:")

st.title("DBChat")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat app with SQL")
    
    st.text_input("host", value="localhost")
    st.text_input("Port", value="3306")
    st.text_input("User", value="root")
    st.text_input("Password", value="admin", type="password")
    st.text_input("Database", value="chinook")
    
    st.button("Connect")
    
st.chat_input("Type a message")