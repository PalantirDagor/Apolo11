import logging
import os
import sys
from datetime import datetime
from logging import handlers

def get_logger(
    app_name: str,
    log_location: str = os.path.join("tmp","logs"),
    log_format: str ="%Y%m%d%H%M%S",

    logger_level: int = logging.DEBUG
):
    """Logger personalizado para uso de Apolo11

    Args:
        app_name (str): Nombre de la aplicación o flujo que está corriendo
        log_location (str, optional): Ruta donde quedaran guardados los los logs. Defaults to os.path.join("tmp","logs").
        log_format (str, optional): Formato de fecha y hora minutos y segundos. Defaults to "%Y%m%d%H%M%S".
        logger_level (int, optional): Nivel de captura y muestra de eventos de logs. Defaults to logging.DEBUG.

    Returns:
        _type_: _description_
    """

    log_save = os.path.join(
        log_location,
        (app_name or "UnknowNameLog") + "_{}.log".format(datetime.now().strftime(log_format))
    )
    logger = None
    
    try:
        logger = logging.getLogger(app_name or "UnknowApp")
        logger.setLevel(logger_level)
        format = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - [%(name)s] : %(message)s", "%d/%m/%Y %H:%M:%S")
        loginStreamHandler = logging.StreamHandler(sys.stdout)
        loginStreamHandler.setFormatter(format)
        logger.addHandler(loginStreamHandler)
        fileHandler = handlers.RotatingFileHandler(
            log_save, maxBytes=(1048576 * 5), backupCount=7)
        fileHandler.setFormatter(format)
        logger.addHandler(fileHandler)
    except Exception as ex:
        logger = None
        
    return logger