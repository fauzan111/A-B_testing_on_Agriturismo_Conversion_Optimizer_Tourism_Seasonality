from sqlalchemy import Boolean, Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class ExperimentLog(Base):
    __tablename__ = "experiment_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    variant = Column(String) # 'A' or 'B'
    converted = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    region = Column(String, nullable=True) # For simulation/analysis later
    selected_feature = Column(String, nullable=True)
