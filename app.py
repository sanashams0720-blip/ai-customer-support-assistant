import streamlit as st
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 AI Customer Support Assistant")

st.caption(
    "Built with LangChain • FAISS • Llama 3 • Groq • Streamlit"
)

st.info(
    "This application uses Retrieval-Augmented Generation (RAG) "
    "to search a knowledge base and generate AI-powered responses."
)

st.markdown("""
### Supported Topics

- Shipping
- Refunds
- Delivery
- International Shipping
- Address Changes
- Support Hours
""")

# Load Vector Store
@st.cache_resource
def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


vectorstore = load_vectorstore()

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

# Load Groq Llama Model
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input(
    "Ask a customer support question..."
)

# Process question
if question:

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Conversation history
    history = ""

    for msg in st.session_state.messages[-6:]:
        history += f"{msg['role']}: {msg['content']}\n"

    # Prompt
    prompt = f"""
You are a helpful customer support assistant.

Use both the conversation history and the knowledge base context.

Rules:
1. Answer only using the context provided.
2. Consider previous messages for follow-up questions.
3. If the answer is not available, say:
   "I could not find that information in the knowledge base."

Conversation History:
{history}

Knowledge Base Context:
{context}

Current Question:
{question}

Answer:
"""

    # Generate response
    response = llm.invoke(prompt)

    answer = response.content

    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Sources
    with st.expander("📚 View Sources"):

        for i, doc in enumerate(docs, start=1):

            st.markdown(f"**Source {i}**")
            st.write(doc.page_content)
            st.divider()

# Footer
st.divider()

st.caption("🚀 Built by Sana Shams")