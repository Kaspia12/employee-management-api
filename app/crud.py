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

def update_employee(db, employee_id, employee_data):
    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee is None:
        return None

    employee.name = employee_data.name
    employee.email = employee_data.email
    employee.department = employee_data.department
    employee.salary = employee_data.salary

    db.commit()
    db.refresh(employee)

    return employee

def delete_employee(db, employee_id):
    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee is None:
        return None

    db.delete(employee)
    db.commit()

    return employee