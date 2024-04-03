import json

class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.genero = genero

        
    def __str__(self):
        return f"Nombre:{self.nombre} , Apellido: {self.apellido}, Mail: {self.email}, Genero: {self.genero}"

# instancias = [] 
# with open("usuarios.txt") as usuarios:
#     linea = usuarios.readline()
#     while linea:
#         usuario = json.loads(linea) # dict
#         # print(type(usuario))
#         instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
        
#         instancias.append(Producto(producto["nombre"], producto["precio"]))

#         linea = usuarios.readline() #next


# for i in instancias:
#     print(i)


# """ EJEMPLO PARA DESARROLLAR LA SEGUNDA PARTE DEL DESAFIO"""
instancias = [] 
with open("usuarios.txt") as usuarios:
    linea = usuarios.readline()
    while linea:
        try:
            usuario = json.loads(linea) # dict
            print(type(usuario))
            instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
        
            
        except Exception as e:

            """Buscar codigo para generar el error.log"""
        finally:
            linea = usuarios.readline() #next

for i in instancias:
    print(i)