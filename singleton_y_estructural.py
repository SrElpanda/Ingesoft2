from abc import ABC, abstractmethod
from datetime import datetime


# ============================================================
# PATRÓN DECORATOR - Sistema de Notificaciones
# ============================================================

class Notificacion(ABC):
    """Interfaz base para todas las notificaciones."""

    @abstractmethod
    def enviar(self, mensaje: str) -> str:
        pass


class NotificacionBase(Notificacion):
    """Componente concreto: notificación básica."""

    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    def enviar(self, mensaje: str) -> str:
        return f"[{self.destinatario}] {mensaje}"


class NotificacionDecorada(Notificacion):
    """Decorator base que envuelve otra notificación."""

    def __init__(self, notificacion: Notificacion):
        self._notificacion = notificacion

    @property
    def notificacion(self) -> Notificacion:
        return self._notificacion

    def enviar(self, mensaje: str) -> str:
        return self._notificacion.enviar(mensaje)


class NotificacionConTimestamp(NotificacionDecorada):
    """Decorator que agrega timestamp."""

    def enviar(self, mensaje: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {super().enviar(mensaje)}"


class NotificacionConLogs(NotificacionDecorada):
    """Decorator que agrega logging."""

    def __init__(self, notificacion: Notificacion):
        super().__init__(notificacion)
        self.logs = []

    def enviar(self, mensaje: str) -> str:
        resultado = super().enviar(mensaje)
        self.logs.append(resultado)
        print(f"LOG: {resultado}")
        return resultado


class NotificacionConMayusculas(NotificacionDecorada):
    """Decorator que convierte el mensaje a mayúsculas."""

    def enviar(self, mensaje: str) -> str:
        return super().enviar(mensaje.upper())


class NotificacionConPrefijo(NotificacionDecorada):
    """Decorator que agrega un prefijo al mensaje."""

    def __init__(self, notificacion: Notificacion, prefijo: str):
        super().__init__(notificacion)
        self.prefijo = prefijo

    def enviar(self, mensaje: str) -> str:
        return super().enviar(f"[{self.prefijo}] {mensaje}")


# ============================================================
# PATRÓN SINGLETON - Centro de Notificaciones
# ============================================================

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

    def configurar_notificacion(self, notificacion: Notificacion) -> Notificacion:
        """Configura y retorna una notificación decorateada lista para usar."""
        self.notificaciones_enviadas += 1
        return notificacion

    def obtener_estadisticas(self) -> dict:
        return {
            "total_enviadas": self.notificaciones_enviadas
        }


# ============================================================
# CLIENTE
# ============================================================

def client_code(notificacion: Notificacion) -> None:
    resultado = notificacion.enviar("Hola mundo")
    print(f"RESULTADO: {resultado}")


if __name__ == "__main__":
    print("=== Ejemplo Decorator + Singleton ===\n")

    # Obtener centro de notificaciones (Singleton)
    centro1 = CentroNotificaciones()
    centro2 = CentroNotificaciones()

    print(f"Misma instancia? {id(centro1) == id(centro2)}\n")

    # Notificación básica
    print("1. Notificación básica:")
    basic = NotificacionBase("usuario@email.com")
    client_code(basic)

    # Agregar timestamp (Decorator)
    print("\n2. Con timestamp:")
    with_timestamp = NotificacionConTimestamp(basic)
    client_code(with_timestamp)

    # Agregar mayúsculas + prefijo (Decorator encadenado)
    print("\n3. Con mayúsculas + prefijo:")
    decorated = NotificacionConPrefijo(
        NotificacionConMayusculas(basic),
        "URGENTE"
    )
    client_code(decorated)

    # Notificación completa: timestamp + prefijo
    print("\n4. Notificación completa (timestamp + prefijo):")
    completa = NotificacionConPrefijo(
        NotificacionConTimestamp(basic),
        "INFO"
    )
    client_code(completa)

    # Ver estadísticas del centro
    print(f"\nEstadísticas del centro: {centro1.obtener_estadisticas()}")