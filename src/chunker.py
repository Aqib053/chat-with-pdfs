def split_text(pages, size=800, overlap=150):
    chunks = []
    for p in pages:
        text, start = p["text"], 0
        while start < len(text):
            chunks.append({
                "text": text[start:start + size],
                "page": p["page"],
                "source": p["source"],
            })
            start += size - overlap
    return chunks
