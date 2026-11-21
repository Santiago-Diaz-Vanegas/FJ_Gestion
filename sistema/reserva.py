from sistema.cliente import Cliente
from sistema.servicio import Servicio
from sistema.errores import (
    DatosInvalidosError,
    ReservaInvalidaError,
    ServicioNoDisponibleError
)
from sistema.registro import registrar_evento


class Reserva:
    """Relaciona un cliente con un servicio y controla su estado."""

    def __init__(self, identificacion, cliente, servicio, duracion):
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise DatosInvalidosError("La identificación de la reserva es obligatoria.")

        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError("La reserva necesita un cliente valido.")

        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError("La reserva necesita un servicio valido.")

        servicio.validar_parametros(duracion)

        self.__identificacion = identificacion.strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise ReservaInvalidaError("Solo se pueden confirmar reservas pendientes.")

        if not self.__servicio.disponible:
            raise ServicioNoDisponibleError("El servicio no se encuentra disponible.")

        self.__servicio.disponible = False
        self.__estado = "Confirmada"

        registrar_evento(f"Reserva {self.__identificacion} confirmada.")
        return "La reserva fue confirmada correctamente."

    def cancelar(self):
        if self.__estado not in ("Pendiente", "Confirmada"):
            raise ReservaInvalidaError("No se puede cancelar una reserva en este estado.")

        if self.__estado == "Confirmada":
            self.__servicio.disponible = True

        self.__estado = "Cancelada"
        registrar_evento(f"Reserva {self.__identificacion} cancelada.")

        return "La reserva fue cancelada correctamente."

    def procesar(self, impuesto=0, descuento=0):
        if self.__estado != "Confirmada":
            raise ReservaInvalidaError("La reserva debe estar confirmada para procesarse.")

        try:
            total = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )

        except Exception as error:
            # Se conserva el error original para saber qué causó el problema.
            raise ReservaInvalidaError(
                "No se pudo calcular el costo de la reserva."
            ) from error

        else:
            self.__estado = "Procesada"
            self.__servicio.disponible = True
            registrar_evento(
                f"Reserva {self.__identificacion} procesada. Total: ${total:,.2f}"
            )
            return total

        finally:
            # Este registro se realiza tanto si el cálculo funciona o tanto si falla.
            registrar_evento(
                f"Termino el intento de procesamiento de la reserva {self.__identificacion}."
            )

    def mostrar_informacion(self):
        return (
            f"Reserva: {self.__identificacion}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion} horas\n"
            f"Estado: {self.__estado}"
        )
