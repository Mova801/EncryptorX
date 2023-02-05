import importlib.util
import webbrowser
from types import ModuleType
from pathlib import Path

from src.logger.logger import basic_log, basic_init_log


@basic_init_log
class Model:
    """Model class that handles data for a controller class."""

    def __init__(self) -> None:
        pass

    @basic_log
    def hyperlink(self, link: str) -> None:
        """
        Open a link.
        :param link: link to open.
        :return: None.
        """
        webbrowser.open(link)

    @basic_log
    def import_module(self, module_name: str) -> ModuleType:
        """
        Import dynamically the given module.
        :param module_name: module to import.
        :return: imported module.
        """
        path: str = str(Path("resources").joinpath(f"{module_name}.py"))
        spec = importlib.util.spec_from_file_location(module_name, path)
        imported_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(imported_module)
        return imported_module
