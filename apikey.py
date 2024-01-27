from dotenv import load_dotenv
import streamlit as st 
class GetKey:
    """
    ## GetKey
    api_key -> Your gemini api key 
    """
    def __init__(self):
        load_dotenv()
        self.api_key = st.secrets['API_KEY']
        self.pinecone_api_key = st.secrets['PINECONE_API_KEY']
        self.pinecone_env = st.secrets['PINECONE_ENV']