import os
import logging
import time
from pathlib import Path


# logger = logging.getLogger(__name__)

def check_folder_structure() -> None:
    Path.mkdir(Path.cwd().joinpath("log"), exist_ok=True)


check_folder_structure()


def logging_setup(caller_module: str) -> logging.Logger:
    caller_module = caller_module.split(".")[-1].strip("__")
    log_dir: str = f'{os.getcwd()}/log/{time.strftime("%m-%d-%Y_%H-%M-%S_")}app.log'
    formatting: str = f'%(asctime)s [%(name)s]:%(levelname)s\t- %(message)s'
    datefmt: str = '%d-%b-%y %H:%M:%S'
    logger = logging.getLogger(caller_module)

    # create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(log_dir)
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.WARNING)
    c_handler.set_name(f"{__name__}stream_handler")
    f_handler.set_name(f"{__name__}file_handler")

    # create formatters and add it to handlers
    c_format = logging.Formatter(formatting, datefmt=datefmt)
    f_format = logging.Formatter(formatting, datefmt=datefmt)
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    logger.setLevel(logging.WARNING)
    return logger
