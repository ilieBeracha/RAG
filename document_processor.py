from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

def load_and_split_documents(file_path: str, chunk_size: int = 500, chunk_overlap: int = 50):
    """Loads a document from the given file path and splits it into chunks."""
    logging.info(f"----------------------------------Loading and splitting documents from {file_path}")
    loader = TextLoader(file_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = splitter.split_documents(documents)
    return docs 