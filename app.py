
import urllib.parse
from dotenv import load_dotenv
import streamlit as st
from langchain_community.utilities import SQLDatabase

def init_database(user, password, host, port, database):
    password = urllib.parse.quote(password)
    db_uri = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)

load_dotenv()

st.set_page_config(page_title="DBChat", page_icon=":speech_balloon:")

st.title("DBChat")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat app with SQL")
    
    st.text_input("host", value="aws-0-ca-central-1.pooler.supabase.com", key="host")
    st.text_input("Port", value="5432", key="port")
    st.text_input("User", value="postgres.yphplsewskzrkbhrmgay", key="user")
    st.text_input("Password", value="Ethanyork@1234", type="password", key="password")
    st.text_input("Database", value="postgres", key="database")
    
    if st.button("Connect"):
        with st.spinner("Connecting to the database"):
            db = init_database(
                st.session_state["user"],
                st.session_state["password"],
                st.session_state["host"],
                st.session_state["port"],
                st.session_state["database"]
            )
            
            st.session_state.db = db
            st.success("Connected to the database")
    
st.chat_input("Type a message")
