from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverResponse, DriverUpdate, DriverStatus

router = APIRouter()

@router.get('/drivers', response_model=list[DriverResponse])
def get_drivers(db: Session = Depends(get_db)):
    return db.query(Driver).all()

@router.post('/drivers', status_code=201, response_model=DriverResponse)
def create_driver(driver_data: DriverCreate, db: Session = Depends(get_db)):
    new_driver = Driver(
        driver_no=driver_data.driver_no,
        first_name=driver_data.first_name,
        last_name=driver_data.last_name,
        is_hazmat=driver_data.is_hazmat,
        is_tanker=driver_data.is_tanker,
        is_doubles=driver_data.is_doubles,
        is_triples=driver_data.is_triples,
        available=driver_data.available,
        shift=driver_data.shift
    )
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)
    return new_driver

@router.get('/drivers/{driver_id}', response_model=DriverResponse)
def get_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.put('/drivers/{driver_id}', response_model=DriverResponse)
def update_driver(driver_id: int, driver_data: DriverUpdate, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    setattr(driver, "driver_no", driver_data.driver_no)
    setattr(driver, "first_name", driver_data.first_name)
    setattr(driver, "last_name", driver_data.last_name)
    setattr(driver, "is_hazmat", driver_data.is_hazmat)
    setattr(driver, "is_tanker", driver_data.is_tanker)
    setattr(driver, "is_doubles", driver_data.is_doubles)
    setattr(driver, "is_triples", driver_data.is_triples)
    setattr(driver, "available", driver_data.available)
    setattr(driver, "shift", driver_data.shift)
    db.commit()
    db.refresh(driver)
    return driver

@router.patch('/drivers/{driver_id}', response_model=DriverResponse)
def update_driver_status(driver_id: int, driver_data: DriverStatus, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    setattr(driver, "available", driver_data.available)
    db.commit()
    db.refresh(driver)
    return driver

@router.delete('/drivers/{driver_id}')
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    db.delete(driver)
    db.commit()
    return {"message": "Driver deleted"}