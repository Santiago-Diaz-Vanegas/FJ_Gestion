import logging
from pathlib import Path


# La carpeta y el archivo se crean automáticamente cuando se ejecuta el programa.
carpeta_proyecto = Path(__file__).resolve().parent.parent
carpeta_logs = carpeta_proyecto / "logs"
carpeta_logs.mkdir(exist_ok=True)

ruta_archivo = carpeta_logs / "software_fj.log"

registro = logging.getLogger("SoftwareFJ")
registro.setLevel(logging.INFO)
registro.propagate = False

# Se comprueba que no se agregue el mismo manejador más de una vez.
if not registro.handlers:
    archivo = logging.FileHandler(ruta_archivo, encoding="utf-8")
    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    archivo.setFormatter(formato)
    registro.addHandler(archivo)


def registrar_evento(mensaje):
    """Guarda una operación normal del sistema."""
    registro.info(mensaje)


def registrar_error(mensaje):
    """Guarda el mensaje y los detalles del error que se está tratando."""
    registro.exception(mensaje)
