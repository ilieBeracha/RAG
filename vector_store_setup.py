from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import logging

def create_vector_store(docs, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """Creates a FAISS vector store from the given documents and embedding model."""
    logging.info(f"----------------------------------Creating vector store with {model_name} model")
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore 