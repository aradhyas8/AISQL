import streamlit as st
from db.connection import get_engine, get_session, execute_query
from langchain.agent import LangChainAgent

# Assuming the Streamlit UI and other setup code is here

# Example usage of DB connection (adjust according to your actual use case)
engine = get_engine("sqlite:///data/Chinook.db")
session = get_session(engine)

# Example usage of LangChainAgent
# Note: Ensure you pass the correct database URI to LangChainAgent
langchain_agent = LangChainAgent("sqlite:///data/Chinook.db")
response = langchain_agent.query("List the total sales per country.")

# Display the response in your Streamlit application
st.write(response)
# Assuming the Streamlit UI and other setup code is here
# Path: db/connection.py
# Note: This file is used to establish a connection to the database#
#Connection to the database