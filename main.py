from typing import Optional
from fastapi import FastAPI

app = FastAPI()

//////////////////////

<<<<<<< HEAD
v2.0////////////////
=======
v2.0/////////////////
>>>>>>> desarrollo
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/listar")
def listar():
    f = open("demofile.txt", "r")
    return f.read()

@app.post("/alta/{nombre}/{telefono}")
def dar_alta(nombre: str, telefono: str):
    f = open("demofile.txt", "w")
    # {
    # "nombre": "pepe",
    # "telefono": "5551234"
    # }
    f.write("{\"nombre\":\"" + nombre + "\",\"telefono\":\"" + telefono + "\"}")
    f.close()
    return {"alta":"ok"}
