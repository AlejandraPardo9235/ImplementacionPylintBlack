from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

# Conexión a la base de datos MySQL
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

# Definición del modelo de departamento
class DepartmentModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    location = CharField(max_length=100)


    class Meta:
        database = database  # Conexión a la base de datos
        table_name = "department"  # Debe coincidir con la tabla en MySQL

# Definición del modelo de empleado
class EmployeeModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    email = CharField(max_length=100)
    phone = CharField(max_length=20)
    department_id = ForeignKeyField(DepartmentModel, backref='employees', on_delete='CASCADE')



    class Meta:
        database = database  # Conexión a la base de datos
        table_name = "employee"  # Debe coincidir con la tabla en MySQL


# Prueba de conexión
try:
    database.connect()
    print("Conexión a la base de datos exitosa.")
except Exception as e:
    print(f"Error conectando a la base de datos: {e}")
finally:
    database.close()
