from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.truck import Truck
from app.schemas.truck import TruckCreate, TruckResponse, TruckUpdate, TruckStatus

router = APIRouter()

@router.get('/trucks', response_model=list[TruckResponse])
def get_trucks(db: Session = Depends(get_db)):
    return db.query(Truck).all()

@router.post('/trucks', status_code=201, response_model=TruckResponse)
def create_truck(truck_data: TruckCreate, db: Session = Depends(get_db)):
    new_truck = Truck(truck_no=truck_data.truck_no, plate=truck_data.plate, vin=truck_data.vin, model=truck_data.model, available=truck_data.available)
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

@router.put('/trucks/{truck_id}', response_model=TruckResponse)
def update_truck(truck_id: int, truck_data: TruckUpdate, db: Session = Depends(get_db)):
    truck = db.query(Truck).filter(Truck.id == truck_id).first()
    if not truck:
        raise HTTPException(status_code=404, detail="Truck not found")
    setattr(truck, "truck_no", truck_data.truck_no)
    setattr(truck, "plate", truck_data.plate)
    setattr(truck,"vin", truck_data.vin)
    setattr(truck, "model", truck_data.model)
    setattr(truck, "available", truck_data.available)
    db.commit()
    db.refresh(truck)
    return truck

@router.patch('/trucks/{truck_id}', response_model=TruckResponse)
def update_truck_status(truck_id: int, truck_data: TruckStatus, db: Session = Depends(get_db)):
    truck = db.query(Truck).filter(Truck.id == truck_id).first()
    if not truck:
        raise HTTPException(status_code=404, detail="Truck not found")
    setattr(truck, "available", truck_data.available)
    db.commit()
    db.refresh(truck)
    return truck

@router.delete('/trucks/{truck_id}')
def delete_truck(truck_id: int, db: Session = Depends(get_db)):
    truck = db.query(Truck).filter(Truck.id == truck_id).first()
    if not truck:
        raise HTTPException(status_code=404, detail="Truck not found")
    db.delete(truck)
    db.commit()
    return {"message": "Truck deleted"}