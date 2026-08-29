from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, DateTime, Integer

DATABASE_URL = "postgresql://gem_user:gem_pass@localhost:5432/gem_verification"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid, datetime

class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    original_zip_name = Column(String)
    status = Column(String, default="uploaded")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class BidderFolder(Base):
    __tablename__ = "bidder_folders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    evaluation_id = Column(UUID(as_uuid=True))
    raw_folder_name = Column(String)
    document_count = Column(Integer, default=0)

class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bidder_folder_id = Column(UUID(as_uuid=True))
    original_relative_path = Column(String)
    stored_path = Column(String)
    extension = Column(String)
    extracted_text = Column(String)
    classification_status = Column(String, default="pending")
    classified_type = Column(String)
    display_name = Column(String)