from app.celery_app import celery_app
from app.services.zip_handler import safe_extract_zip
from app.services.bidder_grouping import group_top_level_folders, extract_all_documents
from app.database import SessionLocal, Evaluation
from pathlib import Path

@celery_app.task
def add(x, y):
    return x + y

@celery_app.task
def process_evaluation(evaluation_id: str, zip_path: str):
    db = SessionLocal()

    try:
        extracted_path = safe_extract_zip(Path(zip_path), evaluation_id)

        db.query(Evaluation).filter_by(id=evaluation_id).update({"status": "extracted"})
        db.commit()

        folder_count = group_top_level_folders(extracted_path, evaluation_id)

        db.query(Evaluation).filter_by(id=evaluation_id).update({"status": "grouped"})
        db.commit()

        doc_count = extract_all_documents(evaluation_id, db)

        db.query(Evaluation).filter_by(id=evaluation_id).update({"status": "text_extracted"})
        db.commit()

        return {
            "extracted_path": str(extracted_path),
            "bidder_folders_found": folder_count,
            "documents_processed": doc_count,
        }

    except Exception as e:
        db.query(Evaluation).filter_by(id=evaluation_id).update({"status": f"failed: {str(e)}"})
        db.commit()
        raise

    finally:
        db.close()