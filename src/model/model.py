import importlib.util
import webbrowser
from pathlib import Path

from src.logger.logger import basic_init_log


@basic_init_log
class Model:
    """Model class that handles data for a controller class."""

    def __init__(self) -> None:
        pass

    def hyperlink(self, link: str) -> None:
        """
        Open a link.
        :param link: link to open.
        :return: None.
        """
        webbrowser.open(link)
