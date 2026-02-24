# En este programa se presentan un ejemplo del 
# uso de las sugerencias de Stride en un ambito sencillo 
# como es el inicio de sesión de un usuario


import hashlib

# Creamos una función para encriptar las contraseñas, evitar spoofing e information disclosure
def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()


# Diccionario de usuarios permitidos
users = {
    "juan":hash_pw("4321"),
    "sergio":hash_pw("1234")
}


logs = [] # Creamos un arreglo para llevar registro de inicios de sesion, evitar repudiation

def login(user,password):
        if users.get(user) == hash_pw(password):
            logs.append(user) # Añadimos el usuario que inicio sesion
            print("Inicio de sesión correcto")
            return True
        else:
            print("inicio de sesión fallido")
            return False


intentos = 0
while intentos <5: # Tener un contador de intentos para evitar un DoS
    user_in = input("Ingrese su usuario: ")
    passwors_in  = input("Ingrese su contraseña: ")
    if login(user_in,passwors_in):
        break
    else:
        intentos +=1


