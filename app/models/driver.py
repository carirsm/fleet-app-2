from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Enum
import enum

class ShiftType(enum.Enum):
    day = "day"
    night = "night"
    naca = "naca"
    out_of_town = "out_of_town"

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, index=True, primary_key=True)
    driver_no = Column(Integer, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_hazmat = Column(Boolean, nullable=False)
    is_tanker = Column(Boolean, nullable=False)
    is_doubles = Column(Boolean, nullable=False)
    is_triples = Column(Boolean, nullable=False)
    available = Column(Boolean, default=True, nullable=False)
    shift = Column(Enum(ShiftType), nullable=False)