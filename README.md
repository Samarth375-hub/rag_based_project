# 🧠 Local RAG App using LangChain + Ollama

A Retrieval-Augmented Generation (RAG) application that scrapes content from URLs, embeds and stores it locally using Chroma, and answers questions based **only** on the retrieved content using a local LLM from Ollama.

---

## 🚀 Features

- 🔗 Scrape multiple URLs
- 📄 Split documents into chunks
- 🧠 Generate embeddings with `mxbai-embed-large`
- 🗂 Store vectors using Chroma (local DB)
- 🤖 Query using local LLMs like `llama3.2:1b`
- 🔒 No external API calls
- 🧭 Only answers from retrieved context

---

## 🧰 Tech Stack

- **LangChain**
- **ChromaDB**
- **Ollama**
- **Streamlit**

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

**### 2. create a virtual environment**
 python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

**### 3. Install Dependencies**
pip install -r requirements.txt

**### 4. Install and run Ollama**
Downlaod and install Ollama
Run your model

**### 5. Run the App**
stremalit run app.py


