# GeM Bid Compliance Verification Platform

An AI-powered platform to verify bidder documents for GeM (Government e-Marketplace) 
procurement. Automates document classification and gives procurement officers a 
compliance dashboard with risk scoring and AI recommendations — final decision 
always stays with the officer.

## Problem it solves
Procurement officers currently verify bidder documents (Udyam/MSME, GST, PAN, 
EPFO/ESIC, etc.) manually. This platform automates document ingestion, OCR, and 
classification to speed up and standardize that process.

## Tech Stack
- FastAPI
- PostgreSQL
- Celery + Redis
- Docker
- Tesseract OCR + Poppler (for scanned document text extraction)
- PyMuPDF (native PDF text extraction)

## Current Status
**Module 1 — Document Ingestion & Classification: Complete**
- Zip upload → safe extraction → bidder grouping → text extraction (native + OCR fallback) → keyword-based classification
- Stores results in PostgreSQL

**Planned Modules**
- Module 2: AI entity extraction (NLP/NER)
- Module 3: Multi-portal API gateway (GST, MCA21, DigiLocker) with RPA fallback
- Module 4: Cross-verification and risk scoring

## Setup
\`\`\`bash
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
docker compose up -d
uvicorn app.main:app --reload
celery -A app.tasks worker --loglevel=info --pool=solo
\`\`\`