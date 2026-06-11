import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

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

st.title("AI Customer Support Assistant")

st.caption(
    "Built with LangChain • FAISS • Sentence Transformers • Streamlit"
)

st.info(
    """
    This application uses Retrieval-Augmented Generation (RAG) principles
    to search a knowledge base and return relevant customer support information.
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
# User Question
# --------------------------------------------------

question = st.text_input(
    "Have a query? Ask me!"
)


# --------------------------------------------------
# Search & Answer
# --------------------------------------------------

if question:

    results = retriever.invoke(question)

    top_result = results[0].page_content.lower()

    # Simple answer generation
    if "delivery address" in top_result:
        answer = (
            "Yes, you can change your delivery address "
            "before the order is shipped."
        )

    elif "refund" in top_result:
        answer = (
            "Customers can request a refund "
            "within 30 days of purchase."
        )

    elif "shipping takes" in top_result:
        answer = (
            "Standard shipping typically takes "
            "5–7 business days."
        )

    elif "international shipping" in top_result:
        answer = (
            "Yes, we offer international shipping "
            "to over 50 countries worldwide."
        )

    elif "support hours" in top_result:
        answer = (
            "Our support team is available Monday "
            "through Friday from 9 AM to 6 PM IST."
        )

    else:
        answer = (
            "I found relevant information in the knowledge base. "
            "Please review the sources below."
        )

    # --------------------------------------------------
    # Display Answer
    # --------------------------------------------------

    st.subheader("Answer")

    st.success(answer)

    # --------------------------------------------------
    # Sources
    # --------------------------------------------------

    st.subheader(f"Sources ({len(results)})")

    for i, doc in enumerate(results, start=1):

        with st.expander(f"Source {i}"):

            st.write(doc.page_content)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Built by Sana Shams"
)