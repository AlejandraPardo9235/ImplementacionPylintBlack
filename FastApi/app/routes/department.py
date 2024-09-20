from fastapi import APIRouter, Body, HTTPException
from models.department import Department

from database import DepartmentModel, database

department_route = APIRouter()


@department_route.get("/")
def get_all_departments():
    try:
        departments = DepartmentModel.select()  # Obtén todos los departamentos
        # Convierte los departamentos a un formato serializable
        department_list = [{
            "id": department.id,
            "name": department.name,
            "location": department.location,
        } for department in departments]
        return department_list
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@department_route.get("/{departmentId}")
def get_department(departmentId: int):
    try:
        department = DepartmentModel.get(DepartmentModel.id == departmentId)
        return department
    except Exception as e:
        print(e)
        return {"error": str(e)}


@department_route.post("/departments")
def create_department(department: Department = Body(...)):
    try:
        database.connect()
        DepartmentModel.create(
            name=department.name, 
            location=department.location, 
        )
        return department
    except Exception as e:
        print(e)
        return {"error": str(e)}
    finally:
        database.close()  # Asegúrate de cerrar la conexión


@department_route.put("/{departmentId}")
def update_department(departmentId: int,department: Department = Body(...)):
    try:
        existing_department = DepartmentModel.get(DepartmentModel.id == departmentId)  # Busca el departamento por ID
        
        # Actualiza los campos del departamento con los valores del cuerpo de la solicitud
        existing_department.name = department.name
        existing_department.location = department.location
        
        existing_department.save()  # Guarda los cambios en la base de datos
        return {"message": "Department updated successfully"}
    except DepartmentModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Department not found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@department_route.delete("/{departmentId}")
def delete_department(departmentId: int):
    try:
        department = DepartmentModel.get(DepartmentModel.id == departmentId)
        department.delete_instance()
        return "Department, Deleted."
    except Exception as e:
        print(e)
        return {"error":str(e)}