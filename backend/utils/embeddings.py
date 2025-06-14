import os
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

# Load .env variables
load_dotenv()

# Pinecone config from .env
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_index_name = os.getenv("PINECONE_INDEX_NAME", "aiops-384")
pinecone_region = os.getenv("PINECONE_REGION", "us-west-2")
pinecone_cloud = os.getenv("PINECONE_CLOUD", "aws")

# ✅ Use smaller, faster model (384-dim output)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ✅ Pinecone dimension must match embedding size
PINECONE_DIMENSION = 384

# Init Pinecone client
pc = Pinecone(api_key=pinecone_api_key)

# Create index if it doesn't exist
if pinecone_index_name not in pc.list_indexes().names():
    pc.create_index(
        name=pinecone_index_name,
        dimension=PINECONE_DIMENSION,
        metric="cosine",
        spec=ServerlessSpec(cloud=pinecone_cloud, region=pinecone_region)
    )

# Connect to index
index = pc.Index(pinecone_index_name)

# Create vectorstore
vectorstore = PineconeVectorStore(
    index=index,
    embedding=embedding_model,
    text_key="text"
)

# Exported for RAG chain or chat use
def get_vectorstore():
    return vectorstore
