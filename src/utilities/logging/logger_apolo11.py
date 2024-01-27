import logging
import os
import sys
from datetime import datetime
from logging import handlers
import yaml
from typing import List

# from src.utilities.files import FileUtils as file


def get_logger(
    app_name: str,
    log_location: str = os.path.join("tmp", "logs"),
    logger_level: int = logging.DEBUG
):
    """Logger personalizado para uso de Apolo11

    Args:
        app_name (str): Nombre de la aplicación o flujo que está corriendo
        log_location (str, optional): Ruta donde quedaran guardados los los logs.
        Defaults to os.path.join("tmp","logs").
        log_format (str, optional): Formato de fecha y hora minutos y segundos.
        Defaults to "%Y%m%d%H%M%S".
        logger_level (int, optional): Nivel de captura y muestra de eventos de logs.
        Defaults to logging.DEBUG.

    Returns:
        _type_: _description_
    """
    constants_path: str = os.path.join(os.path.join("settings", "constants_properties.yaml"))
    # constants_dict: dict = yaml.load(file.read_file(constants_path).object,
    #                                  Loader=yaml.FullLoader)
    with open(constants_path) as file:
        constants_dict = yaml.safe_load(file.read())

    log_formats: List[str] = constants_dict['date_formats']
    number_constants: List[int] = constants_dict['number_constants']
    string_constants: List[str] = constants_dict['string_constants']

    log_save = os.path.join(
        log_location,
        (app_name or string_constants[1]) + "_{}.log".format(datetime.now().strftime(log_formats[1])))
    logger = None

    try:
        logger.setLevel(logger_level)
        logger = logging.getLogger(app_name or string_constants[2])
        format = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - [%(name)s] : %(message)s", log_formats[2])
        loginStreamHandler = logging.StreamHandler(sys.stdout)
        loginStreamHandler.setFormatter(format)
        logger.addHandler(loginStreamHandler)
        fileHandler = handlers.RotatingFileHandler(
            log_save, maxBytes=(number_constants[2]), backupCount=number_constants[1])
        fileHandler.setFormatter(format)
        logger.addHandler(fileHandler)
    except Exception:
        logger = None

    return logger