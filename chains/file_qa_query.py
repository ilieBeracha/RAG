from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_ollama import OllamaLLM

import logging

def base_qa_query(vectorstore, model_name="mistral"):
    """Creates a RetrievalQA chain with the given vector store and LLM model."""
    logging.info(f"----------------------------------Creating QA chain with {model_name} model")
    llm = OllamaLLM(model="mistral")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )
    return qa_chain 