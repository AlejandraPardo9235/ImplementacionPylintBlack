"""
Este módulo contiene la lógica del servicio para manejar las operaciones de empleados,
interactuando con el modelo de la base de datos y convirtiendo los datos a modelos Pydantic.
"""

from typing import List, Optional
from peewee import DoesNotExist
from ..database import EmployeeModel, database  # Asegúrate de que la ruta sea correcta
from ..models.employee import Employee  # Asegúrate de que la ruta sea correcta


class EmployeeService:
    """Capa de servicio para las operaciones de empleado."""

    @staticmethod
    def get_all_employees() -> List[Employee]:
        """
        Recupera todos los empleados de la base de datos.

        Returns:
            List[Employee]: Una lista de instancias de empleado.
        """
        try:
            employees = EmployeeModel.select()
            return [
                Employee.from_orm(employee)  # Convierte el modelo de Peewee a modelo de Pydantic
                for employee in employees
            ]
        except DoesNotExist:
            return []  # O puedes manejar una excepción específica si lo deseas

    @staticmethod
    def get_employee_by_id(employee_id: int) -> Optional[Employee]:
        """
        Recupera un empleado por su ID.

        Args:
            employee_id (int): El ID del empleado.

        Returns:
            Optional[Employee]: El empleado si se encuentra, de lo contrario None.
        """
        try:
            employee = EmployeeModel.get(EmployeeModel.id == employee_id)
            return Employee.from_orm(employee)
        except DoesNotExist:
            return None

    @staticmethod
    def create_employee(employee_data: Employee) -> Employee:
        """
        Crea un nuevo empleado.

        Args:
            employee_data (Employee): Los datos del empleado proporcionados.

        Returns:
            Employee: El empleado recién creado.
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
        Actualiza un empleado existente por su ID.

        Args:
            employee_id (int): El ID del empleado a actualizar.
            employee_data (Employee): Los nuevos datos del empleado.

        Returns:
            bool: True si la actualización fue exitosa, de lo contrario False.
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
        Elimina un empleado por su ID.

        Args:
            employee_id (int): El ID del empleado a eliminar.

        Returns:
            bool: True si el empleado fue eliminado, de lo contrario False.
        """
        try:
            employee = EmployeeModel.get(EmployeeModel.id == employee_id)
            employee.delete_instance()
            return True
        except DoesNotExist:
            return False
