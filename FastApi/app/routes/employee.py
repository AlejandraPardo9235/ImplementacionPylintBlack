from fastapi import APIRouter, Body, HTTPException
from models.employee import Employee

from database import EmployeeModel, database

employee_route = APIRouter()


@employee_route.get("/")
def get_all_employees():
    try:
        employees = EmployeeModel.select()  # Obtén todos los empleados
        # Convierte los empleados a un formato serializable
        employee_list = [{
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "phone": employee.phone,  # Asegúrate de que el nombre del campo es correcto
            "department_id": employee.department_id
        } for employee in employees]
        return employee_list
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@employee_route.get("/{employeeId}")
def get_employee(employeeId: int):
    try:
        employee = EmployeeModel.get(EmployeeModel.id == employeeId)
        return employee
    except Exception as e:
        print(e)
        return {"error": str(e)}


@employee_route.post("/employees")
def create_employee(employee: Employee = Body(...)):
    try:
        database.connect()
        EmployeeModel.create(
            name=employee.name, 
            email=employee.email, 
            phone=employee.phone, 
            department_id=employee.department_id
        )
        return employee
    except Exception as e:
        print(e)
        return {"error": str(e)}
    finally:
        database.close()  # Asegúrate de cerrar la conexión


@employee_route.put("/{employeeId}")
def update_employee(employeeId: int,employee: Employee = Body(...)):
    try:
        existing_employee = EmployeeModel.get(EmployeeModel.id == employeeId)  # Busca el empleado por ID
        
        # Actualiza los campos del empleado con los valores del cuerpo de la solicitud
        existing_employee.name = employee.name
        existing_employee.email = employee.email
        existing_employee.phone = employee.phone
        existing_employee.department_id = employee.department_id
        
        existing_employee.save()  # Guarda los cambios en la base de datos
        return {"message": "Employee updated successfully"}
    except EmployeeModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Employee not found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@employee_route.delete("/{employeeId}")
def delete_employee(employeeId: int):
    try:
        employee = EmployeeModel.get(EmployeeModel.id == employeeId)
        employee.delete_instance()
        return "Empleado, borrado"
    except Exception as e:
        print(e)
        return {"error":str(e)}