# En este archivo están los errores que vamos a utilizar en el sistema.

class ErrorSistema(Exception):
    """Es el error general del sistema Software FJ."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se utiliza cuandoo algun dato no cumple con las validaciones."""
    pass


class ClienteNoEncontradoError(ErrorSistema):
    """Se presenta cuando no existe el cliente que estamos buscando."""
    pass


class ServicioNoEncontradoError(ErrorSistema):
    """Se presenta cuando no existe el servicio solicitado."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se presenta cuando un servicio no se encuentra disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se utiliza cuando una operacion de reserva no esta permitido."""
    pass
