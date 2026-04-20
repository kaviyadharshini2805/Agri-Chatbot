# Agri Chatbot using Retrieval-Augmented Generation (RAG)

## Overview
The Agri Chatbot is an AI-powered application designed to answer agriculture-related queries using domain-specific knowledge. It leverages a Retrieval-Augmented Generation (RAG) architecture to provide accurate and context-aware responses by combining document retrieval with language model generation.

## Features
- Answers agriculture-related queries in natural language  
- Uses domain-specific knowledge base for improved accuracy  
- Reduces hallucination compared to standalone language models  
- Interactive user interface for seamless interaction  

## Tech Stack
- Python  
- Streamlit  
- LangChain  
- FAISS (Vector Database)  
- Large Language Model (LLM)  

## Architecture
The system follows a simple RAG pipeline:

User Query → Vector Search (FAISS) → Relevant Context → LLM → Generated Response

## Workflow
1. User inputs a query through the Streamlit interface  
2. The query is converted into embeddings  
3. FAISS retrieves the most relevant documents  
4. Retrieved context is passed to the LLM  
5. The LLM generates a response based on the context  

## Installation

### Clone the repository
```bash
git clone https://github.com/kaviyadharshini2805/Agri-Chatbot.git
```

### Navigate to the project directory
```bash
cd Agri-Chatbot
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the application
```bash
streamlit run app.py
```

## Project Structure
```
Agri-Chatbot/
│── app.py
│── agri_data.txt
│── requirements.txt
│── README.md
```

## Future Improvements
- Integration with real-time agricultural data sources  
- Multilingual support for regional farmers  
- Advanced RAG techniques such as reranking and query optimization  
- Deployment on cloud platforms  

## Conclusion
This project demonstrates the application of Retrieval-Augmented Generation in building domain-specific AI systems. It highlights how combining vector search with language models can significantly improve response accuracy and reliability.
