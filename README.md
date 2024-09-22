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
