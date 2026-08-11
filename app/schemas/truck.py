from pydantic import BaseModel

class TruckCreate(BaseModel):
    truck_no: int
    plate: str
    vin: str
    model: str
    available: bool

class TruckResponse(BaseModel):
    id: int
    truck_no: int
    plate: str
    vin: str
    model: str
    available: bool

    class Config:
        from_attributes = True

class TruckUpdate(BaseModel):
    truck_no: int
    plate: str
    vin: str
    model: str
    available: bool

class TruckStatus(BaseModel):
    available: bool