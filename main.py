from fastapi import FastAPI
from routes.qa import router as qa_router
from pydantic import BaseModel
from document_processor import load_and_split_documents
from vector_store_setup import create_vector_store
from llm_chain_setup import create_qa_chain
import logging

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

docs = load_and_split_documents("documents/test.txt")
vectorstore = create_vector_store(docs)
qa_chain = create_qa_chain(vectorstore)

app = FastAPI()
app.include_router(qa_router)
