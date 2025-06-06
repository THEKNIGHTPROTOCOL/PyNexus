# 🤖 Conversational Retrieval with LangChain and OpenAI

This project implements a conversational AI assistant using **LangChain**, **OpenAI's GPT models**, and **Chroma** vector storage. It allows users to interact with their own documents using natural language queries.

---

## 🚀 Features

- Load documents from a local `data/` directory  
- Build and persist a **vector store index** for faster future queries  
- Maintain **chat history** for contextual conversations  
- **Command-line or interactive mode** support  
- Easy integration with `.env` for secure API key usage  

---

## 🧱 Requirements

- Python 3.7+
- Required packages:
  - `openai`
  - `langchain`
  - `chromadb`
  - `python-dotenv`

Install dependencies:

```bash
pip install openai langchain chromadb python-dotenv
