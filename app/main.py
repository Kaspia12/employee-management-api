from fastapi import FastAPI
from app.database import engine
from app.database import Base
from app.routes import employees
from app import models
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(
    employees.router
)

@app.get("/")
def home():
    return {"message": "Employee Management API is running!"}


