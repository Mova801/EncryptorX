from __future__ import annotations

from time import sleep
from typing import Callable, Any

from controller import controller_constants
from logger.logger import basic_log, basic_init_log
from model.model import Model
from util.multithreading import as_thread
from view.abc_view import AbstractView


@basic_init_log
class Controller:
    def __init__(self, model: Model, view: AbstractView) -> None:
        self.view: AbstractView = view
        self.model: Model = model

    @basic_log
    def start(self) -> None:
        """Run the application instance."""
        self.view.build(self)
        self.view.run()

    def close(self) -> None:
        """Stop the application."""
        self.view.stop()

    @basic_log
    def handle_hyperlink_request(self, request_type: str) -> None:
        """
        Handle a request to open a link.
        :param request_type: defines the type of the request. Different requests open different links.
        :return: None.
        """
        match request_type:
            case controller_constants.RequestType.BUG_REPORT:
                self.model.hyperlink(controller_constants.Link.github_app_issues)

    @basic_log
    def handle_store_data_request(self, file_name: str, current_path: str, data: list[str],
                                  mode: str | None = 'w') -> None:
        """
        Handle a request to save data into a file.
        :param file_name: file name.
        :param current_path: selected path (where to save the file).
        :param data: data to store.
        :param mode: file mode (write | append |...).
        :return: None.
        """
        self.model.store_data(file_name, current_path, data, mode)

    @basic_log
    def handle_copy_2_clipboard_request(self, data: str) -> None:
        """
        Handle a request to copy data to clipboard.
        :param data: data to copy.
        :return: None.
        """
        self.model.copy2clipboard(data)

    @basic_log
    # @as_thread
    def handle_encrypt_request(self, data: str, key: str) -> tuple[str, str]:
        """
        Handle a request to encrypt data with key.
        :param data: data to encrypt.
        :param key: key used to encrypt data.
        :return: encrypted data and key.
        """
        res: str = ""
        match key:
            case 'bin':
                used_func = bin
            case 'hex':
                used_func = hex
            case _:
                return None, key
        for char in data:
            res += used_func(ord(char))[2:] + ' '
        return res, key
