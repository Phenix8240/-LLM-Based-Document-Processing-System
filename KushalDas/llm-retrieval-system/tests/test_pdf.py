from app.services.pdf_utils import download_pdf, extract_text_from_pdf

pdf_url = "https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf"

pdf_path = download_pdf(pdf_url)
text = extract_text_from_pdf(pdf_path)

print("Extracted characters:", len(text))
print("Preview:\n", text[:500])  # First 500 chars
