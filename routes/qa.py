from fastapi import APIRouter, UploadFile, File, Form
from document_processor import load_and_split_documents
from vector_store.faiss_store import create_vector_store
from chains.file_qa_query import base_qa_query
from chains.base_qa_query import create_base_chain
import logging
import os
import tempfile

router = APIRouter()

@router.post("/qa")
async def run_query(
    query: str = Form(...),
    file: UploadFile = File(None)
):
    logging.info("Received QA request.")
    try:
        if file and file.filename:
            logging.info(f"File uploaded: {file.filename}")
            suffix = os.path.splitext(file.filename)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(await file.read())
                tmp_path = tmp.name

            try:
                logging.info(f"Processing and splitting document: {tmp_path}")
                chunks = load_and_split_documents(tmp_path)
            finally:
                os.remove(tmp_path)
                logging.info(f"Temporary file removed: {tmp_path}")

            logging.info("Creating vector store from document chunks.")
            vectorstore = create_vector_store(chunks)
            logging.info("Creating QA chain and invoking query.")
            qa_chain = base_qa_query(vectorstore)
            result = qa_chain.invoke({"query": query})
            logging.info("Returning QA result.")
            return {"answer": result["result"]}
        else:
            logging.info("No file uploaded, using base chain.")
            base_chain = create_base_chain()
            result = base_chain.invoke({"query": query})
            logging.info("Returning base chain result.")
            return {"answer": result}

    except Exception as e:
        logging.error(f"--- Error during QA: {str(e)}")
        return {"error": str(e)}
