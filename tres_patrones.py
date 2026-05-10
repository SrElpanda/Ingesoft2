from abc import ABC, abstractmethod
from datetime import datetime
from typing import Iterator, List


# ============================================================
# PATRÓN SINGLETON - Gestor de Tareas
# ============================================================

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

    def obtener_todas(self) -> List['Tarea']:
        return self.tareas

    def obtener_pendientes(self) -> List['Tarea']:
        return [t for t in self.tareas if not t.completada]

    def obtener_completadas(self) -> List['Tarea']:
        return [t for t in self.tareas if t.completada]


# ============================================================
# PATRÓN DECORATOR - Tareas con funcionalidades extra
# ============================================================

class Tarea(ABC):
    """Interfaz base para las tareas."""

    @abstractmethod
    def ejecutar(self) -> str:
        pass

    @abstractmethod
    def get_descripcion(self) -> str:
        pass


class TareaBase(Tarea):
    """Tarea básica."""

    def __init__(self, titulo: str, descripcion: str = ""):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
        self.fecha_creacion = datetime.now()

    def ejecutar(self) -> str:
        self.completada = True
        return f"Tarea '{self.titulo}' completada"

    def get_descripcion(self) -> str:
        return f"{self.titulo}: {self.descripcion}"


class TareaDecorada(Tarea):
    """Decorator base para tareas."""

    def __init__(self, tarea: Tarea):
        self._tarea = tarea

    @property
    def tarea(self) -> Tarea:
        return self._tarea

    def ejecutar(self) -> str:
        return self._tarea.ejecutar()

    def get_descripcion(self) -> str:
        return self._tarea.get_descripcion()

    @property
    def completada(self) -> bool:
        return self._tarea.completada

    @completada.setter
    def completada(self, value: bool):
        self._tarea.completada = value


class TareaConTimestamp(TareaDecorada):
    """Decorator que agrega timestamp al ejecutar."""

    def ejecutar(self) -> str:
        inicio = datetime.now().strftime("%H:%M:%S")
        resultado = super().ejecutar()
        fin = datetime.now().strftime("%H:%M:%S")
        return f"[{inicio}] {resultado} [{fin}]"


class TareaConValidacion(TareaDecorada):
    """Decorator que valida antes de ejecutar."""

    def __init__(self, tarea: Tarea, validacion: callable):
        super().__init__(tarea)
        self.validacion = validacion

    def ejecutar(self) -> str:
        if self.validacion():
            return super().ejecutar()
        return f"Tarea '{self.tarea.titulo}' no passou na validação"


class TareaConRetry(TareaDecorada):
    """Decorator que reintenta la tarea si falla."""

    def __init__(self, tarea: Tarea, max_reintentos: int = 3):
        super().__init__(tarea)
        self.max_reintentos = max_reintentos

    def ejecutar(self) -> str:
        intentos = 0
        while intentos < self.max_reintentos:
            try:
                return super().ejecutar()
            except Exception as e:
                intentos += 1
                if intentos >= self.max_reintentos:
                    return f"Error después de {intentos} intentos: {e}"
        return "Tarea fallida"


class TareaConPrioridad(TareaDecorada):
    """Decorator que agrega prioridad."""

    def __init__(self, tarea: Tarea, prioridad: int):
        super().__init__(tarea)
        self.prioridad = prioridad

    def get_descripcion(self) -> str:
        return f"[PRIORIDAD {self.prioridad}] {super().get_descripcion()}"


# ============================================================
# PATRÓN ITERATOR - Recorrer tareas
# ============================================================

class IteradorTareas(Iterator):
    """Iterator para recorrer tareas."""

    def __init__(self, tareas: List[Tarea]):
        self._tareas = tareas
        self._indice = 0

    def __next__(self) -> Tarea:
        if self._indice >= len(self._tareas):
            raise StopIteration
        tarea = self._tareas[self._indice]
        self._indice += 1
        return tarea


class IteradorInverso(Iterator):
    """Iterator que recorre en orden inverso."""

    def __init__(self, tareas: List[Tarea]):
        self._tareas = list(reversed(tareas))
        self._indice = 0

    def __next__(self) -> Tarea:
        if self._indice >= len(self._tareas):
            raise StopIteration
        tarea = self._tareas[self._indice]
        self._indice += 1
        return tarea


# ============================================================
# EJEMPLO DE USO
# ============================================================

if __name__ == "__main__":
    print("=== Singleton + Decorator + Iterator ===\n")

    # Obtener gestor (Singleton)
    gestor = GestorTareas()
    gestor2 = GestorTareas()

    print(f"Misma instancia? {id(gestor) == id(gestor2)}\n")

    # Crear tareas base
    tarea1 = TareaBase("Estudiar Python", "Patrones de diseño")
    tarea2 = TareaBase("Hacer ejercicio", "30 minutos")
    tarea3 = TareaBase("Leer libro", "Capítulo 5")

    # Aplicar decorators
    tarea1_decorada = TareaConTimestamp(tarea1)
    tarea2_decorada = TareaConPrioridad(tarea2, prioridad=1)
    tarea3_decorada = TareaConValidacion(
        TareaConTimestamp(tarea3),
        validacion=lambda: len("test") > 0
    )

    # Agregar al gestor
    gestor.agregar_tarea(tarea1_decorada)
    gestor.agregar_tarea(tarea2_decorada)
    gestor.agregar_tarea(tarea3_decorada)

    # Iterar con Iterator normal
    print("=== Recorrido normal ===")
    for tarea in IteradorTareas(gestor.obtener_todas()):
        print(f"  - {tarea.get_descripcion()}")

    # Iterar en orden inverso
    print("\n=== Recorrido inverso ===")
    for tarea in IteradorInverso(gestor.obtener_todas()):
        print(f"  - {tarea.get_descripcion()}")

    # Ejecutar tareas
    print("\n=== Ejecutando tareas ===")
    for tarea in gestor.obtener_todas():
        print(f"  {tarea.ejecutar()}")

    # Ver estadísticas
    print(f"\nTotal tareas: {len(gestor.obtener_todas())}")
    print(f"Pendientes: {len(gestor.obtener_pendientes())}")
    print(f"Completadas: {len(gestor.obtener_completadas())}")