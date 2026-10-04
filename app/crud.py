from sqlalchemy.orm import Session

from app import models
from app.schemas import EmployeeCreate


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