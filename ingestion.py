from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


def ingest_documents(urls: list[str]):
    documents = []
    for url in urls:
        try:
            loader = WebBaseLoader(url)
            docs = loader.load()
            documents.extend(docs)
        except Exception as e:
            print(f"failed to load {url}: {e}")
            
    
    splitter = RecursiveCharacterTextSplitter(chunk_size = 400, chunk_overlap = 50)
    chunks = splitter.split_documents(documents)
    
    
    embeddings = OllamaEmbeddings(model = "mxbai-embed-large:latest")
    db = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="./chroma_db")
    print("Documents embedded and stored in Chroma")
    
    
    