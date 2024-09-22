# FastAPI Project with Pylint and MySQL

Este es un proyecto que utiliza **FastAPI** para crear una API con un sistema de bases de datos MySQL. Además, incluye **Pylint** para verificar la calidad del código. Se ejecuta en un contenedor **Docker** para facilitar la configuración y el despliegue.

## Requisitos previos

Asegúrate de tener instaladas las siguientes herramientas en tu máquina:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.12](https://www.python.org/)

## Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/AlejandraPardo9235/ImplementacionPylintBlack.git
cd ImplementacionPylintBlack/FastApi
```

## Instalacion sin docker

1. Crea y activa un entorno virtual (opcional pero recomendado):
```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/macOS
.\venv\Scripts\activate  # En Windows
```
2. Instala las dependencias del proyecto:
```bash
pip install -r requirements.txt
```
3. Configura las variables de entorno necesarias.
4. Inicia la aplicación.

   
## Instalacion con docker

1. Asegúrate de estar en el directorio **FastApi/**, donde está el archivo **Dockerfile** y **docker-compose.yml**.
2.  Construir la imagen de Docker:
```bash
docker compose build 
```
3. Iniciar los contenedores
```bash
docker compose up
```

## Configuracion PYLINT 
El proyecto utiliza Pylint para verificar la calidad del código. A continuación se muestran los pasos para ejecutarlo:


1. Instalación de Pylint (Si no tienes Pylint instalado en tu entorno virtual o local, puedes instalarlo con el siguiente comando)
```bash
pip install pylint
```

2. Verifica que la instalación fue exitosa ejecutando:
```bash
pylint --version
```

3. Para analizar todo el proyecto, asegúrate de estar en el directorio raíz del proyecto y ejecuta el siguiente comando:
```bash
pylint app/
```
4. Si deseas analizar un archivo específico, ejecuta el siguiente comando, reemplazando <archivo> por la ruta del archivo que deseas verificar:
```bash
pylint app/<archivo>.py
```

## Configuracion De PEP8:
PEP8 es la guía de estilo para escribir código Python limpio y legible. Aquí hay algunos puntos clave a seguir:

 - Usa 4 espacios por nivel de indentación.
 - Limita las líneas a un máximo de 79 caracteres.
 - Utiliza una línea en blanco para separar funciones y clases.
 - Los nombres de las variables y funciones deben ser en minúsculas con palabras separadas por guiones bajos (snake_case).
 - Usa nombres de clases en formato CamelCase.
   
Para aplicar las normas de PEP8 automáticamente, puedes usar Black como formateador de código.

## Configuracion De Black:
Black es una herramienta que formatea el código Python automáticamente siguiendo las reglas de PEP8.

1. Si no tienes Black instalado, puedes agregarlo ejecutando:
```bash
pip install black
```
2. Para formatear todo tu proyecto, asegúrate de estar en el directorio raíz del proyecto y ejecuta el siguiente comando:
```bash
black app/
```
3. Si deseas formatear un archivo específico, puedes hacerlo con el siguiente comando:
```bash
black app/<archivo>.py
```
4. Si deseas ver los cambios antes de aplicarlos, ejecuta Black en modo de comprobación:
```bash
black --check app/
```
