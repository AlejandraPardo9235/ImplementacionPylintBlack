"""
This module defines the routes for handling employee-related operations.
"""

from peewee import DoesNotExist  # Importaciones de terceros
from fastapi import APIRouter, Body, HTTPException  # Importaciones de terceros

from models.employee import Employee  # Importaciones locales
from database import EmployeeModel, database

# Crear el router para las rutas relacionadas con empleados
employee_route = APIRouter()


@employee_route.get("/")
def get_all_employees():
    """
    Retrieve all employees from the database.

    Returns:
        list: A list of employees, each represented as a dictionary with 'id', 'name', 'email',
        'phone', and 'department_id'.
    """
    try:
        employees = EmployeeModel.select()  # Fetch all employees
        employee_list = [
            {
                "id": employee.id,
                "name": employee.name,
                "email": employee.email,
                "phone": employee.phone,
                "department_id": employee.department_id,
            }
            for employee in employees
        ]
        return employee_list
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc


@employee_route.get("/{employee_id}")
def get_employee(employee_id: int):
    """
    Retrieve a specific employee by their ID.

    Args:
        employee_id (int): The unique identifier of the employee.

    Returns:
        dict: The employee data if found.

    Raises:
        HTTPException: If the employee does not exist or if there's an internal server error.
    """
    try:
        employee = EmployeeModel.get(EmployeeModel.id == employee_id)
        return employee
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Employee not found") from exc
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc


@employee_route.post("/employees")
def create_employee(employee: Employee = Body(...)):
    """
    Create a new employee in the database.

    Args:
        employee (Employee): The employee data provided in the request body.

    Returns:
        Employee: The newly created employee data.

    Raises:
        HTTPException: If there is an internal server error.
    """
    try:
        database.connect()
        EmployeeModel.create(
            name=employee.name,
            email=employee.email,
            phone=employee.phone,
            department_id=employee.department_id,
        )
        return employee
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc
    finally:
        database.close()  # Ensure the database connection is closed


@employee_route.put("/{employee_id}")
def update_employee(employee_id: int, employee: Employee = Body(...)):
    """
    Update an existing employee by their ID.

    Args:
        employee_id (int): The unique identifier of the employee.
        employee (Employee): The employee data to update.

    Returns:
        dict: A success message if the update was successful.

    Raises:
        HTTPException: If the employee is not found or if there's an internal server error.
    """
    try:
        existing_employee = EmployeeModel.get(EmployeeModel.id == employee_id)
        existing_employee.name = employee.name
        existing_employee.email = employee.email
        existing_employee.phone = employee.phone
        existing_employee.department_id = employee.department_id

        existing_employee.save()  # Save changes to the database
        return {"message": "Employee updated successfully"}
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Employee not found") from exc
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc


@employee_route.delete("/{employee_id}")
def delete_employee(employee_id: int):
    """
    Delete an employee by their ID.

    Args:
        employee_id (int): The unique identifier of the employee.

    Returns:
        str: A success message if the employee was deleted.

    Raises:
        HTTPException: If the employee is not found or if there's an internal server error.
    """
    try:
        employee = EmployeeModel.get(EmployeeModel.id == employee_id)
        employee.delete_instance()
        return "Employee deleted."
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Employee not found") from exc
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc
