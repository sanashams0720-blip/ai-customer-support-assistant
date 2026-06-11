from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load document
loader = TextLoader("docs/company_faq.txt")
documents = loader.load()

# Split document
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating vector database...")

# Create FAISS vector store
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

# Save locally
vectorstore.save_local("vectorstore")

print("Vector database created successfully!")
