from fastapi import APIRouter, HTTPException
from py_env.model import Employee, EmployeeUpdate
from py_env.database import employees
router =APIRouter(
    prefix="/employee",
    tags=["employee"]
)

router.get("/")
def get_employees():
    return {
        "msg": "List of all employees",
        "data": employees
    }

@router.get("/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            return {
                "msg": "Employee found",
                "data": employee
            }
    raise HTTPException(status_code=404, detail="Employee not found")

@router.put("/{employee_id}")
def update_employee(employee_id: int, employee_update: EmployeeUpdate):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            employee["name"] = employee_update.name
            employee["department"] = employee_update.department
            employee["age"] = employee_update.age
            return {
                "msg": "Employee updated successfully",
                "data": employee
            }
    raise HTTPException(status_code=404, detail="Employee not found")

@router.post("/add_employee")
def add_employee(employee: Employee):
    try:
        employee_id = max(e["employee_id"] for e in employees) + 1
    except ValueError:
        employee_id = 1
    new_employee = {
        "employee_id": employee_id,
        "name": employee.name,
        "department": employee.department,
        "age": employee.age
    }
    employees.append(new_employee)
    return {
        "msg": "Employee added successfully",
        "data": new_employee
    }