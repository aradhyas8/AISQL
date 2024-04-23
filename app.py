import os
import urllib.parse
from dotenv import load_dotenv
import streamlit as st
from langchain_community.utilities import SQLDatabase

load_dotenv()  # This loads the environment variables from the .env file.

def init_database():
    user = os.getenv("DB_USER")
    password = urllib.parse.quote(os.getenv("DB_PASSWORD"))  # URL-encode the password
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_DATABASE")
    db_uri = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)

st.set_page_config(page_title="DBChat", page_icon=":speech_balloon:")
st.title("DBChat")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat app with SQL")

    if st.button("Connect"):
        with st.spinner("Connecting to the database"):
            db = init_database()
            st.session_state.db = db
            st.success("Connected to the database")

st.chat_input("Type a message")
