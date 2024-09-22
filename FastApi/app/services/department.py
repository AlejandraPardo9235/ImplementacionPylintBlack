from typing import List, Optional
from peewee import DoesNotExist
from app.database import DepartmentModel, database
from app.models.department import Department


class DepartmentService:
    """Service layer for Department operations."""

    @staticmethod
    def get_all_departments() -> List[Department]:
        """
        Retrieve all departments from the database.

        Returns:
            List[Department]: A list of department instances.
        """
        try:
            departments = DepartmentModel.select()
            return [
                Department.from_orm(
                    department
                )  # Convert Peewee model to Pydantic model
                for department in departments
            ]
        except DoesNotExist:
            return []

    @staticmethod
    def get_department_by_id(department_id: int) -> Optional[Department]:
        """
        Retrieve a department by its ID.

        Args:
            department_id (int): The ID of the department.

        Returns:
            Optional[Department]: The department if found, otherwise None.
        """
        try:
            department = DepartmentModel.get(DepartmentModel.id == department_id)
            return Department.from_orm(department)
        except DoesNotExist:
            return None

    @staticmethod
    def create_department(department_data: Department) -> Department:
        """
        Create a new department.

        Args:
            department_data (Department): The department data provided.

        Returns:
            Department: The newly created department.
        """
        try:
            database.connect()
            department = DepartmentModel.create(
                name=department_data.name,
                location=department_data.location,
            )
            return Department.from_orm(department)
        finally:
            database.close()

    @staticmethod
    def update_department(department_id: int, department_data: Department) -> bool:
        """
        Update an existing department by its ID.

        Args:
            department_id (int): The ID of the department to update.
            department_data (Department): The new department data.

        Returns:
            bool: True if the update was successful, otherwise False.
        """
        try:
            department = DepartmentModel.get(DepartmentModel.id == department_id)
            department.name = department_data.name
            department.location = department_data.location
            department.save()
            return True
        except DoesNotExist:
            return False

    @staticmethod
    def delete_department(department_id: int) -> bool:
        """
        Delete a department by its ID.

        Args:
            department_id (int): The ID of the department to delete.

        Returns:
            bool: True if the department was deleted, otherwise False.
        """
        try:
            department = DepartmentModel.get(DepartmentModel.id == department_id)
            department.delete_instance()
            return True
        except DoesNotExist:
            return False
