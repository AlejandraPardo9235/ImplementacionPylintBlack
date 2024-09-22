"""
This module defines the routes for handling department-related operations.

It provides the following routes:
- GET / : Retrieve all departments.
- GET /{department_id} : Retrieve a specific department by its ID.
- POST /departments : Create a new department.
- PUT /{department_id} : Update an existing department.
- DELETE /{department_id} : Delete a department by its ID.
"""

from fastapi import APIRouter, Body, HTTPException
from app.models.department import (
    Department,
)  # Asegúrate de que la ruta de importación sea correcta
from app.database import DepartmentModel, database  # Ajustar la ruta de importación
from peewee import DoesNotExist

# Create a router object to handle department routes
department_route = APIRouter()


@department_route.get("/")
def get_all_departments():
    """
    Retrieve all departments from the database.


    Returns:
        list: A list of departments, each represented as a dictionary with 'id', 'name', and 'location'.

    Raises:
        HTTPException: If there is an internal server error.
    """
    try:
        departments = DepartmentModel.select()  # Fetch all departments
        department_list = [
            {
                "id": department.id,
                "name": department.name,
                "location": department.location,
            }
            for department in departments
        ]
        return department_list
    except DoesNotExist as exc:
        print(exc)
        raise HTTPException(status_code=404, detail="Department not found") from exc


@department_route.get("/{department_id}")
def get_department(department_id: int):
    """
    Retrieve a specific department by its ID.

    Args:
        department_id (int): The unique identifier of the department.

    Returns:
        dict: The department data if found.

    Raises:
        HTTPException: If the department does not exist or if there's an internal server error.
    """
    try:
        department = DepartmentModel.get(DepartmentModel.id == department_id)
        return department
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Department not found") from exc
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc


@department_route.post("/departments")
def create_department(department: Department = Body(...)):
    """
    Create a new department in the database.

    Args:
        department (Department): The department data provided in the request body.

    Returns:
        Department: The newly created department data.

    Raises:
        HTTPException: If there is an internal server error.
    """
    try:
        database.connect()  # Connect to the database
        DepartmentModel.create(
            name=department.name,
            location=department.location,
        )
        return department
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc
    finally:
        database.close()  # Ensure the database connection is closed


@department_route.put("/{department_id}")
def update_department(department_id: int, department: Department = Body(...)):
    """
    Update an existing department by its ID.

    Args:
        department_id (int): The unique identifier of the department.
        department (Department): The department data to update.

    Returns:
        dict: A success message if the update was successful.

    Raises:
        HTTPException: If the department is not found or if there's an internal server error.
    """
    try:
        existing_department = DepartmentModel.get(
            DepartmentModel.id == department_id
        )  # Find department by ID
        existing_department.name = department.name
        existing_department.location = department.location

        existing_department.save()  # Save changes to the database
        return {"message": "Department updated successfully"}
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Department not found") from exc
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc


@department_route.delete("/{department_id}")
def delete_department(department_id: int):
    """
    Delete a department by its ID.

    Args:
        department_id (int): The unique identifier of the department.

    Returns:
        str: A success message if the department was deleted.

    Raises:
        HTTPException: If the department is not found or if there's an internal server error.
    """
    try:
        department = DepartmentModel.get(DepartmentModel.id == department_id)
        department.delete_instance()
        return "Department deleted."
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Department not found") from exc
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc
