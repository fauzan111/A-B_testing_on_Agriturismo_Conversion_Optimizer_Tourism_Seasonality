from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from . import models
from .models import SessionLocal, engine
from pydantic import BaseModel
import random
import uuid
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, specify the frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BookingRequest(BaseModel):
    user_id: str
    variant: str
    region: str = "Unknown"
    selected_feature: str = None

@app.get("/api/experiment/variant")
def get_variant(user_id: str = None):
    if not user_id:
        user_id = str(uuid.uuid4())
    
    # Simple random assignment for this demo
    # In a real system, we might hash the user_id to ensure consistency
    variant = random.choice(['A', 'B'])
    
    return {"variant": variant, "user_id": user_id}

@app.post("/api/book")
def book(booking: BookingRequest, db: Session = Depends(get_db)):
    # Log the conversion
    db_log = models.ExperimentLog(
        user_id=booking.user_id,
        variant=booking.variant,
        converted=True,
        region=booking.region,
        selected_feature=booking.selected_feature
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return {"status": "success", "booking_id": db_log.id}

@app.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    total_a = db.query(models.ExperimentLog).filter(models.ExperimentLog.variant == 'A').count()
    conv_a = db.query(models.ExperimentLog).filter(models.ExperimentLog.variant == 'A', models.ExperimentLog.converted == True).count()
    
    total_b = db.query(models.ExperimentLog).filter(models.ExperimentLog.variant == 'B').count()
    conv_b = db.query(models.ExperimentLog).filter(models.ExperimentLog.variant == 'B', models.ExperimentLog.converted == True).count()
    
    return {
        "A": {"total": total_a, "converted": conv_a},
        "B": {"total": total_b, "converted": conv_b}
    }
