# Software FJ - Sistema de gestión

## Descripción

Este proyecto es un sistema desarrollado en Python para practicar programacion orientada a objetos. Permite registrar clientes, guardar los servicios de la empresa y crear reservas.

Los servicios que se pueden gestionar son:

Reserva de salas.
Alquiler de equipos.
Asesorias especializadas.

La informacion se maneja con objetos y listas mientras el programa esta abierto. No se utiliza una base de datos.

## Organización

- `sistema/cliente.py`: contiene la clase `Cliente`.
- `sistema/entidad.py`: contiene la clase abstracta `Entidad`.
- `sistema/servicio.py`: contiene la clase abstracta `Servicio`.
- `sistema/servicios.py`: contiene los tres tipos de servicios.
- `sistema/reserva.py`: contiene la clase `Reserva`.
- `sistema/gestor.py`: administra las listas de clientes, servicios y reservas.
- `sistema/errores.py`: contiene las excepciones personalizadas.
- `sistema/registro.py`: guarda los eventos y errores.
- `main.py`: ejecuta las simulaciones del sistema.

## Requisitos

- Python 3.10 o una versión reciente.
- No se requieren instalar librerias externas.

## Como ejecutar:

Abre una terminal en la carpeta principal del proyecto y ejecuta:

`py main.py`

En otros sistemas tambien se puede utilizar:

`python main.py`

## Registros

Al ejecutar el programa se crea la carpeta "logs" si no existe. Alli se guarda el archivo "software_fj.log", que contiene los eventos y errores de las pruebas. 
Incluí el archivo `.log` como evidencia de las pruebas realizadas durante el desarrollo.

## Nota

En las simulaciones del archivo "main.py" se incluyen operaciones correctas y otras que se realizaron con datos incorrectos para así comprobar que este sistema controle los errores y pueda continuar.
