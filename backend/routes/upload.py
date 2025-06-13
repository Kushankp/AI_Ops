from fastapi import APIRouter, UploadFile
from langchain_community.document_loaders import PyPDFLoader
from utils.embeddings import vectorstore
import os
import tempfile

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile):
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        loader = PyPDFLoader(tmp_path)
        documents = loader.load()

        # Add to Pinecone via LangChain vectorstore
        vectorstore.add_documents(documents)
        return {"message": "File uploaded and indexed successfully"}

    finally:
        os.remove(tmp_path)
