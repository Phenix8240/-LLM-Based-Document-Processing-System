import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
sys.path.append(os.path.abspath(".."))
from app.services.pdf_utils import download_pdf,extract_text_from_pdf

class OutputRequest(BaseModel):
    documents: str
    questions: List[str]

app = FastAPI()

@app.get("/")
def root():
    return {"status" : "Api is running"}

@app.post("/api/v1/hackrx/run")
def run(req: OutputRequest):
   path = download_pdf(req.documents)
   text = extract_text_from_pdf(path)
   return{
       "message":"Pdf extracted",
       "size" : len(text),
       "summary": text[:500],
       "questions": req.questions
   }
