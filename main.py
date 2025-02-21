from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import crud

from crud import create_city
from engine import engine, SessionLocal
from database import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/cities/")
def create_city(name: str, additional_info: str, db: Session = Depends(get_db)):
    return crud.create_city(db, name, additional_info)
