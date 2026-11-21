from abc import ABC, abstractmethod

from sistema.errores import DatosInvalidosError


class Entidad(ABC):
    """Clase base para los elementos que tienen una identificacion."""

    def __init__(self, identificacion):
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise DatosInvalidosError("La identificacion es obligatoria.")

        self._identificacion = identificacion.strip()

    @property
    def identificacion(self):
        return self._identificacion

    @abstractmethod
    def mostrar_informacion(self):
        pass
