from sistema.gestor import GestorSistema
from sistema.cliente import Cliente
from sistema.servicios import ReservaSalas, AlquilerEquipos, Asesoria
from sistema.errores import ErrorSistema
from sistema.registro import registrar_evento, registrar_error


def ejecutar_operacion(numero, descripcion, funcion):
    """Ejecuta una prueba y evita que un error detenga las demas."""
    print("\n" + "-" * 60)
    print(f"OPERACION {numero}: {descripcion}")

    try:
        resultado = funcion()

    except ErrorSistema as error:
        registrar_error(f"Error controlado en la operacion {numero}: {error}")
        print("La operacion no se pudo completar:", error)

    except Exception as error:
        # En este bloque se captura errores no previstos para que podamos continuar.
        registrar_error(f"Error inesperado en la operacion {numero}: {error}")
        print("Se presento un error inesperado:", error)

    else:
        if resultado is not None:
            print(resultado)
        registrar_evento(f"La operacion {numero} termino correctamente.")

    finally:
        # Se ejecuta incluso cuando la operacion genera una excepcion.
        registrar_evento(f"Finalizo la operacion {numero}.")


def registrar_primer_cliente(gestor, datos):
    cliente = Cliente(
        "C001",
        "Laura Martinez",
        "laura@gmail.com",
        "3001234567"
    )
    gestor.registrar_cliente(cliente)
    datos["cliente"] = cliente
    return "Se registró a Laura Martinez."


def intentar_cliente_invalido(gestor, datos):
    cliente = Cliente(
        "C002",
        "Andres Gomez",
        "correo_incorrecto",
        "3101234567"
    )
    gestor.registrar_cliente(cliente)
    return "Cliente registrado."


def intentar_cliente_repetido(gestor, datos):
    cliente = Cliente(
        "C001",
        "Laura Gomez",
        "laura2@gmail.com",
        "3111234567"
    )
    gestor.registrar_cliente(cliente)
    return "Cliente registrado."


def registrar_sala(gestor, datos):
    sala = ReservaSalas("S001", "Sala de reuniones", 50000, 15)
    gestor.registrar_servicio(sala)
    datos["sala"] = sala
    return "Se registró la sala de reuniones."


def registrar_equipos(gestor, datos):
    equipos = AlquilerEquipos("S002", "Alquiler de computadores", 15000, 3)
    gestor.registrar_servicio(equipos)
    datos["equipos"] = equipos
    return "Se registro el alquiler de computadores."


def registrar_asesoria(gestor, datos):
    asesoria = Asesoria(
        "S003",
        "Asesoría de software",
        80000,
        "Desarrollo de software"
    )
    gestor.registrar_servicio(asesoria)
    datos["asesoria"] = asesoria
    return "Se registro el servicio de asesoria."


def intentar_servicio_invalido(gestor, datos):
    servicio = ReservaSalas("S004", "Sala no valida", -5000, 10)
    gestor.registrar_servicio(servicio)
    return "Servicio registrado."


def crear_reserva_exitosa(gestor, datos):
    reserva = gestor.crear_reserva("R001", "C001", "S001", 2)
    reserva.confirmar()
    total = reserva.procesar(impuesto=19, descuento=10)
    datos["reserva_procesada"] = reserva
    return f"Reserva procesada. Total a pagar: ${total:,.2f}"


def intentar_servicio_no_disponible(gestor, datos):
    servicio = gestor.buscar_servicio("S003")
    servicio.disponible = False
    reserva = None

    try:
        reserva = gestor.crear_reserva("R002", "C001", "S003", 1)
        return reserva.confirmar()

    finally:
        # Se libera el servicio para que las siguientes pruebas puedan usarlo.
        if reserva is not None and reserva.estado == "Pendiente":
            reserva.cancelar()

        servicio.disponible = True
        registrar_evento("Se restablecio la disponibilidad del servicio S003.")


def intentar_duracion_incorrecta(gestor, datos):
    gestor.crear_reserva("R003", "C001", "S002", 0)
    return "Reserva creada."


def intentar_cliente_que_no_existe(gestor, datos):
    gestor.crear_reserva("R004", "C999", "S002", 2)
    return "Reserva creada."


def crear_y_cancelar_reserva(gestor, datos):
    reserva = gestor.crear_reserva("R005", "C001", "S002", 2)
    reserva.confirmar()
    datos["reserva_cancelada"] = reserva
    return reserva.cancelar()


