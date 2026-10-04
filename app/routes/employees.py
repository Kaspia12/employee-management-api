from fastapi import APIRouter, Depends, HTTPException
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

@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse
)

def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.get_employee(
        db,
        employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    updated_employee = crud.update_employee(
        db,
        employee_id,
        employee
    )

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee

@router.delete("/{employee_id}", response_model=EmployeeResponse)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    deleted_employee = crud.delete_employee(db, employee_id)

    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return deleted_employee