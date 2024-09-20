from fastapi import FastAPI
from starlette.responses import RedirectResponse

#Base de datos
from routes.employee import employee_route
from routes.department import department_route

from contextlib import asynccontextmanager
from database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    #conectar a la base de datos si la conexion esta cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aqui es donde se ejecutara la aplicacion
    finally:
        # Cerrar la conexion cuando la aplicacion se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

#Rutas
app.include_router(employee_route, prefix="/employees", tags=["Employees"])
app.include_router(department_route, prefix="/departments", tags=["Departments"])