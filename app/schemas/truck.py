from pydantic import BaseModel

class TruckCreate(BaseModel):
    truck_no: int
    model: str
    available: bool

class TruckResponse(BaseModel):
    id: int
    truck_no: int
    model: str
    available: bool

    class Config:
        from_attributes = True