from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Truck(Base):

    __tablename__ = "trucks"

    id = Column(Integer, index=True, primary_key=True)
    truck_no = Column(Integer, nullable=False)
    plate = Column(String, nullable=False)
    vin = Column(String, nullable=False)
    model = Column(String, nullable=False)
    available = Column(Boolean, nullable=False)
