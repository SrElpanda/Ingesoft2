# Capa de Seguridad: Consumo de API

import requests
import config

def obtener_version():
    try:
        response = requests.get(config.URL_VERSION)

        if response.status_code != 200:
            print(f"Error al obtener versión: Código HTTP {response.status_code}")
            return None

        data = response.json()
        if not isinstance(data, str): # Verifica que sea un string puesto que el EndPoint devuelve siempre "100"
            print(f"Error: Formato de respuesta inesperado")
            return None

        version_api = data
        print(f"Versión API: {version_api}")
        return int(version_api)

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def login():
    try:
        headers = config.LOGIN_HEADERS
        data = config.LOGIN_DATA

        response = requests.post(
            config.URL_LOGIN,
            json=data,
            headers=headers
        )

        if response.status_code != 200:
            print(f"Error en login: Código HTTP {response.status_code}")
            return None
        response_data = response.json()

        if not isinstance(response_data, dict):
            print(f"Error: Formato de respuesta inesperado en login")
            return None

        print(f"Login exitoso")
        return response_data

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión en login: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado en login: {e}")
        return None

def obtener_tablas():
    try:
        response = requests.get(config.URL_TABLAS)

        if response.status_code != 200:
            print(f"Error al obtener tablas: Código HTTP {response.status_code}")
            return []

        data = response.json()
        if not isinstance(data, dict):
            print(f"Error: Formato de respuesta inesperado")
            return []
        
        tablas = data.get("Table", [])
        print(f"Se obtieron {len(tablas)} tablas del API")
        return tablas

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []

def obtener_localidades():
    try:
        response = requests.get(config.URL_LOCALIDADES)

        if response.status_code != 200:
            print(f"Error al obtener localidades: Código HTTP {response.status_code}")
            return []

        data = response.json()
        if isinstance(data, list):
            localidades = data
        else:
            print(f"Error: Formato de respuesta inesperado")
            return []

        print(f"Se obtieron {len(localidades)} localidades del API")
        return localidades

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []