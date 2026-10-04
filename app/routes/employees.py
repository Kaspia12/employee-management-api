from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import EmployeeCreate, EmployeeResponse
from app import crud


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.post(
    "/",
    response_model=EmployeeResponse
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    return crud.create_employee(
        db,
        employee
    )
@router.get(
    "/",
    response_model=list[EmployeeResponse]
)
def get_employees(
    db: Session = Depends(get_db)
):
    return crud.get_employees(db)