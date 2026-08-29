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
     "esic_certificate": [
        "employees state insurance", "esic", "esi corporation",
        "insurance number", "employer code", "sub code",
        "esic registration", "e.s.i. act", "insurable employment"
    ],

    "startup_india_certificate": [
        "startup india", "dpiit", "department for promotion of industry",
        "certificate of recognition", "startup recognition number",
        "recognition certificate", "startup india scheme",
        "innovative", "scalable business model"
    ],

    "nsic_certificate": [
        "national small industries corporation", "nsic",
        "single point registration", "spr certificate",
        "nsic registration", "monetary limit",
        "tender marketing", "public procurement policy"
    ],

    "oem_authorization": [
        "original equipment manufacturer", "oem", "authorization letter",
        "authorized dealer", "authorized distributor", "manufacturer authorization",
        "authorized to sell", "authorized to bid", "on behalf of the manufacturer",
        "letter of authorization"
    ],

    "digilocker_document": [
        "digilocker", "digital locker", "issued via digilocker",
        "digitally signed", "e-sign", "meripehchaan",
        "digilocker verified", "government of india digilocker"
    ],

    "board_resolution_poa": [
        "board resolution", "power of attorney", "poa",
        "authorized signatory", "resolved that", "board of directors",
        "hereby authorize", "in pursuance of section", "notarized",
        "certified true copy of resolution"
    ],

    "self_declaration": [
        "self declaration", "undertaking", "hereby declare",
        "i/we declare", "solemnly affirm", "declaration form",
        "on affidavit", "non-blacklisting declaration", "no litigation certificate"
    ],

    "financial_statement": [
        "balance sheet", "profit and loss", "audited financial statement",
        "annual turnover", "chartered accountant", "auditor's report",
        "net worth certificate", "ca certificate", "financial year ended",
        "statement of accounts"
    ],

    "blacklisting_debarment": [
        "blacklisting", "debarment", "not blacklisted", "not debarred",
        "banned list", "holiday listed", "suspension of business dealings",
        "no adverse action", "certificate of non-blacklisting"
    ],

    "make_in_india_local_content": [
        "make in india", "local content", "class-i local supplier",
        "class-ii local supplier", "domestic value addition",
        "purchase preference", "local content percentage",
        "self-certification of local content"
    ],
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