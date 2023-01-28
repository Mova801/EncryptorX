from logger.logger import basic_log, basic_init_log
from model.model import Model
from view.abc_view import AbstractView
from controller.controller_threading import as_thread
from resources import constants


@basic_init_log
class Controller:
    def __init__(self, model: Model, view: AbstractView) -> None:
        self.view: AbstractView = view
        self.model: Model = model

    @basic_log
    def run(self) -> None:
        """Run the application instance."""
        self.view.build(self)
        self.view.run()

    def close(self) -> None:
        """Stop the application."""
        self.view.stop()

    def handle_id_request(self, element) -> None:
        """
        Handle id request from the view.
        :param element: element which needs a new id.
        :return: None.
        """
        new_id: int = self.model.id()
        self.view.set_id(element, new_id)

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
            output_text = f"Unfilled elaboration function. " \
                          f"Define the main function body of the module to import: {constants.MODULE_TO_IMPORT}",
        finally:
            if isinstance(output_text, str):
                self.view.update_output_textbox(output_text)
