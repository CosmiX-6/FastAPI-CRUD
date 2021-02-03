from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class StudentSchema(BaseModel):
    fullname : str = Field(...)
    email : EmailStr = Field(...)
    course : str = Field(...)
    year : int = Field(...,gt=0, lt=10)
    cgpa : float = Field(...,le=10.00)

    class Config:
        schema_extra = {
            "emaxple": {
                "fullname" : "Akash Sharma",
                "email" : "asprox.head124@gmail.com",
                "course" : "FastAPI",
                "year" : 1,
                "cgpa" : "9.1",
            }
        }

class UpdateStudentModel(BaseModel):
    fullname : Optional[str]
    email : Optional[EmailStr]
    course : Optional[str]
    year : Optional[int]
    cgpa : Optional[float]

    class Config:
        schema_extra = {
            "example" : {
                "fullname": "Akash Sharma",
                "email": "asprox.head124@gmail.com",
                "course": "FastAPI - Pro",
                "year": 2,
                "cgpa": "4.0",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}