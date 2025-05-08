from fastapi import APIRouter
from pydantic import BaseModel
from document_processor import load_and_split_documents
from vector_store_setup import create_vector_store
from llm_chain_setup import create_qa_chain

import logging

docs = load_and_split_documents("documents/test.txt")
vectorstore = create_vector_store(docs)
qa_chain = create_qa_chain(vectorstore)

router = APIRouter()

class QueryInput(BaseModel):
    input: str

@router.post("/run_qa")
async def run_qa(data: QueryInput):
    try:
        print(f"----------------------------------Running QA with query: {data.input}")
        result = qa_chain.invoke(input={"query": data.input})
        print(f"----------------------------------Result: {result}")
        return {"answer": result["result"]}
    except Exception as e:
        return {"error": str(e)}
    