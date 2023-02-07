"""
Simple module provided by Mova801.
Run an MVC based application.
Graphical User Interface provided by http://github.com/Mova801
"""
from controller.controller import Controller
from model.model import Model
from view.view import DPGGUI


def main() -> None:
    """Create and run a new application."""
    gui = DPGGUI(win_size=(900, 560), is_loading=True)
    app = Controller(model=Model(), view=gui)
    app.start()


if __name__ == '__main__':
    main()
