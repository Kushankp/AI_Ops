from utils.embeddings import get_vectorstore

def get_context_for_query(query: str) -> str:
    """
    Retrieves the most relevant context from Pinecone using the query.
    """
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(query)
    return "\n\n".join([doc.page_content for doc in docs])
