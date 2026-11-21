import re

from sistema.entidad import Entidad
from sistema.errores import DatosInvalidosError


class Cliente(Entidad):
    """Guarda los datos de una persona que utiliza los servicios."""

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion)

        self.__nombre = self.validar_nombre(nombre)
        self.__correo = self.validar_correo(correo)
        self.__telefono = self.validar_telefono(telefono)

    def validar_nombre(self, nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) < 2:
            raise DatosInvalidosError("El nombre debe tener al menos dos caracteres.")

        return nombre.strip()

    def validar_correo(self, correo):
        if not isinstance(correo, str):
            raise DatosInvalidosError("El correo debe ser un texto.")

        correo = correo.strip().lower()
        patron = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not re.fullmatch(patron, correo):
            raise DatosInvalidosError("El formato del correo no es valido.")

        return correo

    def validar_telefono(self, telefono):
        if not isinstance(telefono, str):
            raise DatosInvalidosError("El telefono debe ingresarse como texto.")

        telefono = telefono.strip()
        numeros = re.sub(r"\D", "", telefono)

        if not 7 <= len(numeros) <= 15:
            raise DatosInvalidosError("El numero de telefono no es valido.")

        return telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"Identificacion: {self.identificacion}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )
