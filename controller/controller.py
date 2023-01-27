import importlib.util
import threading
import tkinter as tk
from typing import Callable
import customtkinter as ct
from types import ModuleType
from pathlib import Path

from resources import constants
from logger.logger import basic_log
from gui.gui_constants import Colors


@basic_log
def start_thread(target_function: Callable, *args) -> None:
    """
    Starts a new daemon thread.
    :param target_function: thread target function.
    :param args: args to the target_function.
    :return: None.
    """
    th: threading = threading.Thread(target=target_function, daemon=True, args=args)
    th.start()


def activate_button_when_text_is_present(
        textbox: ct.CTkTextbox, btn_to_activate: ct.CTkButton, check_time: int) -> None:
    """
    Every :param check_time: checks if :param textbox: has text in it, if so activate :param btn_to_activate:
    :param textbox: textbox to check.
    :param btn_to_activate: button to activate.
    :param check_time: time to wait between checks.
    :return: None.
    """
    btn_to_activate.after(check_time, activate_button_when_text_is_present, textbox, btn_to_activate, check_time)
    if textbox.get(0.0, tk.END) != "\n":
        btn_to_activate.configure(state=tk.NORMAL)
        btn_to_activate.configure(fg_color=Colors.CYAN.hex)
    else:
        btn_to_activate.configure(state=tk.DISABLED)
        btn_to_activate.configure(fg_color=Colors.LIGHT_CYAN.hex)


@basic_log
def elaborate_button_callback(textbox: ct.CTkTextbox) -> None:
    """
    Get the text of the textbox and elaborates it.
    :param textbox: textbox.
    :return: None.
    """

    @basic_log
    def import_module(module_name: str) -> ModuleType:
        """
        Imports dynamically the given module.
        :param module_name: module to import.
        :return: imported module.
        """
        path: str = str(Path("resources").joinpath(f"{module_name}.py"))
        spec = importlib.util.spec_from_file_location(module_name, path)
        imported_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(imported_module)
        return imported_module

    @basic_log
    def textbox_set_text(text: str) -> None:
        """
        Set the text of the textbox to the given :param text:
        :param text: text to insert.
        :return: None.
        """
        textbox.delete(0.0, tk.END)
        textbox.insert(0.0, text)

    module: ModuleType = ...
    try:
        module = import_module(constants.MODULE_TO_IMPORT)
    except ImportError:
        pass

    try:
        output_text: str = module.main(textbox.get(1.0, "end"))
    except NotImplementedError:
        output_text = "ERROR"

    if isinstance(output_text, str):
        textbox_set_text(output_text)
