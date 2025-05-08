
# RAG (Retrieval-Augmented Generation) QA API

This project implements a Retrieval-Augmented Generation (RAG) question-answering pipeline using FastAPI, LangChain, and Ollama with support for both chat and file-based queries.

## Project Structure

```
.
├── chains/
│   ├── base_qa_query.py        # Base chat chain (no document)
│   └── file_qa_query.py        # QA chain using document context
├── routes/
│   └── qa.py                   # Main QA route with both modes
├── vector_store/
│   └── faiss_store.py          # Vector store setup using FAISS
├── document_processor.py       # Document loader + splitter
├── main.py                     # FastAPI app entry point
├── requirements.txt
```

## Features

- Ask questions directly or by uploading a document
- Automatic document chunking and vector store creation with FAISS
- Uses `mistral` via Ollama for LLM responses
- Handles both plain queries and file-based RAG in one endpoint

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure Ollama is running with the `mistral` model:
```bash
ollama run mistral
```

3. Start the FastAPI app:
```bash
uvicorn main:app --reload
```

## API Endpoints

### `POST /qa`

Handles both plain questions and file-assisted RAG queries.

#### Parameters:
- `query`: The question you want to ask (required, `Form` field)
- `file`: A document file (`.txt`, `.csv`, etc.) to use for context (optional, `UploadFile`)

#### Behavior:
- If a file is uploaded:  
  → Splits and indexes the content, then answers using retrieval-augmented QA
- If no file is uploaded:  
  → Answers the query using a basic language model chain

## Examples

### Query without a file
```bash
curl -X POST http://localhost:8000/qa \
  -F "query=What is the capital of France?"
```

### Query with a document
```bash
curl -X POST http://localhost:8000/qa \
  -F "query=What is this document about?" \
  -F "file=@documents/example.txt"
```

## License

[Include license information here]

## Contributing

[Include contribution guidelines here]
