from fastapi import FastAPI

app = FastAPI(title="API Hola Mundo")


@app.get("/api/hola")
def hola_mundo():
    return {
        "mensaje": "Hola mundo",
        "lenguaje": "Python",
        "framework": "FastAPI",
    }