from fastapi import APIRouter, UploadFile, File, Form
from document_processor import load_and_split_documents
from vector_store_setup import create_vector_store
from llm_chain_setup import create_qa_chain
from create_base_chain import create_base_chain
import logging
import os
import tempfile

router = APIRouter()

@router.post("/query")
async def run_query(
    query: str = Form(...),
    file: UploadFile = File(None)
):
    try:
        if file and file.filename:
            suffix = os.path.splitext(file.filename)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(await file.read())
                tmp_path = tmp.name

            try:
                chunks = load_and_split_documents(tmp_path)
            finally:
                os.remove(tmp_path)

            vectorstore = create_vector_store(chunks)
            qa_chain = create_qa_chain(vectorstore)
            result = qa_chain.invoke({"query": query})
            return {"answer": result["result"]}
        else:
            base_chain = create_base_chain()
            result = base_chain.invoke({"query": query})
            return {"answer": result}

    except Exception as e:
        logging.error(f"--- Error during QA: {str(e)}")
        return {"error": str(e)}
