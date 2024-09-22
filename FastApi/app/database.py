"""
Este módulo define los modelos para interactuar con la base de datos MySQL,
incluyendo los modelos de departamento y empleado, y maneja la conexión a la base de datos.
"""

# Importaciones estándar de Python
import os

# Importaciones de terceros
from dotenv import load_dotenv
from peewee import (
    MySQLDatabase,
    Model,
    CharField,
    AutoField,
    ForeignKeyField,
    DatabaseError,
)

# Cargar variables de entorno
load_dotenv()

# Conexión a la base de datos MySQL utilizando las variables de entorno
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


# Modelo de departamento
class DepartmentModel(Model):
    """Modelo que representa un departamento en la base de datos.

    Atributos:
        id (AutoField): Identificador único del departamento.
        name (CharField): Nombre del departamento.
        location (CharField): Ubicación del departamento.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    location = CharField(max_length=100)

    class Meta:
        database = database
        table_name = "department"


# Modelo de empleado
class EmployeeModel(Model):
    """Modelo que representa un empleado en la base de datos.

    Atributos:
        id (AutoField): Identificador único del empleado.
        name (CharField): Nombre del empleado.
        email (CharField): Correo electrónico del empleado.
        phone (CharField): Número de teléfono del empleado.
        department_id (ForeignKeyField): Referencia al departamento al que pertenece el empleado.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    email = CharField(max_length=100)
    phone = CharField(max_length=20)
    department_id = ForeignKeyField(
        DepartmentModel, backref="employees", on_delete="CASCADE"
    )

    class Meta:
        database = database
        table_name = "employee"


# Prueba de conexión a la base de datos
if __name__ == "__main__":
    try:
        database.connect()
        print("Conexión a la base de datos exitosa.")
    except DatabaseError as e:
        print(f"Error conectando a la base de datos: {e}")
    finally:
        database.close()
