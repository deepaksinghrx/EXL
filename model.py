from pydantic import BaseModel

# creating a base model
class Employee(BaseModel):
    name: str
    department: str
    age: int

class EmployeeUpdate(BaseModel):
    name: str
    department: str
    age: int

class addEmployee(BaseModel):
    name: str
    department: str
    age: int 
