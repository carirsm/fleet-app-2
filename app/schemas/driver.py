from pydantic import BaseModel
from app.models.driver import ShiftType

class DriverCreate(BaseModel):
    driver_no: int
    first_name: str
    last_name: str
    is_hazmat: bool
    is_tanker: bool
    is_doubles: bool
    is_triples: bool
    available: bool
    shift: ShiftType

class DriverUpdate(BaseModel):
    driver_no: int
    first_name: str
    last_name: str
    is_hazmat: bool
    is_tanker: bool
    is_doubles: bool
    is_triples: bool
    available: bool
    shift: ShiftType


class DriverResponse(BaseModel):
    id: int
    driver_no: int
    first_name: str
    last_name: str
    is_hazmat: bool
    is_tanker: bool
    is_doubles: bool
    is_triples: bool
    available: bool
    shift: ShiftType

    class Config:
        from_attributes = True

class DriverStatus(BaseModel):
    available: bool