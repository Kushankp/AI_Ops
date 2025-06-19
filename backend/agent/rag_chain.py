from utils.embeddings import get_vectorstore

MIN_CONTEXT_LENGTH = 30  # or adjust based on your needs

def get_context_for_query(query: str) -> str:
    """
    Retrieves the most relevant context for the query using the vectorstore.
    Returns empty string if no meaningful context is found.
    """
    try:
        vectorstore = get_vectorstore()
        retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
        docs = retriever.get_relevant_documents(query)

        print(f"\n🔍 Query: {query}")
        print(f"📄 Retrieved {len(docs)} documents from vectorstore\n")

        combined_context = "\n\n".join([doc.page_content for doc in docs])
        
        if len(combined_context.strip()) < MIN_CONTEXT_LENGTH:
            print("⚠️ Context too short or irrelevant — falling back to general LLM response.\n")
            return ""  # Let main.py handle fallback
        else:
            for i, doc in enumerate(docs):
                print(f"--- Document {i+1} ---")
                print(doc.page_content[:300], "\n")
            return combined_context

    except Exception as e:
        print("❌ Error in get_context_for_query:", e)
        return ""
