from utils.embeddings import get_vectorstore  # This must now be a function, not a global object

def get_context_for_query(query: str) -> str:
    """
    Retrieves the most relevant context from Pinecone using the query.
    This function ensures lazy loading to avoid OOM issues during app startup.
    """
    # Lazy load the vectorstore to reduce memory usage at import time
    vectorstore = get_vectorstore()
    
    # Use a retriever with fewer docs to limit memory
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    # Fetch documents
    docs = retriever.get_relevant_documents(query)
    
    # Debug logging
    print(f"\n🔍 Query: {query}")
    print(f"📄 Retrieved {len(docs)} documents from Pinecone\n")
    for i, doc in enumerate(docs):
        print(f"--- Document {i+1} ---")
        print(doc.page_content[:300], "\n")  # preview

    # Combine document content
    return "\n\n".join([doc.page_content for doc in docs])
