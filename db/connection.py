# db/connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_engine(db_uri):
    """
    Create and return an SQLAlchemy engine.
    """
    engine = create_engine(db_uri)
    return engine

def get_session(engine):
    """
    Create and return an SQLAlchemy session.
    """
    Session = sessionmaker(bind=engine)
    return Session()

def execute_query(session, query):
    """
    Execute a given SQL query using the provided session and return the results.
    """
    try:
        result = session.execute(query)
        return result.fetchall()  # Or adjust based on the query type
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
