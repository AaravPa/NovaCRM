from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "sqlite:///./novacrm.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI(title="NovaCRM API")

@app.on_event("startup")
async def startup():
    from app.models import Base
    Base.metadata.create_all(bind=engine)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/auth/signup")
async def signup(email: str, password: str):
    # TODO: Implement user registration
    return {"token": "jwt_token_here"}

@app.get("/contacts")
async def get_contacts():
    # TODO: Implement contact retrieval
    return {"contacts": []}
