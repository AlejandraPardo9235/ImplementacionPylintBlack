"""
This module contains the Employee model.
"""

from pydantic import BaseModel


class Employee(BaseModel):
    """
    Employee model representing an employee with an id, name, email, phone, and department_id.

    Attributes:
        id (int): The unique identifier of the employee.
        name (str): The name of the employee.
        email (str): The email address of the employee.
        phone (str): The phone number of the employee.
        department_id (int): The identifier of the department the employee belongs to.
    """

    id: int
    name: str
    email: str
    phone: str
    department_id: int

    class Config:
        """
        Configuration for the Employee model to enable ORM mode.
        """

        orm_mode = True
