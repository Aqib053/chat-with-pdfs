from pypdf import PdfReader

def load_pdf(file):
    reader = PdfReader(file)
    name = getattr(file, "name", str(file))
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append({"text": text, "page": i, "source": name})
    return pages
