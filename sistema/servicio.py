import math
from abc import abstractmethod

from sistema.entidad import Entidad
from sistema.errores import DatosInvalidosError


class Servicio(Entidad):
    """Clase base para los servicios que ofrece Software FJ."""

    def __init__(self, identificacion, nombre, disponible=True):
        super().__init__(identificacion)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")

        if not isinstance(disponible, bool):
            raise DatosInvalidosError("La disponibilidad debe ser verdadera o falsa.")

        self._nombre = nombre.strip()
        self._disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        if not isinstance(valor, bool):
            raise DatosInvalidosError("La disponibilidad debe ser verdadera o falsa.")

        self._disponible = valor

    def validar_tarifa(self, tarifa):
        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)):
            raise DatosInvalidosError("La tarifa debe ser un numero.")

        if not math.isfinite(tarifa) or tarifa <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")

    def validar_duracion(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise DatosInvalidosError("La duración debe ser un numero.")

        if not math.isfinite(duracion) or duracion <= 0:
            raise DatosInvalidosError("La duracion debe ser mayor que cero.")

    def validar_impuesto_descuento(self, impuesto, descuento):
        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)):
            raise DatosInvalidosError("El impuesto debe ser un numero.")

        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
            raise DatosInvalidosError("El descuento debe ser un numero.")

        if not math.isfinite(impuesto) or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 100.")

        if not math.isfinite(descuento) or not 0 <= descuento <= 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

    def calcular_total(self, costo, impuesto, descuento):
        if isinstance(costo, bool) or not isinstance(costo, (int, float)):
            raise DatosInvalidosError("El costo calculado no es valido.")

        if not math.isfinite(costo) or costo < 0:
            raise DatosInvalidosError("El costo calculado no es valido.")

        self.validar_impuesto_descuento(impuesto, descuento)

        costo_con_descuento = costo - (costo * descuento / 100)
        total = costo_con_descuento + (costo_con_descuento * impuesto / 100)

        return round(total, 2)

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    def mostrar_informacion(self):
        return self.describir()
