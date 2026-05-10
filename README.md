# Laboratorio Patrones de Diseño

# Nombre: Juan Felipe Fajardo Garzón


En este taller se implementan ejemplos sencillos realizados en python de diferentes patrones de diseño de software, en la tabla de a continuacion se presenta el patron utilizado en cada uno de los ejemplos



## Códigos y patrones usados

| Archivo | Patrones implementados |
|---------|----------------------|
| `factory_example.py` | Factory |
| `sigleton_login.py` | Singleton |
| `singleton_y_estructural.py` | Singleton + Decorator |
| `tres_patrones.py` | Singleton + Decorator + Iterator |



## factory_example.py: Creación de páginas web


En este ejemplo se crea un sistema para generar diferentes tipos de páginas web (Home, Blog, Contacto, etc.) usando el patrón Factory Method.

Para ello se crea una clase abstracta llamada WebPage, esta funciona como una "plantilla" para las demás paginas, definiendo su estructura (método render)

Posteriormente en cada una de las clases para las paginas especificas se sobreescribe el método render con el códgio HTML de la página a crear, además, como argumento de cada clase específica se para la clase WebPage que funciona como plantilla.

Finalmente se usa un creator que se encarga de "fabricar" las paginas web según su código HTML específico; en este ejemplo en python se imprime el códgio HTML en consola por facilidad de implementación

### Código importante

```python
# La interfaz común que todas las páginas deben cumplir
class WebPage(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Una ejemplo de landingPage cambiando el método render
class LandingPage(WebPage):
    def render(self) -> str:
        return """
        <!DOCTYPE html>
        <html>
        <head><title>Landing Page</title></head>
        <body>
            <header><h1>Bienvenido a Nuestro Producto</h1></header>
            <section>
                <h2>Características</h2>
                <ul>
                    <li>Rápido y eficiente</li>
                    <li>Fácil de usar</li>
                    <li>Precio accesible</li>
                </ul>
            </section>
            <footer><button>Comprar Ahora</button></footer>
        </body>
        </html>
        """

# El Creator que fabrica cada tipo de página
class LandingPageCreator(WebPageCreator):
    def create_page(self) -> WebPage:
        return LandingPage()
```


### Resultado obtenido

código de la pagina/clase landing page
![alt text](media/1.png)


Código de la página/clase Blog

![alt text](media/2.png)

Código de la página/clase Contacto

![alt text](media/3.png)


### Detalles importantes

- `WebPageCreator` define el método `create_page()` pero no sabe qué tipo de página crea
- Cada subclase (`LandingPageCreator`, `BlogPageCreator`, etc.) decide qué tipo crear
- El cliente solo necesita saber que trabaja con un `WebPageCreator`, no importa cuál



## sigleton_login.py: Sistema de login

En este ejemplo se desarrolla un sistema sencillo de login haciendo uso del patrón de diseño singleton; se hace uso de este patron para manejar las sesiones del usuario. En este caso, se usa una clase "meta" la cual gestiona la creación de las instancias, dentro de esta clase se verifica si ya hay una instancia (sesion) creada con anterioridad (para no volver a crear una misma sesión 2 veces), en caso de no haber una sesión la crea y la añade a la lista

Posteriormente se crea la clase Singleton donde se implementa el sistema de login (la bd de los usuarios está hardcodeada para facilidad de implementación); en esta clase también se tiene el método que valida el usuario y contraseña ingresados, en caso de ser correctos pone el atributo authenticated como verdadero 

### Código importante

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.authenticated = False

    def login(self, username, psw):
        usuarios = {"persona1": "1234", "person2": "5678"}

        if self.authenticated is True:
            print("Usuario ya logeado")

        if username in usuarios:
            if psw == usuarios[username]:
                print("Sesion iniciada")
                self.authenticated = True


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    s1.login("persona1","1234")
```


### Resultado de la ejecucion

Primero se comprueba que las instancias sean las mismas y se obtiene un mensaje de exito (implementado en la plantilla de refactoring guru)

Luego se usa el login para iniciar sesion como uno de los usuarios registrados en la base de datos

![alt text](media/4.png)




## singleton_y_estructural.py - Sistema de notificaciones

En este ejemplo se implementa el patrón singleton y decorator para crear un sistema sencillo de notificaciones; primero se usa singleton para crear un centro de notificaciones, y que sea el mismo centro para todos los tipos de notificaciones (manejar el mismo objeto)

El centro de notificaciones tiene algunos atributos como el estado de inicializacion (verdadero cuando se crea) y el número de notificaciones enviadas en este objeto, además de un método para imprimir este último atributo

### Singleton - Centro de notificaciones

```python
class CentroNotificaciones:
    """Singleton que gestiona el centro de notificaciones."""

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if self._inicializado:
            return
        self.notificaciones_enviadas = 0
        self._inicializado = True

    def obtener_estadisticas(self) -> dict:
        return {"total_enviadas": self.notificaciones_enviadas}
