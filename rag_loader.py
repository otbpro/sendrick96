import pdfplumber
import requests
from langchain.text_splitter import CharacterTextSplitter

NARO_PDFS = [
    "https://naro.go.ug/wp-content/uploads/2025/05/NARO-Annual-Reprot-2023_2024.pdf",
    "https://naro.go.ug/wp-content/uploads/2024/02/NARO_impact_study-report-_l2-30-11-2023.pdf"
]

def load_nARO_knowledge():
    full_text = "NARO Official Knowledge Northern Uganda:\n"
    for url in NARO_PDFS:
        try:
            resp = requests.get(url)
            with open("temp.pdf", "wb") as f: f.write(resp.content)
            with pdfplumber.open("temp.pdf") as pdf:
                for page in pdf.pages:
                    full_text += page.extract_text() or "" + "\n"
        except: pass
    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    return splitter.create_documents([full_text])
