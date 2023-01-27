import customtkinter as ct
from pathlib import Path

from gui import gui_layout
from gui.gui_constants import GuiConstants
from gui import gui_exceptions
from logger.logger import basic_init_log, basic_log


@basic_init_log
class Gui(ct.CTk):
    """
    Graphical User Interface class used to display the graphical interface
    In order to use a new window you must ensure to:
        - instantiate a new window
        - run the window
    """

    def __init__(self, title: str, win_size: tuple[int, int], icon: str = "") -> None:
        super().__init__()
        # window
        self.title(title)
        try:
            self.geometry(f"{win_size[0]}x{win_size[1]}")
        except ValueError:
            raise gui_exceptions.GuiInvalidWindowSizeError(win_size)

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.close)  # call self.close() when window gets closed

        if icon != "":  # FIXME: not supported in recent lib update, must wait
            self.iconbitmap(Path.cwd().joinpath(GuiConstants.icon_path).joinpath(icon))

        # setting window theme and appearance
        ct.set_appearance_mode(GuiConstants.appearance_mode)
        ct.set_default_color_theme(GuiConstants.color_theme)

        self.update_time_ms: int = 100
        self.id_counter: int = 0

    def id(self) -> int:
        """
        Returns a unique id for an element of the Gui layout.
        :return: ret_id
        """
        ret_id: int = self.id_counter
        self.id_counter += 1
        return ret_id

    @basic_log
    def build(self) -> None:
        """Builds the application layout."""
        gui_layout.build_layout(self)

    @basic_log
    def run(self) -> None:
        """Runs the application instance."""
        if self:
            self.mainloop()

    @basic_log
    def close(self) -> None:
        """Destroy the window when closed."""
        self.destroy()
