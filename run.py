"""
Created by Marco Vita (aka Mova801) on 23/01/2023
Graphical User Interface provided by http://github.com/Mova801
"""
from gui import gui_class
from gui import gui_exceptions
from gui.gui_constants import GuiConstants


def main() -> None:
    """Creates and runs a new window."""
    try:
        app = gui_class.Gui(title="MovaApp_v0.0.1", win_size=(800, 600), icon=GuiConstants.icon)
    except gui_exceptions.GuiInvalidWindowSizeError:
        exit(-1)
    else:
        app.build()
        app.run()


if __name__ == '__main__':
    main()
