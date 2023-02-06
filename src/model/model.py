"""
Module containing the application logic.
"""
from __future__ import annotations

import webbrowser
from pathlib import Path

from src.logger.logger import basic_init_log
from src.view.view_constants import AppConstants


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

    def store_data(self, file_name: str, current_path: str, data: str, mode: str | None = 'w'):
        """
        Store data into a file.
        :param file_name: file name.
        :param current_path: selected path (where to save the file).
        :param data: data to store.
        :param mode: file mode (write | append |...).
        :return: None.
        """
        if not file_name.endswith(AppConstants.generated_file_extension):
            file_name += AppConstants.generated_file_extension
        file_path = Path(current_path)
        if file_path.is_dir():
            with open(file_path.joinpath(file_name), mode) as f:
                f.write(data)
