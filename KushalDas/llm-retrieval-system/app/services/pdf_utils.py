import fitz
import requests
import tempfile
from pathlib import Path

def download_pdf(url : str) -> Path:
    response = requests.get(url)
    response.raise_for_status()
    temporaryFile = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temporaryFile.write(response.content)
    temporaryFile.close()
    return Path(temporaryFile.name)

def extract_text_from_pdf(pdfFilePath : Path) -> str:
    pdf = fitz.open(pdfFilePath)
    text = ""
    for page in pdf:    
        text+=page.get_text("text")
    return text