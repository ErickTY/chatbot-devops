import fitz  # PyMuPDF

def extract_text_from_pdfs(pdf_paths):
    content = ""
    for path in pdf_paths:
        with fitz.open(path) as doc:
            for page in doc:
                content += page.get_text()
    return content
