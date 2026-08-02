from fastapi import FastAPI
from app.database import Base, engine
from app.models.truck import Truck
from app.models.driver import Driver
from app.routes import trucks
from app.routes import drivers

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(trucks.router)
app.include_router(drivers.router)