```

### Decorator - Notificaciones

El patrón decorator se usa para los tipos de notificaciones, primero se tiene una notificación base la cual funciona como una "plantilla" para las otras notificaciones; en las otras clases se le añaden funcionalidades (marcas de tiempo, prefijos de tipos, etc.) a la notificación base para crear múltiples tipos, y debido a que todas comparten la misma base, todas poseen el método enviar y el atributo destinatario

```python
# Componente base
class NotificacionBase(Notificacion):
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    def enviar(self, mensaje: str) -> str:
        return f"[{self.destinatario}] {mensaje}"

# Decorator que agrega timestamp
class NotificacionConTimestamp(NotificacionDecorada):
    def enviar(self, mensaje: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {super().enviar(mensaje)}"

# Decorator que agrega prefijo
class NotificacionConPrefijo(NotificacionDecorada):
    def __init__(self, notificacion: Notificacion, prefijo: str):
        super().__init__(notificacion)
        self.prefijo = prefijo

    def enviar(self, mensaje: str) -> str:
        return super().enviar(f"[{self.prefijo}] {mensaje}")
```

### Resultado de la ejecucion

![alt text](media/5.png)


### Detalles importantes

- El Centro de Notificaciones es un Singleton siempre es la misma instancia
- Cada decorator agrega una funcionalidad sin modificar la clase original
- El componente base sigue funcionando solo a pesar de poderse "decorar"

---

## tres_patrones.py - Gestor de tareas

En este último ejemplo se aplican 3 patrones de diseño, singleton para crear un gestor de tareas como un único elemento para todas las tareas, luego se usa decorator para crear todos los tipos de tareas que puede manejar el centro de tareas y finalmente se usa iterator para recorrer todas las tareas en el centro


### Singleton - Gestor de tareas

De forma similar al ejemplo anterior se usa singleton para crear una unica instancia del centro de tareas (funciona practicamente igual que el centro de notificaciones)

```python
class GestorTareas:
    """Singleton que gestiona un listado centralizado de tareas."""

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if self._inicializado:
            return
        self.tareas: List[Tarea] = []
        self._inicializado = True

    def agregar_tarea(self, tarea: 'Tarea') -> None:
        self.tareas.append(tarea)

    def obtener_pendientes(self) -> List['Tarea']:
        return [t for t in self.tareas if not t.completada]

    def obtener_completadas(self) -> List['Tarea']:
        return [t for t in self.tareas if t.completada]
```

### Decorator - Tareas con extras

Ahora se usa Decorator donde se crea una tarea base, y luego se "decora" en clases posteriores para agregarle nuevas características a las demás tareas 

```python
# Tarea base
class TareaBase(Tarea):
    def __init__(self, titulo: str, descripcion: str = ""):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
        self.fecha_creacion = datetime.now()

    def ejecutar(self) -> str:
        self.completada = True
        return f"Tarea '{self.titulo}' completada"

# Decorator con timestamp
class TareaConTimestamp(TareaDecorada):
    def ejecutar(self) -> str:
        inicio = datetime.now().strftime("%H:%M:%S")
        resultado = super().ejecutar()
        fin = datetime.now().strftime("%H:%M:%S")
        return f"[{inicio}] {resultado} [{fin}]"

# Decorator con validación
class TareaConValidacion(TareaDecorada):
    def __init__(self, tarea: Tarea, validacion: callable):
        super().__init__(tarea)
        self.validacion = validacion

    def ejecutar(self) -> str:
        if self.validacion():
            return super().ejecutar()
        return f"Tarea '{self.tarea.titulo}' no passou na validação"

# Decorator con prioridad
class TareaConPrioridad(TareaDecorada):
    def __init__(self, tarea: Tarea, prioridad: int):
        super().__init__(tarea)
        self.prioridad = prioridad

    def get_descripcion(self) -> str:
        return f"[PRIORIDAD {self.prioridad}] {super().get_descripcion()}"
```

### Iterator - Recorrido de tareas

Finalmente se usa iterator para recorrer todas las tareas de forma eficiente, se tiene un iterator en sentido normal, y en sentido inverso

```python
# Iterador normal
class IteradorTareas(Iterator):
    def __init__(self, tareas: List[Tarea]):
        self._tareas = tareas
        self._indice = 0

    def __next__(self) -> Tarea:
        if self._indice >= len(self._tareas):
            raise StopIteration
        tarea = self._tareas[self._indice]
        self._indice += 1
        return tarea

# Iterador inverso
class IteradorInverso(Iterator):
    def __init__(self, tareas: List[Tarea]):
        self._tareas = list(reversed(tareas))
        self._indice = 0

    def __next__(self) -> Tarea:
        if self._indice >= len(self._tareas):
            raise StopIteration
        tarea = self._tareas[self._indice]
        self._indice += 1
        return tarea
```


### Resultado De la ejecucion

![alt text](media/6.png)

### Caracteristicas importantes

- Las tareas se pueden "decorar" para agregarle funcionalidades: 
- El Gestor es Singleton que siempre es la misma instancia
- Los Iterators permiten recorrer de formas diferentes sin cambiar la estructura interna de las tareas


## Referencias

https://refactoring.guru/es/design-patterns