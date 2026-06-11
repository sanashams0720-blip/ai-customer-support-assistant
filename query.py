from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

# Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

query = "Can I change my address?"

results = retriever.invoke(query)

print("\nRelevant Results:\n")

for i, doc in enumerate(results, 1):
    print(f"Result {i}")
    print("-" * 50)
    print(doc.page_content)
    print()
