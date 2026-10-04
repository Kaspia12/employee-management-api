from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):

    name: str
    email: EmailStr
    department: str
    salary: float


class EmployeeResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    department: str
    salary: float

    class Config:
        from_attributes = True