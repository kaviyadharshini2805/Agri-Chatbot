# Agri Chatbot
## Project Description

Agri Chatbot is an offline AI-powered agriculture assistance system developed using Streamlit, LangChain, FAISS, and Hugging Face embeddings. The project uses Retrieval-Augmented Generation (RAG) concepts to retrieve relevant agricultural information from a local text knowledge base and provide accurate responses to user queries.

The application processes agricultural documents by splitting them into smaller text chunks, converting them into vector embeddings, and storing them in a FAISS vector database for efficient semantic similarity search. When a user asks a question, the chatbot retrieves the most relevant content and displays context-based answers through an interactive Streamlit interface.

This project demonstrates the practical implementation of Natural Language Processing (NLP), vector databases, semantic search, and AI-driven information retrieval in the agriculture domain.
Live Demo: https://kaviyadharshini-agri-chatbot.streamlit.app/

---

## Features

- Offline document-based question answering
- Semantic search using FAISS vector database
- Hugging Face sentence transformer embeddings
- Streamlit web interface
- Agriculture-focused knowledge retrieval
- Lightweight and easy to run locally

---

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face Transformers
- Sentence Transformers

---

## Project Structure

```text
Agri-Chatbot/
│
├── app.py
├── agri_data.txt
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kaviyadharshini2805/Agri-Chatbot.git
```

Navigate to the project folder:

```bash
cd Agri-Chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## How It Works

1. Agricultural text data is loaded from `agri_data.txt`
2. Text is split into smaller chunks
3. Embeddings are generated using Hugging Face models
4. FAISS stores vector embeddings for similarity search
5. User queries are matched with relevant document chunks
6. Retrieved responses are displayed through Streamlit

---

## Future Improvements

- Integration with large language models
- Multilingual support
- Voice-based interaction
- Real-time agricultural datasets
- Cloud deployment

---

## Author

Kaviyadharshini M

---
