"""
loader.py - loading and processing documents for RAG system.
source: https://medium.com/@fsiqueira.gabriel/extraindo-dados-de-pdfs-com-pdfplumber-usando-python-a3a17c9f5839

Using pdfplumber for text and tables extraction.
PyMuPDF for images extraction.
easyocr for OCR on images. -> scanned PDFs.
"""

from csv import reader
from unittest import result
import pdfplumber
import fitz  # PyMuPDF
from PIL import Image
from pathlib import Path
import io
import os
import easyocr

reader = easyocr.Reader(['en', 'pt'])  # language list

def extract_pdf(pdf_path: str):
    """
    Extracts content from a PDF with:
    - pdfplumber for text/tables
    - PyMuPDF for images
    - easyocr fallback if text extraction fails
    
    Returns:
        List of page-level dictionaries suitable for embeddings.
    """

    pdf_path = Path(pdf_path)
    pages_content = []

    #Extract text with pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        pdf_texts = [page.extract_text() or "" for page in pdf.pages]

    #Extract images with PyMuPDF (fitz)
    doc = fitz.open(pdf_path)
    pdf_images = []
    for page in doc:
        page_images = []
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            page_images.append(image)
        pdf_images.append(page_images)

    #Join text and images per page
    for i in range(len(doc)):
        text = pdf_texts[i].strip()

        # OCR fallback if text is empty
        if not text:
            print(f"Page {i+1} has no text, performing OCR...")
            pix = doc[i].get_pixmap(dpi=300)
            name_only = os.path.splitext(os.path.basename(pdf_path))[0]
            img_path = f"docs/{name_only}_page_{i+1}.png"
            pix.save(img_path)

            result = reader.readtext(img_path, detail=0)

            text = "\n".join(result) if result else ""

            os.remove(img_path)

        page_content = {
            "page_number": i + 1,
            "text": text,
            "images": pdf_images[i]  # list of PIL.Image objects
        }
        pages_content.append(page_content)

    return pages_content