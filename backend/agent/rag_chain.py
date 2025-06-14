from utils.embeddings import get_vectorstore

def get_context_for_query(query: str) -> str:
    """
    Retrieves the most relevant context from Pinecone using the query.
    """
    vectorstore = get_vectorstore()
    
    # Set number of documents to retrieve
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})  # increase from default 4

    # Retrieve documents
    docs = retriever.get_relevant_documents(query)
    
    print(f"\n🔍 Query: {query}")
    print(f"📄 Retrieved {len(docs)} documents from Pinecone\n")

    for i, doc in enumerate(docs):
        print(f"--- Document {i+1} ---")
        print(doc.page_content[:300], "\n")  # preview first 300 chars

    return "\n\n".join([doc.page_content for doc in docs])
