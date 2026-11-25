# API REST Hola Mundo

Proyecto académico de una API REST desarrollado con Python y FastAPI.

## Tecnologías utilizadas
- Python
- FastAPI
- Uvicorn
- Visual Studio Code

## Instalación

1. Crear un entorno virtual:

   `python -m venv venv`

2. Activar el entorno virtual en Windows:

   `.\venv\Scripts\Activate.ps1`

3. Instalar FastAPI:

   `pip install "fastapi[standard]"`

## Ejecución

`python -m uvicorn main:app --reload`

## Endpoint

- Método: GET
- Ruta: `/api/hola`
- Dirección local: `http://127.0.0.1:8000/api/hola`

## Respuesta JSON

{
  "mensaje": "Hola Mundo",
  "lenguaje": "Python",
  "framework": "FastAPI"
}