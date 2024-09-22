from typing import List, Optional
from peewee import DoesNotExist
from database import EmployeeModel, database
from models.employee import Employee


class EmployeeService:
    """Service layer for Employee operations."""

    @staticmethod
    def get_all_employees() -> List[Employee]:
        """
        Retrieve all employees from the database.

        Returns:
            List[Employee]: A list of employee instances.
        """
        try:
            employees = EmployeeModel.select()
            return [
                Employee.from_orm(employee)  # Convert Peewee model to Pydantic model
                for employee in employees
            ]
        except Exception:
            return []

    @staticmethod
    def get_employee_by_id(employee_id: int) -> Optional[Employee]:
        """
        Retrieve an employee by their ID.

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            Optional[Employee]: The employee if found, otherwise None.
        """
        try:
            employee = EmployeeModel.get(EmployeeModel.id == employee_id)
            return Employee.from_orm(employee)
        except DoesNotExist:
            return None

    @staticmethod
    def create_employee(employee_data: Employee) -> Employee:
        """
        Create a new employee.

        Args:
            employee_data (Employee): The employee data provided.

        Returns:
            Employee: The newly created employee.
        """
        try:
            database.connect()
            employee = EmployeeModel.create(
                name=employee_data.name,
                email=employee_data.email,
                phone=employee_data.phone,
                department_id=employee_data.department_id,
            )
            return Employee.from_orm(employee)
        finally:
            database.close()

    @staticmethod
    def update_employee(employee_id: int, employee_data: Employee) -> bool:
        """
        Update an existing employee by their ID.

        Args:
            employee_id (int): The ID of the employee to update.
            employee_data (Employee): The new employee data.

        Returns:
            bool: True if the update was successful, otherwise False.
        """
        try:
            employee = EmployeeModel.get(EmployeeModel.id == employee_id)
            employee.name = employee_data.name
            employee.email = employee_data.email
            employee.phone = employee_data.phone
            employee.department_id = employee_data.department_id
            employee.save()
            return True
        except DoesNotExist:
            return False

    @staticmethod
    def delete_employee(employee_id: int) -> bool:
        """
        Delete an employee by their ID.

        Args:
            employee_id (int): The ID of the employee to delete.

        Returns:
            bool: True if the employee was deleted, otherwise False.
        """
        try:
            employee = EmployeeModel.get(EmployeeModel.id == employee_id)
            employee.delete_instance()
            return True
        except DoesNotExist:
            return False
