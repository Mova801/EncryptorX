import importlib.util
import threading
import tkinter
import tkinter as tk
from typing import Callable
import customtkinter as ct
from types import ModuleType
from pathlib import Path

from resources import constants
from util.app_logger import logging_setup
from gui.gui_constants import Colors

control_logger = logging_setup(__name__)


def start_thread(target_function: Callable, *args) -> None:
    """
    Starts a new daemon thread.
    :param target_function: thread target function
    :param args: args to the target_function
    :return: None
    """
    control_logger.warning("function callback to 'start_thread'")
    th: threading = threading.Thread(target=target_function, daemon=True, args=args)
    control_logger.warning(f"started a new daemon thread {th.name} with target '{target_function}({args})")
    th.start()


def activate_button_when_text_is_present(
        textbox: ct.CTkTextbox, btn_to_activate: ct.CTkButton, check_time: int) -> None:
    """
    Every :param check_time: checks if :param textbox: has text in it, if so activate :param btn_to_activate:
    :param textbox: textbox to check
    :param btn_to_activate: button to activate
    :param check_time: time to wait between checks
    :return: None
    """
    btn_to_activate.after(check_time, activate_button_when_text_is_present, textbox, btn_to_activate, check_time)
    if textbox.get(0.0, tkinter.END) != "\n":
        btn_to_activate.configure(state=tk.NORMAL)
        btn_to_activate.configure(fg_color=Colors.CYAN.hex)
    else:
        btn_to_activate.configure(state=tk.DISABLED)
        btn_to_activate.configure(fg_color=Colors.LIGHT_CYAN.hex)


def elaborate_button_callback(textbox: ct.CTkTextbox) -> None:
    """
    Get the text of the textbox and elaborates it,
    :param textbox: textbox
    :return: None
    """

    def import_module(module_name: str) -> ModuleType:
        """
        Imports dynamically the given module.
        :param module_name: module to import
        :return: imported module
        """
        path: str = str(Path("resources").joinpath(f"{module_name}.py"))
        spec = importlib.util.spec_from_file_location(module_name, path)
        imported_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(imported_module)
        return imported_module

    def textbox_set_text(text: str) -> None:
        """
        Set the text of the textbox to the given :param text:
        :param text: text to insert
        :return: None
        """
        textbox.delete(0.0, tk.END)
        textbox.insert(0.0, text)

    control_logger.warning(f"function callback {elaborate_button_callback.__name__}")
    control_logger.warning(f"trying to import module {constants.MODULE_TO_IMPORT}")
    module: ModuleType = ...
    try:
        module = import_module(constants.MODULE_TO_IMPORT)
    except ImportError as e:
        print(e)
        control_logger.error(e)
        control_logger.warning("check 'resources' folder")
    control_logger.warning(f"{module.__name__} imported correctly")
    control_logger.warning(f"function callback to {module.main.__name__}")

    try:
        output_text: str = module.main(textbox.get(1.0, "end"))
    except NotImplementedError as e:
        control_logger.error(e)
        output_text = "ERROR"

    required_type = str
    if isinstance(output_text, str):
        textbox_set_text(output_text)
    else:
        control_logger.error(
            f"{module.main.__name__} from {module.__name__} returned '{output_text}' of type {type(output_text)} not {required_type}. Computation result will be ignored")