def intentar_cancelar_reserva_procesada(gestor, datos):
    reserva = datos["reserva_procesada"]
    return reserva.cancelar()


def probar_encadenamiento(gestor, datos):
    reserva = gestor.crear_reserva("R006", "C001", "S003", 1)
    reserva.confirmar()

    try:
        # El impuesto no es valido. Reserva lo convierte en un error de reserva,
        # pero este conserva el error original como causa.
        return reserva.procesar(impuesto=150)

    finally:
        if reserva.estado == "Confirmada":
            reserva.cancelar()


def calcular_costo_con_opciones(gestor, datos):
    sala = gestor.buscar_servicio("S001")
    total = sala.calcular_costo(2, impuesto=19, descuento=10)
    return f"Costo de dos horas de sala con impuesto y descuento: ${total:,.2f}"


def mostrar_resumen(gestor):
    print("\n" + "=" * 60)
    print("RESUMEN DEL SISTEMA SOFTWARE FJ")
    print("=" * 60)

    print("\nCLIENTES:")
    for cliente in gestor.listar_clientes():
        print(f"- {cliente.identificacion}: {cliente.nombre}")

    print("\nSERVICIOS:")
    for servicio in gestor.listar_servicios():
        estado = "Disponible" if servicio.disponible else "No disponible"
        print(f"- {servicio.identificacion}: {servicio.nombre} ({estado})")

    print("\nRESERVAS:")
    for reserva in gestor.listar_reservas():
        print(f"- {reserva.identificacion}: {reserva.estado}")

    print("\nEl sistema termino las pruebas. Revisa logs/software_fj.log para ver los registros.")
    registrar_evento("Termino la ejecucion de las simulaciones.")


def main():
    gestor = GestorSistema()
    datos = {}

    print("=" * 60)
    print("SISTEMA DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS")
    print("SOFTWARE FJ")
    print("=" * 60)

    ejecutar_operacion(1, "Registrar un cliente valido", lambda: registrar_primer_cliente(gestor, datos))
    ejecutar_operacion(2, "Intentar registrar un cliente con correo incorrecto", lambda: intentar_cliente_invalido(gestor, datos))
    ejecutar_operacion(3, "Intentar registrar una identificación repetida", lambda: intentar_cliente_repetido(gestor, datos))
    ejecutar_operacion(4, "Registrar un servicio de reserva de salas", lambda: registrar_sala(gestor, datos))
    ejecutar_operacion(5, "Registrar un servicio de alquiler de equipos", lambda: registrar_equipos(gestor, datos))
    ejecutar_operacion(6, "Registrar un servicio de asesoria", lambda: registrar_asesoria(gestor, datos))
    ejecutar_operacion(7, "Intentar crear un servicio con tarifa negativa", lambda: intentar_servicio_invalido(gestor, datos))
    ejecutar_operacion(8, "Crear, confirmar y procesar una reserva", lambda: crear_reserva_exitosa(gestor, datos))
    ejecutar_operacion(9, "Intentar confirmar una reserva con servicio no disponible", lambda: intentar_servicio_no_disponible(gestor, datos))
    ejecutar_operacion(10, "Intentar crear una reserva con duración invalida", lambda: intentar_duracion_incorrecta(gestor, datos))
    ejecutar_operacion(11, "Intentar reservar con un cliente que no existe", lambda: intentar_cliente_que_no_existe(gestor, datos))
    ejecutar_operacion(12, "Crear y cancelar una reserva correctamente", lambda: crear_y_cancelar_reserva(gestor, datos))
    ejecutar_operacion(13, "Intentar cancelar una reserva que ya fue procesada", lambda: intentar_cancelar_reserva_procesada(gestor, datos))
    ejecutar_operacion(14, "Comprobar el encadenamiento de excepciones", lambda: probar_encadenamiento(gestor, datos))
    ejecutar_operacion(15, "Calcular un costo con impuesto y descuento", lambda: calcular_costo_con_opciones(gestor, datos))

    mostrar_resumen(gestor)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        # Esta es una ultima protección por si ocurre un error fuera de las pruebas.
        registrar_error(f"Error general al ejecutar el programa: {error}")
        print("Ocurrio un problema general. El detalle quedo guardado en el archivo de logs.")
