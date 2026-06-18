# 🤖 AI Customer Support Assistant

**Designed and Developed by Sana Shams**

## 📸 Application Preview

![AI Customer Support Assistant](screenshot.png)

A Retrieval-Augmented Generation (RAG) based customer support assistant built using LangChain, FAISS, Sentence Transformers, Groq, Llama 3, and Streamlit.

The application enables users to ask customer support questions in natural language, retrieves the most relevant information from a knowledge base using semantic search, and generates context-aware answers using Llama 3.

---

## 🚀 Features

* Retrieval-Augmented Generation (RAG)
* Semantic search using vector embeddings
* FAISS vector database for efficient retrieval
* Document chunking and indexing using LangChain
* AI-generated responses powered by Llama 3
* Groq-powered low-latency inference
* Interactive Streamlit web interface
* Source attribution for retrieved answers
* Context-aware question answering
* Clean and responsive UI

---

## 🏗️ Architecture

```text
User Question
      │
      ▼
Streamlit Interface
      │
      ▼
LangChain Retriever
      │
      ▼
FAISS Vector Store
      │
      ▼
Relevant Knowledge Chunks
      │
      ▼
Llama 3 (Groq)
      │
      ▼
AI Generated Response
      │
      ▼
Source Attribution
```

---

## 🛠️ Tech Stack

* Python
* LangChain
* FAISS
* Sentence Transformers
* Hugging Face Embeddings
* Groq API
* Llama 3
* Streamlit
* Python Dotenv

---

## 📚 Supported Topics

* Shipping
* Refunds
* Delivery
* International Shipping
* Address Changes
* Support Hours

---

## 📂 Project Structure

```text
ai-customer-support-assistant/
│
├── docs/
│   └── company_faq.txt
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
├── screenshot.png
├── .env
├── app.py
├── ingest.py
├── query.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

### 1. Knowledge Base Creation

Customer support FAQs are stored inside:

```text
docs/company_faq.txt
```

### 2. Document Processing

LangChain loads the FAQ document and splits it into manageable chunks.

### 3. Embedding Generation

Sentence Transformers converts each text chunk into vector embeddings.

### 4. Vector Storage

FAISS stores the embeddings for efficient semantic retrieval.

### 5. User Query

Users submit questions through the Streamlit interface.

### 6. Retrieval

The retriever finds the most relevant document chunks based on semantic similarity.

### 7. AI Response Generation

Retrieved context is sent to Llama 3 through the Groq API.

The model generates a contextual answer grounded in the retrieved documents while displaying the supporting source information.

---

## ▶️ Running the Application

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create the Vector Database

```bash
python ingest.py
```

### Add Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Launch the Application

```bash
streamlit run app.py
```

---

## 🔮 Future Enhancements

* Conversational memory
* Chat-style interface
* PDF document ingestion
* Multi-document knowledge base
* Cloud deployment
* Confidence scoring
* Conversation history
* User authentication

---

## 👨‍💻 Author

**Sana Shams**

Built as a hands-on Generative AI project demonstrating Retrieval-Augmented Generation (RAG), semantic search, vector databases, and LLM-powered question answering using LangChain, FAISS, Groq, Llama 3, and Streamlit.
