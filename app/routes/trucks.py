from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.truck import Truck
from app.schemas.truck import TruckCreate, TruckResponse

router = APIRouter()

@router.get('/trucks', response_model=list[TruckResponse])
def get_trucks(db: Session = Depends(get_db)):
    return db.query(Truck).all()

@router.post('/trucks', status_code=201, response_model=TruckResponse)
def create_truck(truck_data: TruckCreate, db: Session = Depends(get_db)):
    new_truck = Truck(truck_no=truck_data.truck_no, model=truck_data.model, available=truck_data.available)
    db.add(new_truck)
    db.commit()
    db.refresh(new_truck)
    return new_truck

@router.get('/trucks/{truck_id}', response_model=TruckResponse)
def get_truck(truck_id: int, db: Session = Depends(get_db)):
    truck = db.query(Truck).filter(Truck.id == truck_id).first()
    if not truck:
        raise HTTPException(status_code=404, detail="Truck not found")
    return truck