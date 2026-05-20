# Prueba Técnica (Python)

## Nombre: Juan Felipe Fajardo Garzón

## Descripción

Esta es una implementación en Python de la prueba técnica original para Android. La aplicación cumple con los mismos requisitos funcionales haciendo uso de otro lenguaje y librerías

## Estructura

```
Prueba tecnica/
├── config.py        # Archivo de configuración (URLs, credenciales, etc.)
├── database.py      # Archivo para crear y conectarse con la base de datos
├── api_client.py    # Archivo que consume los endpoints de la API
├── main.py          # Programa principal, la capa de presentación
├── requirements.txt # Librerías necesarias del proyecto
└── README.md
```

## Explicación de la Solución

### 1. Capa de Seguridad

#### Control de Versión

Esta funcionalidad se implementó en el archivo `api_client.py` dentro de la función `obtener_version()`. Lo que hace es consumir un endpoint externo que devuelve la versión actual del aplicativo que está desplegada en el servidor. Una vez que obtiene esa información, la compara con la versión local que está hardcodeada en el archivo de configuración. Si la versión del servidor es mayor a la local, significa que hay una actualización disponible y se le avisa al usuario. Si por el contrario la versión local es mayor, significa que está trabajando con una versión de desarrollo más nueva que la del servidor. Y si son iguales, pues todo está al día

#### Login

Para el `login` se consume un endpoint de autenticación que requiere headers específicos y un body con las credenciales del usuario. El código hace la petición `POST` con toda esa información y si el servidor responde con código 200, significa que el login fue exitoso. En ese caso se extraen los datos del usuario que vienen en la respuesta (usuario, identificación y nombre) y se almacenan en una variable global para mantenerlos en memoria durante toda la sesión. Si el código de respuesta es diferente a 200, se muestra un mensaje de error indicando que no se pudo iniciar sesión

### 2. Capa de Datos 

#### Base de Datos SQLite

La aplicación utiliza `SQLite` para almacenar las tablas del sistema que se obtienen desde el API. Se crea una base de datos local llamada `app_database.db` que contiene una tabla llamada `tablas_sistema` donde se guardan los nombres de todas las tablas que devuelve el endpoint. Esta tabla se limpia cada vez que se descargan nuevas tablas para evitar datos duplicados. La base de datos se crea automáticamente la primera vez que se ejecuta el programa

#### Consumo de API de Esquema

Para obtener el esquema de tablas del sistema se consume un endpoint específico que devuelve una lista con todas las tablas que existen en el backend. El código hace una petición `GET` a ese endpoint y si responde correctamente, guarda cada nombre de tabla en la base de datos `SQLite` local

### 3. Capa de Presentación

La capa de presentación está implementada en `main.py` y consiste en un menú de consola que simula las pantallas de una aplicación móvil. Cada vez que se muestra una pantalla se limpia la consola para mantener el orden

#### Pantalla HOME

La pantalla HOME es la primera que se muestra cuando el usuario ingresa a esta sección. Lo que hace es verificar si hay un usuario logueado en la variable global y si existe, muestra los tres datos principales: el usuario, la identificación y el nombre de la persona que inició sesión. Si no hay nadie logueado, simplemente muestra un mensaje indicando que no hay usuario logueado para que la persona sepa que debe iniciar sesión primero.

#### Pantalla TABLAS

La pantalla TABLAS consulta todas las tablas que se almacenaron previamente en la base de datos `SQLite` local. Primero verifica que se haya ejecutado antes la opción de cargar tablas del sistema, y si hay datos, los muestra en una lista numerada donde cada número corresponde a una tabla. Si no hay tablas disponibles significa que el usuario no ha ejecutado la opción de cargar tablas del sistema

#### Pantalla LOCALIDADES

La pantalla LOCALIDADES consume un endpoint cada vez que se accede a ella, a diferencia de las tablas que se consultan localmente. El código hace la petición `GET` y si obtiene datos, recorre cada registro mostrando la abreviación de la ciudad junto con el nombre completo. Esto permite ver todas las localidades disponibles de forma ordenada. Si por alguna razón el endpoint no responde o hay un error, se muestra un mensaje indicando que no se pudieron obtener las localidades

## Manejo de Errores

- **Try/Catch:** Se utiliza en todas las operaciones de base de datos y llamadas API
- **Errores de API:** Si el HTTP response code no es 200, se muestra un mensaje de alerta
- **Errores de conexión:** Se captura la excepción y se muestra un mensaje explicativo

## Principios Aplicados

**Responsabilidad Única:** Cada Archivo cumple con un solo objetivo:
   - `config.py`: Solo configuración
   - `database.py`: Solo acceso a datos
   - `api_client.py`: Solo consumo de EndPoints
   - `main.py`: Solo presentación


## Notas Importantes

- Esta implementación es en consola, no tiene interfaz gráfica como Android
- El propósito es demostrar la lógica y funcionamiento de los requerimientos
- Para ejecutar es necesaria la librería `requests`
- La base de datos se crea automáticamente al iniciar (archivo `app_database.db`)