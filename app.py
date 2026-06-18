import streamlit as st
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 AI Customer Support Assistant")

st.caption(
    "Built with LangChain • FAISS • Llama 3 • Groq • Streamlit"
)

st.info(
    """
    This application uses Retrieval-Augmented Generation (RAG)
    to search a knowledge base and generate AI-powered responses.
    """
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

# --------------------------------------------------
# Load Vector Store
# --------------------------------------------------

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

# --------------------------------------------------
# Load Groq Llama 3
# --------------------------------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# --------------------------------------------------
# User Question
# --------------------------------------------------

question = st.text_input(
    "Have a query? Ask me!"
)

# --------------------------------------------------
# Search & Generate Answer
# --------------------------------------------------

if question:

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a helpful customer support assistant.

Answer ONLY using the provided context.

If the answer is not available in the context,
say:

'I could not find that information in the knowledge base.'

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    # --------------------------------------------------
    # Display Answer
    # --------------------------------------------------

    st.subheader("Answer")

    st.success(response.content)

    # --------------------------------------------------
    # Display Sources
    # --------------------------------------------------

    st.subheader(f"Sources ({len(docs)})")

    for i, doc in enumerate(docs, start=1):

        with st.expander(f"Source {i}"):

            st.write(doc.page_content)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption("🚀 Built by Sana Shams")