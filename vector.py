import chromadb.utils.embedding_functions as embedding_functions
from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma,Pinecone 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
import os 
import chromadb
from pinecone import Pinecone as Cone
from apikey import GetKey
embed_model  = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=GetKey().api_key)
def embeddings():
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=GetKey().api_key)

def add_document_tovector(fileName):
    loader =DirectoryLoader('./upload',glob="./*.pdf",loader_cls=PyPDFLoader)
    for file in loader.load():
        print(file.metadata)
        if file.metadata['source']==fileName:
            print(fileName)
            db = Chroma(persist_directory='./chromadb',embedding_function=embeddings)
            db.add_documents(
                docs=file
            )
            db.persist()
def vectordb()->Chroma:
    loader = DirectoryLoader('./upload',glob="./*.pdf",loader_cls=PyPDFLoader)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=500)
    docs = text_splitter.split_documents(documents)

    client = chromadb.Client()
    if client.list_collections():
        client.get_or_create_collection("source")
    
    db = Chroma.from_documents(docs,embed_model,persist_directory='./chromadb')
    db.persist()

    return db
def use_cone():
    
    loader = DirectoryLoader('./upload',glob="./*.pdf",loader_cls=PyPDFLoader)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=500)
    docs = text_splitter.split_documents(documents)
    
    cone= Cone(
     api_key= GetKey().pinecone_api_key,
     environment=GetKey().pinecone_env
    )
    index_name ="source"
    pineconedb = Pinecone.from_documents(docs, embed_model, index_name=index_name)
    return pineconedb
def cone_vector(filename):
    loader = DirectoryLoader('./upload',glob="./*.pdf",loader_cls=PyPDFLoader)
    # use only file name fetching
    documents = loader.load()
    for file in documents:
        if filename==file.metadata['source']:
            create_cone_embed(file)
            
def create_cone_embed(getFile):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=500)
    docs = text_splitter.split_documents(getFile)
    
    cone= Cone(
     api_key= GetKey().pinecone_api_key,
     environment=GetKey().pinecone_env
    )
    index_name ="source"
    if index_name in cone.list_indexes():
        index=cone.Index(index_name)
        db = Pinecone(index,embed_model,"text")
        for text in docs:
            db.add_text(text.page_content)