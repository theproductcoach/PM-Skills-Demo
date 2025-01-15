from setup_components import vector_store

# Clear the vector store
if hasattr(vector_store, "documents"):
    vector_store.documents = []  # Clear the document list
    print("Vector store cleared.")
else:
    print("No documents to clear.")
