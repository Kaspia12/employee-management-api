from sqlalchemy.orm import Session

from app import models
from app.schemas import EmployeeCreate
from app.models import Employee

def create_employee(
        db: Session,
        employee: EmployeeCreate
):


    new_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        salary=employee.salary
    )

    db.add(new_employee)

    db.commit()

    db.refresh(new_employee)

    return new_employee

def get_employees(db):
    return db.query(Employee).all()

def get_employee(db, employee_id):
    return db.query(Employee).filter(Employee.id == employee_id).first()