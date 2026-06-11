# 🤖 AI Customer Support Assistant

**Designed and Developed by Sana Shams**

A Retrieval-Augmented Generation (RAG) based customer support assistant built using LangChain, FAISS, Sentence Transformers, and Streamlit.

The application enables users to ask customer support questions in natural language and retrieves the most relevant information from a knowledge base using semantic search.

---

## 🚀 Features

* Semantic search using vector embeddings
* FAISS vector database for efficient retrieval
* Document chunking using LangChain
* Interactive Streamlit web interface
* Knowledge-base driven responses
* Source attribution for retrieved answers
* Clean and responsive UI
* Ready for LLM integration (Llama 3 / OpenAI)

---

## 🛠️ Tech Stack

* Python
* LangChain
* FAISS
* Sentence Transformers
* Hugging Face Embeddings
* Streamlit

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
├── app.py
├── ingest.py
├── query.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

### Step 1: Knowledge Base Creation

Customer support FAQs are stored inside:

```text
docs/company_faq.txt
```

### Step 2: Document Processing

LangChain loads the document and splits it into smaller chunks.

### Step 3: Embedding Generation

Sentence Transformers converts text chunks into vector embeddings.

### Step 4: Vector Storage

FAISS stores the embeddings for efficient semantic search.

### Step 5: User Query

The user enters a question through the Streamlit interface.

### Step 6: Retrieval

Relevant document chunks are retrieved based on semantic similarity.

### Step 7: Response Generation

The application returns the most relevant answer and displays the supporting source documents.

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

### Launch the Streamlit App

```bash
streamlit run app.py
```

---

## 🔮 Future Enhancements

* Llama 3 integration using Ollama
* OpenAI API integration
* Conversational memory
* Chat-style interface
* PDF document ingestion
* Multi-document knowledge base
* Source citations with confidence scores

---

## 👨‍💻 Author

**Sana Shams**

Built as part of a hands-on Generative AI and Retrieval-Augmented Generation (RAG) learning project using LangChain, FAISS, and Streamlit.
