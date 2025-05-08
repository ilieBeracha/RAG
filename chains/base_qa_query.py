from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
import logging

def create_base_chain():
    logging.info("Creating base QA chain with mistral model.")
    llm = OllamaLLM(model="mistral")
    prompt = PromptTemplate(
        input_variables=["query"],
        template="Answer the following question clearly:\n\n{query}"
    )
    chain = prompt | llm
    return chain
