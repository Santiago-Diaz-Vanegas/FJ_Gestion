from sistema.cliente import Cliente
from sistema.servicio import Servicio
from sistema.reserva import Reserva
from sistema.errores import (
    DatosInvalidosError,
    ClienteNoEncontradoError,
    ServicioNoEncontradoError
)
from sistema.registro import registrar_evento


class GestorSistema:
    """Guarda y administra los clientes servicios y reservas."""

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

    def registrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError("El dato recibido no es un cliente.")

        for cliente_guardado in self.__clientes:
            if cliente_guardado.identificacion == cliente.identificacion:
                raise DatosInvalidosError("Ya existe un cliente con esa identificacion.")

        self.__clientes.append(cliente)
        registrar_evento(f"Se registró el cliente {cliente.identificacion}.")
        return "Cliente registrado correctamente."

    def registrar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError("El dato recibido no es un servicio.")

        for servicio_guardado in self.__servicios:
            if servicio_guardado.identificacion == servicio.identificacion:
                raise DatosInvalidosError("Ya existe un servicio con esa identificacion.")

        self.__servicios.append(servicio)
        registrar_evento(f"Se registró el servicio {servicio.identificacion}.")
        return "Servicio registrado correctamente."

    def buscar_cliente(self, identificacion):
        for cliente in self.__clientes:
            if cliente.identificacion == identificacion:
                return cliente

        raise ClienteNoEncontradoError(
            f"No se encontro el cliente con identificacion {identificacion}."
        )

    def buscar_servicio(self, identificacion):
        for servicio in self.__servicios:
            if servicio.identificacion == identificacion:
                return servicio

        raise ServicioNoEncontradoError(
            f"No se encontro el servicio con identificacion {identificacion}."
        )

    def crear_reserva(self, identificacion, id_cliente, id_servicio, duracion):
        for reserva in self.__reservas:
            if reserva.identificacion == identificacion:
                raise DatosInvalidosError("Ya existe una reserva con esa identificacion.")

        cliente = self.buscar_cliente(id_cliente)
        servicio = self.buscar_servicio(id_servicio)

        nueva_reserva = Reserva(
            identificacion,
            cliente,
            servicio,
            duracion
        )

        self.__reservas.append(nueva_reserva)
        registrar_evento(f"Se creo la reserva {identificacion}.")
        return nueva_reserva

    def listar_clientes(self):
        return list(self.__clientes)

    def listar_servicios(self):
        return list(self.__servicios)

    def listar_reservas(self):
        return list(self.__reservas)
