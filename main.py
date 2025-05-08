from fastapi import FastAPI
from routes.query import router as query_router
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(query_router)
