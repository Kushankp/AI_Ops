import os
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

# Load environment variables
load_dotenv()

# Config from .env
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_index_name = os.getenv("PINECONE_INDEX_NAME", "aiops")
pinecone_region = os.getenv("PINECONE_REGION", "us-west-2")
pinecone_cloud = os.getenv("PINECONE_CLOUD", "aws")

# Use e5-large (1024-dim output)
embedding_model = HuggingFaceEmbeddings(model_name="intfloat/e5-large")

# Init Pinecone client
pc = Pinecone(api_key=pinecone_api_key)

# Create index if not exists
if pinecone_index_name not in pc.list_indexes().names():
    pc.create_index(
        name=pinecone_index_name,
        dimension=1024,
        metric="cosine",
        spec=ServerlessSpec(cloud=pinecone_cloud, region=pinecone_region)
    )

# Connect to the index
index = pc.Index(pinecone_index_name)

# Create vectorstore
vectorstore = PineconeVectorStore(
    index=index,
    embedding=embedding_model,
    text_key="text"
)

# ✅ Make vectorstore available to import
def get_vectorstore():
    return vectorstore
