"""
This module contains the Department model.
"""

from pydantic import BaseModel


class Department(BaseModel):
    """
    Department model representing a department with an id, name, and location.

    Attributes:
        id (int): The unique identifier of the department.
        name (str): The name of the department.
        location (str): The location where the department is based.
    """

    id: int
    name: str
    location: str
