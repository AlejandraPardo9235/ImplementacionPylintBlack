"""
Module defining the DepartmentDTO.

This DTO represents the data structure used for transferring
department data between different layers of the application.
"""

from typing import Optional  # Importación estándar
from pydantic import BaseModel  # Importación de terceros


class DepartmentDTO(BaseModel):
    # pylint: disable=too-few-public-methods
    """
    DTO for Department entity. This class represents the data structure
    used to transfer department data between different layers of the application.

    Attributes:
        id (Optional[int]): The unique identifier for the department. This is optional.
        name (str): The name of the department.
        location (str): The location of the department.
    """
    id: Optional[int] = None
    name: str
    location: str

    class Config:
        """
        Pydantic configuration class for ORM compatibility.
        """

        orm_mode = True
