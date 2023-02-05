from src.logger.logger import basic_log, basic_init_log
from src.model.model import Model
from src.view.abc_view import AbstractView
from src.controller import controller_constants
from src.controller.controller_threading import as_thread
from src.resources import constants


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

    def handle_open_link_request(self, request_type: str) -> None:
        """
        Handle a request to open a link.
        :param request_type: defines the type of the request. Different requests open different links.
        :return: None.
        """
        match request_type:
            case controller_constants.RequestType.BUG_REPORT:
                self.model.hyperlink(controller_constants.Link.github_app_issues)

    @basic_log
    @as_thread
    def handle_elaborate_click(self, text: str) -> None:
        """
        Elaborate :param text:
        :param text: passed text.
        :return: None.
        """
        output_text: str = ""
        try:
            module = self.model.import_module(constants.MODULE_TO_IMPORT)
            output_text: str = module.main(text)
        except ImportError:
            output_text = "ERROR"
        except NotImplementedError:
            output_text = f"Unfilled elaboration function." \
                          f" Define the main function body of the module to import: {constants.MODULE_TO_IMPORT}"
        finally:
            if isinstance(output_text, str):
                self.view.update_output_textbox(output_text)
