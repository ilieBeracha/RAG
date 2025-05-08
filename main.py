from fastapi import FastAPI
from routes.qa import router as qa_router
from dotenv import load_dotenv
import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(markup=True)]
)

logger = logging.getLogger("rich")

load_dotenv()

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

logging.info("Starting FastAPI app.")
app = FastAPI()
logging.info("Including QA router.")
app.include_router(qa_router)
