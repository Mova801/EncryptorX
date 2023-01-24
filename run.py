"""
Created by Marco Vita (aka Mova801) on 23/01/2023
Graphical User Interface provided by http://github.com/Mova801
"""
from gui import gui_class
from gui import gui_exceptions
from gui.gui_constants import GuiConstants
from util import app_logger


def main() -> None:
    """Creates and runs a new window."""

    app: gui_class.Gui = ...
    try:
        main_logger.warning("initializing app")
        app = gui_class.Gui(title="MovaApp_v0.0.1", win_size=(800, 600), icon=GuiConstants.icon)
    except gui_exceptions.GuiInvalidWindowSizeError as e:
        main_logger.error(e)
        exit(-1)

    main_logger.warning("building app layout")
    app.build()
    main_logger.warning("running app")
    app.run()
    main_logger.warning("app closed")


if __name__ == '__main__':
    main_logger = app_logger.logging_setup(__name__)
    main()
