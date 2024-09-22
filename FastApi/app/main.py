"""
Este módulo define la aplicación FastAPI y maneja las rutas y el ciclo de vida de la aplicación.

Proporciona las siguientes funcionalidades:
- Manejo del ciclo de vida de la aplicación para la conexión a la base de datos.
- Redirección a la documentación de la API en la raíz.
- Inclusión de rutas para manejar empleados y departamentos.
"""

# Importaciones estándar de Python
from contextlib import asynccontextmanager

# Importaciones de terceros
from starlette.responses import RedirectResponse
from fastapi import FastAPI

# Importaciones de rutas
from routes.employee import employee_route  # Asegúrate de que la ruta de importación sea correcta
from routes.department import department_route  # Asegúrate de que la ruta de importación sea correcta

# Importación de la base de datos
from database import database as connection  # Ajustar la ruta de importación

@asynccontextmanager
async def lifespan():
    """Manejo del ciclo de vida de la aplicación para conectar y desconectar de la base de datos.

    Yields:
        None: Ejecuta la aplicación en el contexto proporcionado.
    """
    if connection.is_closed():
        connection.connect()  # Conectar a la base de datos
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        if not connection.is_closed():
            connection.close()  # Cerrar la conexión a la base de datos

# Crear una instancia de la aplicación FastAPI
app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root() -> RedirectResponse:
    """Redirige a la documentación de la API.

    Returns:
        RedirectResponse: La respuesta de redirección a la documentación.
    """
    return RedirectResponse(url="/docs")

# Inclusión de rutas
app.include_router(employee_route, prefix="/employees", tags=["Employees"])
app.include_router(department_route, prefix="/departments", tags=["Departments"])
