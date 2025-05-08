# RAG (Retrieval-Augmented Generation) QA Chain Setup

This project provides a simple setup for creating a Retrieval-Augmented Generation (RAG) question-answering (QA) chain using [LangChain](https://github.com/langchain-ai/langchain) and [Ollama](https://ollama.com/).

## Features

- Uses the `mistral` model via Ollama for LLM responses.
- Integrates with any LangChain-compatible vector store for document retrieval.
- Returns both answers and source documents for transparency.

## Requirements

- Python 3.8+
- [LangChain](https://python.langchain.com/)
- [langchain-ollama](https://github.com/langchain-ai/langchain-ollama)
- An Ollama server running with the `mistral` model available

Install dependencies:

```bash
pip install langchain langchain-ollama
```

## Usage

1. **Set up your vector store** (see LangChain docs for options).
2. **Import and use the chain setup:**

```python
from llm_chain_setup import create_qa_chain

# Assume you have a vectorstore object ready
qa_chain = create_qa_chain(vectorstore)

# Ask a question
result = qa_chain({"query": "What is retrieval-augmented generation?"})
print(result["result"])
print(result["source_documents"])
```

## File Overview

- `llm_chain_setup.py`: Contains the `create_qa_chain` function to build a QA chain with a specified vector store and LLM model.

## Customization

- Change the model by passing a different `model_name` to `create_qa_chain`.
- Extend the chain with custom prompts or chain types as needed.

## License

MIT License
# RAG
# RAG
# RAG
