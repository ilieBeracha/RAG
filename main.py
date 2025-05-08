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

app = FastAPI()
app.include_router(qa_router)

if __name__ == "__main__":
    import uvicorn
    logging.info("Running app with uvicorn on 0.0.0.0:8000")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
