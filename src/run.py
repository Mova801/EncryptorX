"""
Simple module provided by Mova801.
Run an MVC based application.
Graphical User Interface provided by http://github.com/Mova801
"""
from view.view import Gui
from model.model import Model
from controller.controller import Controller


def main() -> None:
    """Create and run a new application."""
    gui = Gui(title="MovaApp_v0.0.2-alpha", win_size=(800, 600))
    app = Controller(model=Model(), view=gui)
    app.start()


if __name__ == '__main__':
    main()
