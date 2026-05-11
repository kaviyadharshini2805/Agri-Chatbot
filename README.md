# Agri Chatbot

An offline Retrieval-Augmented Generation (RAG) based agriculture chatbot built using Streamlit, LangChain, FAISS, and Hugging Face embeddings.

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

## License

This project is for educational and learning purposes.
