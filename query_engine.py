from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama, OllamaEmbeddings


def answer_query(query:str) -> str:
    db = Chroma(persist_directory="./chroma_db", embedding_function=OllamaEmbeddings(model = "mxbai-embed-large:latest"))
    retriever = db.as_retriever()
    
    prompt_template = """
    You are a helpful assistant. Use only the follwowing context to answer the question.
    if the answer is not contained in the context, say "I don't know".
    
    context:
    {context}
    
    Question: {question}
    Answer:
    """
    prompt = PromptTemplate(
        template = prompt_template,
        input_variables=["context", "question"]
        
    )
    
    llm = ChatOllama(model = "llama3.2:1b")
    
    qa = RetrievalQA.from_chain_type(llm = llm ,
                                     retriever = retriever,
                                     chain_type="stuff",
                                     chain_type_kwargs={"prompt":prompt}
                                     
                                     )
    return qa.invoke({"query": query})
