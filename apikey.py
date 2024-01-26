from dotenv import load_dotenv
import os
class GetKey:
    """
    ## GetKey
    api_key -> Your gemini api key 
    """
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')
        self.pinecone_api_key = os.getenv('PINECONE_API_KEY')
        self.pinecone_env = os.getenv('PINECONE_ENV')