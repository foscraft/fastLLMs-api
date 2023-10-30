import time
from typing import Any
from fastapi import  HTTPException, Depends
from core import app
from core.main_module import setup_chain


app = FastAPI()
@app.post("/api/v1/ask", response_model=Any)
async def ask_question(data: dict, qa=Depends(setup_chain)):
    """
    Ask Question API Endpoint.

    Submit a query and receive an answer from the language model chain.

    Request Body (Content-Type: application/json):
    """
    query = data.get("query")
    if not query:
        raise HTTPException(status_code=400, detail="Please provide a query.")

    start = time.time()
    res = qa(query)
    answer, docs = (
        res["result"],
        []
        if app.state.config.get("HIDE_SOURCE", False)
        else res["source_documents"],
    )
    end = time.time()

    # Convert Document objects to dictionaries
    docs_json = [doc.__dict__ for doc in docs]

    return {
        "answer": answer,
        "documents": docs_json,
        "query_time": round(end - start, 3),
    }
