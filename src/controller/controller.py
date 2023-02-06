from __future__ import annotations

from pathlib import Path
from time import sleep

from src.controller import controller_constants
from src.controller.controller_threading import as_thread
from src.logger.logger import basic_log, basic_init_log
from src.model.model import Model
from src.view.abc_view import AbstractView
from src.view.view_constants import AppConstants


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
    def handle_save_file_request(self, file_name: str, current_path: str, data: str, mode: str | None = 'w') -> None:
        if not file_name.endswith(''):
            file_name += AppConstants.generated_file_extension
        file_path = Path(current_path)
        if file_path.is_dir():
            with open(file_path.joinpath(file_name), mode) as f:
                f.write(data)

    @basic_log
    # @as_thread
    def handle_encrypt_request(self, data: str, key: str) -> tuple[str, str]:
        """
        Encrypt data with key.
        :param data: data to encrypt.
        :param key: key used to encrypt data.
        :return: encrypted data and key.
        """
        sleep(1.5)
