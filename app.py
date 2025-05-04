import streamlit as st 
from ingestion import ingest_documents
from query_engine import answer_query

st.set_page_config(page_title="Local RAG with Ollama",layout = "centered")

st.title("Local RAG App using Langchain + Ollama")
st.markdown("Ingest website content and ask questions - no external APIs needed.")


st.header("Provide URL(s) to ingest")
url_input = st.text_area("Enter one or more URLs (one per Line):")


if st.button("Ingest Content"):
    urls = [u.strip() for u in url_input.splitlines()]
    if not urls:
        st.warning("Please enter at least one valid URL.")
    else:
        with st.spinner("Scrapping and embedding.."):
            ingest_documents(urls)
        st.success("Ingestion completed!")

st.header("Ask a question")
query = st.text_input("your question:")

if st.button("Get answer"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = answer_query(query)
        st.success("Answer:")
        st.write(answer)
        
        