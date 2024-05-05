# langchain/agent.py
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

class LangChainAgent:
    def __init__(self, db_uri):
        self.db = SQLDatabase.from_uri(db_uri)
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.agent_executor = create_sql_agent(self.llm, db=self.db, agent_type="openai-tools", verbose=True)

    def query(self, input_text):
        """
        Process a natural language query, execute it, and return the response.
        """
        try:
            response = self.agent_executor.invoke(input_text)
            return response
        except Exception as e:
            print(f"Error processing query with LangChain Agent: {e}")
            return None
