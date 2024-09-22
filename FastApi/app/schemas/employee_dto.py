# pylint: disable=too-few-public-methods
"""
Module defining the EmployeeDTO.

This DTO represents the data structure used for transferring
employee data between different layers of the application.
"""

from typing import Optional  # Importación estándar
from pydantic import BaseModel  # Importación de terceros


class EmployeeDTO(BaseModel):
    """
    DTO for Employee entity. This class represents the data structure
    used to transfer employee data between different layers of the application.

    Attributes:
        id (Optional[int]): The unique identifier for the employee. This is optional.
        name (str): The name of the employee.
        email (str): The email of the employee.
        phone (str): The phone number of the employee.
        department_id (int): The ID of the department to which the employee belongs.
    """

    id: Optional[int] = None
    name: str
    email: str
    phone: str
    department_id: int

    class Config:
        """
        Pydantic configuration class for ORM compatibility.
        """

        orm_mode = True
