# Capa de Presentación: Programa Principal

import os
import api_client
import database
import config

usuario_logueado = None

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def pantalla_home():
    global usuario_logueado
    limpiar_consola()
    print("HOME")

    if usuario_logueado:
        print(f"Usuario: {usuario_logueado['usuario']}")
        print(f"Identificación: {usuario_logueado['identificacion']}")
        print(f"Nombre: {usuario_logueado['nombre']}")
    else:
        print("No hay usuario logueado")

def pantalla_tablas():
    limpiar_consola()
    print("TABLAS")

    tablas = database.obtener_tablas()

    if tablas:
        print(f"Se encontraron {len(tablas)} tablas:")
        for i, tabla in enumerate(tablas, 1):
            print(f"  {i}. {tabla}")
    else:
        print("No hay tablas disponibles")

    print("\nPresione Enter para volver al Home")
    input()
    pantalla_home()

def pantalla_localidades():
    limpiar_consola()
    print("LOCALIDADES")

    localidades = api_client.obtener_localidades()

    if localidades:
        print(f"Se encontraron {len(localidades)} localidades:\n")
        for loc in localidades:
            abreviacion = loc.get("AbreviacionCiudad", "N/A")
            nombre = loc.get("NombreCompleto", "N/A")
            print(f"  - {abreviacion}: {nombre}")
    else:
        print("No se pudieron obtener las localidades")

    print("\nPresione Enter para volver al Home")
    input()
    pantalla_home()

def verificar_version():
    print("\nObteniendo versión")

    version_api = api_client.obtener_version()
    version_local = config.VERSION_LOCAL

    if version_api:
        if version_api > version_local:
            print(f"La versión local {version_local} es inferior a la versión del servidor {version_api}")
        elif version_api < version_local:
            print(f"La versión local {version_local} es superior a la versión del servidor {version_api}")
        else:
            print(f"La versión está actualizada: {version_local}")
    else:
        print("No se pudo verificar la versión")

def iniciar_sesion():
    global usuario_logueado
    print("\nIniciando sesión")

    datos_login = api_client.login()

    if datos_login:
        usuario_logueado = {
            "usuario": datos_login.get("Usuario", ""),
            "identificacion": datos_login.get("Identificacion", ""),
            "nombre": datos_login.get("Nombre", "")
        }
        print("Sesión iniciada")
        return True
    else:
        print("Error: No se pudo iniciar sesión")
        return False

def cargar_tablas():
    print("\nDescargando tablas de la API")

    tablas = api_client.obtener_tablas()

    if tablas:
        database.guardar_tablas(tablas)
        print("Tablas guardadas Correctamente")
    else:
        print("No se pudieron obtener las tablas")

def menu_principal():
    while True:
        limpiar_consola()
        print("PRUEBA TECNICA: PYTHON")
        print("1. Verificar versión")
        print("2. Iniciar sesión")
        print("3. Cargar tablas del sistema")
        print("4. Ir a Home")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            verificar_version()
            input("\nPresione Enter para continuar")
        elif opcion == "2":
            iniciar_sesion()
            input("\nPresione Enter para continuar")
        elif opcion == "3":
            cargar_tablas()
            input("\nPresione Enter para continuar")
        elif opcion == "4":
            pantalla_home()
            while True:
                print("\nSeleccione una opción:")
                print("1. Ver Tablas")
                print("2. Ver Localidades")
                print("3. Volver al menú principal")
                sub_opcion = input("Opción: ")

                if sub_opcion == "1":
                    pantalla_tablas()
                elif sub_opcion == "2":
                    pantalla_localidades()
                elif sub_opcion == "3":
                    break
                else:
                    print("Opción inválida")
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_principal()