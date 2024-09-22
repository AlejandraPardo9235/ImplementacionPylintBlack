"""
This module defines routes for handling department operations.

It provides the following routes:
- GET / : Retrieve all departments.
- GET /{department_id} : Retrieve a specific department by ID.
- POST /departments : Create a new department.
- PUT /{department_id} : Update an existing department.
- DELETE /{department_id} : Delete a department by ID.
"""

from fastapi import APIRouter, Body, HTTPException
from models.department import Department  # Ensure the import path is correct
from database import DepartmentModel, database  # Adjust the import path
from peewee import DoesNotExist

department_route = APIRouter()

@department_route.get("/")
def get_all_departments():
    """
    Retrieve all departments from the database.

    Returns:
        list: A list of departments, each as a dict with 'id', 'name', and 'location'.

    Raises:
        HTTPException: If there is an internal server error.
    """
    try:
        departments = DepartmentModel.select()
        return [
            {"id": dept.id, "name": dept.name, "location": dept.location}
            for dept in departments
        ]
    except DoesNotExist as exc:
        print(exc)
        raise HTTPException(status_code=404, detail="Department not found") from exc

@department_route.get("/{department_id}")
def get_department(department_id: int):
    """
    Retrieve a department by its ID.

    Args:
        department_id (int): The department's unique identifier.

    Returns:
        dict: The department data if found.

    Raises:
        HTTPException: If the department does not exist.
    """
    try:
        department = DepartmentModel.get(DepartmentModel.id == department_id)
        return {"id": department.id, "name": department.name, "location": department.location}
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
        department (Department): The department data from the request body.

    Returns:
        dict: The newly created department data.

    Raises:
        HTTPException: If there is an internal server error.
    """
    try:
        database.connect()
        new_dept = DepartmentModel.create(
            name=department.name,
            location=department.location,
        )
        return {"id": new_dept.id, "name": new_dept.name, "location": new_dept.location}
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc
    finally:
        database.close()

@department_route.put("/{department_id}")
def update_department(department_id: int, department: Department = Body(...)):
    """
    Update a department by its ID.

    Args:
        department_id (int): The department's unique identifier.
        department (Department): The updated department data.

    Returns:
        dict: A success message if the update was successful.

    Raises:
        HTTPException: If the department is not found.
    """
    try:
        existing_department = DepartmentModel.get(
            DepartmentModel.id == department_id
        )
        existing_department.name = department.name
        existing_department.location = department.location
        existing_department.save()
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
        department_id (int): The department's unique identifier.

    Returns:
        str: A success message if the department was deleted.

    Raises:
        HTTPException: If the department is not found.
    """
    try:
        department = DepartmentModel.get(DepartmentModel.id == department_id)
        department.delete_instance()
        return {"message": "Department deleted."}
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Department not found") from exc
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error") from exc
