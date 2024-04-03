import json
from datetime import datetime

class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.genero = genero

        
    def __str__(self):
        return f"Nombre:{self.nombre} , Apellido: {self.apellido}, Mail: {self.email}, Genero: {self.genero}"

instancias = [] 
with open("usuarios.txt") as usuarios:
    linea = usuarios.readline()
    while linea:
        try:
            usuario = json.loads(linea)
            # print(type(usuario))
            instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
                    
        except Exception as e:
            with open("error.log", "a+") as log:
                now = datetime.now()
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}\n")
        finally:
            linea = usuarios.readline() #next

for i in instancias:
    print(i)