import fitz  # pymupdf
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def extract_text_from_pdf(file_path: str) -> str:
    text_parts = []

    doc = fitz.open(file_path)
    for page in doc:
        text_parts.append(page.get_text())
    doc.close()

    return "\n".join(text_parts).strip()

def extract_forensic_metadata(file_path: str) -> dict:
    doc = fitz.open(file_path)

    metadata = doc.metadata
    producer = metadata.get("producer", None)

    has_digital_signature = False
    for page in doc:
        widgets = page.widgets() or []
        for widget in widgets:
            if widget.field_type_string == "Signature":
                has_digital_signature = True
                break
        if has_digital_signature:
            break

    fonts_seen = set()
    for page in doc:
        for font in page.get_fonts():
            fonts_seen.add(font[3])
    font_anomaly_detected = len(fonts_seen) > 5

    doc.close()

    return {
        "producer": producer,
        "has_digital_signature": has_digital_signature,
        "font_anomaly_detected": font_anomaly_detected,
    }



pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\poppler-26.02.0\Library\bin"

def ocr_image_file(file_path: str) -> str:
    image = Image.open(file_path)
    return pytesseract.image_to_string(image).strip()

def ocr_pdf(file_path: str) -> str:
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    text_parts = []
    for page_image in pages:
        text_parts.append(pytesseract.image_to_string(page_image))
    return "\n".join(text_parts).strip()