import os
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

# Load environment variables
load_dotenv()

# Config constants
PINECONE_DIMENSION = 384
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "aiops-384")
PINECONE_REGION = os.getenv("PINECONE_REGION", "us-west-2")
PINECONE_CLOUD = os.getenv("PINECONE_CLOUD", "gcp")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


def get_vectorstore():
    """
    Lazily initializes and returns a Pinecone-backed vectorstore
    using a locally stored Hugging Face embedding model.
    """
    # ✅ Load embedding model from local folder
    embedding_model = HuggingFaceEmbeddings(
    model_name="/app/models/all-MiniLM-L6-v2"  # This path will match what you copy in Docker
    )
    # Initialize Pinecone client and connect to index
    pc = Pinecone(api_key=PINECONE_API_KEY)

    if PINECONE_INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=PINECONE_DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(cloud=PINECONE_CLOUD, region=PINECONE_REGION),
        )

    index = pc.Index(PINECONE_INDEX_NAME)

    return PineconeVectorStore(
        index=index,
        embedding=embedding_model,
        text_key="text"
    )
