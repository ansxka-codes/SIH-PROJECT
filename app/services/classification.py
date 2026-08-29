DOCUMENT_SIGNATURES = {
    "udyam_certificate": {
        "keywords": ["udyam registration", "udyam registration number", "udyam reg"],
        "display_name": "Udyam Registration Certificate",
    },
    "gst_certificate": {
        "keywords": ["goods and services tax", "gstin", "certificate of registration"],
        "display_name": "GST Registration Certificate",
    },
    "pan_card": {
        "keywords": ["income tax department", "permanent account number", "govt. of india"],
        "display_name": "PAN Card",
    },
    "itr_acknowledgment": {
        "keywords": ["income tax return", "acknowledgement number", "assessment year"],
        "display_name": "ITR Acknowledgment",
    },
    "epfo_certificate": {
        "keywords": ["employees provident fund", "epfo", "establishment code"],
        "display_name": "EPFO Registration Certificate",
    },
}

def classify_document(text: str) -> tuple[str, str]:
    if not text:
        return "unclassified", "Unclassified Document"

    text_lower = text.lower()

    best_match = None
    best_score = 0

    for doc_type, signature in DOCUMENT_SIGNATURES.items():
        score = sum(1 for kw in signature["keywords"] if kw in text_lower)
        if score > best_score:
            best_score = score
            best_match = doc_type

    if best_match is None:
        return "unclassified", "Unclassified Document"

    return best_match, DOCUMENT_SIGNATURES[best_match]["display_name"]