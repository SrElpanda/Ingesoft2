# Capa de Datos: DB SQLite

import sqlite3

def conectar():
    try:
        conexion = sqlite3.connect("app_database.db")
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise

def crear_tablas():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT,
                identificacion TEXT,
                nombre TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tablas_sistema (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_tabla TEXT
            )
        """)

        conn.commit()
        conn.close()
        print("Tablas creadas exitosamente")
    except Exception as e:
        print(f"Error al crear tablas: {e}")
        raise

def guardar_tablas(tablas):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tablas_sistema")

        for tabla in tablas:
            cursor.execute(
                "INSERT INTO tablas_sistema (nombre_tabla) VALUES (?)",
                (tabla,)
            )

        conn.commit()
        conn.close()
        print(f"Se guardaron {len(tablas)} tablas exitosamente")
    except Exception as e:
        print(f"Error al guardar tablas: {e}")
        raise


def obtener_tablas():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre_tabla FROM tablas_sistema")
        resultado = cursor.fetchall()
        conn.close()
        return [fila[0] for fila in resultado]
    except Exception as e:
        print(f"Error al obtener tablas: {e}")
        return []