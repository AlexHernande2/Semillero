import json
import os

FILE = "usuarios.json"

# Asegura que el archivo exista
def init_data():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump({}, f)

def cargar_usuarios():
    with open(FILE, "r") as f:
        return json.load(f)

def guardar_usuario(cedula, data):
    usuarios = cargar_usuarios()
    usuarios[cedula] = data
    with open(FILE, "w") as f:
        json.dump(usuarios, f, indent=4)

def usuario_existe(cedula):
    usuarios = cargar_usuarios()
    return cedula in usuarios
