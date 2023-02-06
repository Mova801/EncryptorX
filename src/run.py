"""
Simple module provided by Mova801.
Run an MVC based application.
Graphical User Interface provided by http://github.com/Mova801
"""
from view.view import DPGGUI
from model.model import Model
from controller.controller import Controller


def main() -> None:
    """Create and run a new application."""
    gui = DPGGUI(win_size=(900, 547))
    app = Controller(model=Model(), view=gui)
    app.start()


if __name__ == '__main__':
    main()
