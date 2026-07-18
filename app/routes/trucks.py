from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.truck import Truck
from app.schemas.truck import TruckCreate, TruckResponse

router = APIRouter()

@router.get('/trucks', response_model=list[TruckResponse])
def get_trucks(db: Session = Depends(get_db)):
    return db.query(Truck).all()