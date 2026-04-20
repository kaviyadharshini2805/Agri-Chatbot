import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load data
loader = TextLoader("agri_data.txt")
documents = loader.load()

# Split text
text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Use local embeddings (NO API)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create vector DB
db = FAISS.from_documents(docs, embeddings)

# Streamlit UI
st.title("🌾 Agri Chatbot (Offline RAG)")

query = st.text_input("Ask your question:")

if query:
    docs = db.similarity_search(query, k=2)
    
    # Simple response (no LLM)
    response = " ".join([doc.page_content for doc in docs])
    
    st.success(response)