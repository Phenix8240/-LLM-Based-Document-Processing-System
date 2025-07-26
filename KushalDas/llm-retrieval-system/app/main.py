from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class OutputRequest(BaseModel):
    document: str
    question: List[str]

app = FastAPI()

@app.get("/")
def root():
    return {"status" : "Api is running"}

@app.post("/api/v1/hackrx/run")
def run(req: OutputRequest):
    return { "message" : "Received successfully",
             "document_url": req.document,
             "question": req.question}
