from sistema.servicio import Servicio
from sistema.errores import DatosInvalidosError


class ReservaSalas(Servicio):
    """Servicio para alquilar una sala por horas."""

    def __init__(self, identificacion, nombre, tarifa_hora, capacidad):
        super().__init__(identificacion, nombre)

        self.validar_tarifa(tarifa_hora)

        if isinstance(capacidad, bool) or not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser un numero entero positivo.")

        self.__tarifa_hora = tarifa_hora
        self.__capacidad = capacidad

    def validar_parametros(self, duracion):
        self.validar_duracion(duracion)

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        costo = self.__tarifa_hora * duracion
        return self.calcular_total(costo, impuesto, descuento)

    def describir(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Tarifa por hora: ${self.__tarifa_hora:,.2f}\n"
            f"Capacidad: {self.__capacidad} personas"
        )


class AlquilerEquipos(Servicio):
    """Servicio para alquilar equipos tecnologicos."""

    def __init__(self, identificacion, nombre, tarifa_hora, cantidad):
        super().__init__(identificacion, nombre)

        self.validar_tarifa(tarifa_hora)

        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise DatosInvalidosError("La cantidad de equipos debe ser un entero positivo.")

        self.__tarifa_hora = tarifa_hora
        self.__cantidad = cantidad

    def validar_parametros(self, duracion):
        self.validar_duracion(duracion)

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        costo = self.__tarifa_hora * duracion * self.__cantidad
        return self.calcular_total(costo, impuesto, descuento)

    def describir(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Tarifa por hora y equipo: ${self.__tarifa_hora:,.2f}\n"
            f"Cantidad de equipos: {self.__cantidad}"
        )


class Asesoria(Servicio):
    """Servicio de asesoría en un tema especializado."""

    def __init__(self, identificacion, nombre, tarifa_hora, especialidad):
        super().__init__(identificacion, nombre)

        self.validar_tarifa(tarifa_hora)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("La especialidad es obligatoria.")

        self.__tarifa_hora = tarifa_hora
        self.__especialidad = especialidad.strip()

    def validar_parametros(self, duracion):
        self.validar_duracion(duracion)

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        costo = self.__tarifa_hora * duracion
        return self.calcular_total(costo, impuesto, descuento)

    def describir(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Tarifa por hora: ${self.__tarifa_hora:,.2f}\n"
            f"Especialidad: {self.__especialidad}"
        )
