"""
Module containing the DPGGUI a gui using dearpygui.
"""
from __future__ import annotations
import dearpygui.dearpygui as dpg
import functools
import time
from typing import Callable, Any

from src.controller import controller_constants
from src.logger.logger import basic_init_log, basic_log
from src.view.abc_view import AbstractView
from src.view.elements.init_loading_window import InitialLoading
from src.view.view_constants import Colors
from src.view.view_constants import FontConstants
from src.view.view_constants import AppConstants
from src.view.view_constants import ImageConstants
from src.view.elements.result_element import ResultElement


def _prepare_data_to_elaborate(controller, *args) -> Any:
    """
    Receive data to elaborate and return the processed data.
    :param controller: controller used to access the functions.
    :param args: data to elaborate
    :return: processed data.
    """
    return controller.handle_encrypt_request(*args)


def _prepare_message(data0: Any, data1: Any) -> str:
    return f"""# {AppConstants.app_name}{AppConstants.version}

date: {time.strftime("%Y-%m-%d %H:%M:%S")}        
key: {data0}
data: {data1}

========================================================================================
"""


@basic_init_log
class DPGGUI(AbstractView):
    """
    Graphical User Interface class used to display the graphical interface
    In order to use a new window you must ensure to:
        - instantiate a new window
        - run the window
    """

    def __init__(self, win_size: tuple[int, int], title: str | None = "", is_loading: bool | None = False) -> None:
        if not title:
            title = AppConstants.app_name
        self.title = title

        # dearpygui setup
        dpg.create_context()
        dpg.create_viewport(title=title, width=win_size[0], height=win_size[1])
        dpg.set_viewport_resizable(AppConstants.resizable)

        self.win_size: tuple[int, int] = win_size
        if is_loading:
            self.__setup_loading()

        # value registry
        with dpg.value_registry():
            dpg.add_string_value(default_value="", tag="input_textbox_value")
            dpg.add_string_value(default_value="", tag="input_key_value")

        # font registry
        with dpg.font_registry():
            # first argument ids the path to the .ttf or .otf file
            self.__fonts: dict[str, int | str] = {
                'default': dpg.add_font(
                    AppConstants.font_path.joinpath(FontConstants.ProggyCleanSZBP), FontConstants.size_D),
                'medium': dpg.add_font(
                    AppConstants.font_path.joinpath(FontConstants.RobotoMedium), FontConstants.size_M),
                'large': dpg.add_font(
                    AppConstants.font_path.joinpath(FontConstants.RobotoMedium), FontConstants.size_L)
            }

        # texture registry
        with dpg.texture_registry():
            img = AppConstants.image_path.joinpath(ImageConstants.copy)
            width, height, channels, data = dpg.load_image(str(img))
            self.__images: dict[str, str] = {
                'copy': 'copy_image'
            }
            dpg.add_static_texture(width=width, height=height, default_value=data, tag=self.__images['copy'])

        # window
        dpg.set_viewport_small_icon(AppConstants.image_path.joinpath(ImageConstants.logo))
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.bind_font(self.__fonts['default'])

        # setting support variables
        self.__results_counter: int = 0
        self.__processing: bool = False
        self.__fd_generated: bool = False

    def __setup_loading(self) -> None:
        """"""
        # width = height = 200
        # self.init_loading = InitialLoading(width, height, AppConstants.image_path.joinpath(ImageConstants.loading))

    def __stop_loading(self) -> None:
        """"""
        # self.init_loading.delete()

    def __increment_result_counter(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Increment the result counter variable at the end of the function.
        """

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            value = func(self, *args, **kwargs)
            self.__results_counter += 1
            return value

        return wrapper

    def __processing(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Set the processing flag (PF) of the view before function
        execution and reset it when the function is terminated.
        When the PF is set some actions are limited (i.e. some user input).
        """

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            self.__processing = True
            value = func(self, *args, **kwargs)
            self.__processing = False
            return value

        return wrapper

    def __activate_button_when_text_is_present(self, element: list[str], button: str) -> None:
        """
        Enable the button when the element has a value.
        Disable the button when the element has no value.
        :param element: element to check.
        :param button: button to enable/disable.
        :return: None.
        """
        if self.__processing:
            dpg.disable_item(button)
            return
        for elem in element:
            if not dpg.get_value(elem):
                dpg.disable_item(button)
                return
        dpg.enable_item(button)

    @__increment_result_counter
    def __add_result(self, parent: str) -> ResultElement:
        """
        Create a new result in wait state.
        A result in wait state is waiting for content and present a loading indicator at its center.
        :param parent: where to attach the new result.
        :return: new result id.
        """
        return ResultElement(parent, self.__results_counter)

    @__processing
    @basic_log
    def __clear_results(self, parent: str) -> None:
        """
        Clear the parent item (removes any child).
        :param parent: target item.
        :return: None.
        """
        dpg.delete_item(parent, children_only=True)
        self.__results_counter = 0

    @__processing
    @basic_log
    def __prepare_result_element(self, controller, parent: str) -> None:
        """
        Prepare a new result to show data.
        :param controller: controller used to access functions.
        :param parent: target item.
        :return: None.
        """
        result: ResultElement = self.__add_result(parent)

        # put the new Result at the top of the list (shown first)
        output_slot = dpg.get_item_children(parent, 1)
        output_slot.sort()
        output_slot.reverse()
        dpg.reorder_items(parent, 1, new_order=output_slot)

        data = dpg.get_value("input_textbox_value")
        key = dpg.get_value("input_key_value")
        new_data, new_key = _prepare_data_to_elaborate(controller, data, key)
        data_to_save: str = _prepare_message(new_data, new_key)

        result.set_content(
            self.__fonts['medium'], text0=('key: ', new_key), text1=('data:', new_data),
            main_button=('Save', lambda: self.__open_file_dialog(controller, data_to_save, 'a')),
            secondary_button=('copy', controller.handle_copy_2_clipboard_request, self.__images['copy'])
        )

    @__processing
    @basic_log
    def __open_file_dialog(self, controller, data, mode: str | None = 'w') -> None:
        """
        Open a file dialog and then send a request to save a file at the path selected by the user.
        :param controller: controller used to access functions.
        :param data: data to store.
        :param mode: file mode.
        :return: None.
        """
        if not self.__fd_generated:
            self.__fd_generated = True
            # ========================================= FILE DIALOG =========================================
            with dpg.file_dialog(label="File Dialog",
                                 width=dpg.get_viewport_width() // 1.2,  # type: ignore
                                 height=dpg.get_viewport_height() // 1.5,  # type: ignore
                                 show=True, tag="filedialog", modal=True,
                                 callback=lambda _, output: controller.handle_store_data_request(
                                     file_name=output['file_name'], current_path=output['current_path'], data=data,
                                     mode=mode)):
                dpg.add_file_extension(
                    AppConstants.generated_file_extension + "{" + f".{AppConstants.generated_file_extension}" + "}"
                )  # color=(255, 0, 255, 255))

        dpg.show_item('filedialog')

    @basic_log
    def run(self) -> None:
        """Run the view mainloop."""
        while dpg.is_dearpygui_running():
            self.__activate_button_when_text_is_present(["input_textbox_value", "input_key_value"], "process_btn")

            dpg.render_dearpygui_frame()

    @basic_log
    def stop(self) -> None:
        """Destroy the window when closed."""
        dpg.destroy_context()

    @basic_log
    def build(self, controller) -> None:
        """
        Build the Gui layout.
        :param controller: controller that handles the data user interactions.
        :return: None.
        """
        self.__stop_loading()

        # ========================================= PRYMARY WINDOW =========================================
        with dpg.window(tag="primary_window"):
            # ========================================= Spacing =========================================
            dpg.add_spacer(height=5)

            # ========================================== Menu ==========================================
            with dpg.menu_bar():
                with dpg.menu(label="File"):
                    dpg.add_menu_item(label="Open file", callback=lambda: print("[WIP] text from file"))

                    # save button
                    dpg.add_menu_item(label="Save", callback=lambda: self.__open_file_dialog(controller, 'suca'))

                with dpg.menu(label="Settings"):
                    dpg.add_menu_item(label="Full screen", check=True,
                                      callback=lambda: dpg.toggle_viewport_fullscreen())

                with dpg.menu(label="Help"):
                    dpg.add_menu_item(
                        label="Report bug", callback=lambda: controller.handle_hyperlink_request(
                            controller_constants.RequestType.BUG_REPORT)
                    )

                sga_id: int = dpg.add_text("EncryptorX", indent=dpg.get_viewport_width() // 2.2)  # type: ignore
                dpg.bind_item_font(sga_id, self.__fonts['medium'])

            # ======================================== Input Text ==========================================
            dpg.add_text("Enter text to process:", tag="input_text")
            input_text_id: int = dpg.add_input_text(tag="input_textbox", multiline=True,
                                                    width=dpg.get_viewport_width(),
                                                    height=dpg.get_viewport_height() // 3.3,  # type: ignore
                                                    source="input_textbox_value")
            dpg.bind_item_font(input_text_id, self.__fonts['medium'])

            # ======================================== Input Key ========================================
            with dpg.group(horizontal=True):
                dpg.add_text("Key: ", tag="input_key")
                input_key_id: int = dpg.add_input_text(tag="input_text_key",
                                                       width=dpg.get_viewport_width(),
                                                       source="input_key_value")
                dpg.bind_item_font(input_key_id, self.__fonts['medium'])

            # ========================================= Spacing ==========================================
            dpg.add_spacer(height=1)

            # ======================================= Result Window =======================================
            with dpg.child_window(tag="result_window", autosize_x=True, height=(dpg.get_viewport_height() // 3) + 35):
                pass

            # ========================================= Buttons =========================================
            with dpg.group(horizontal=True):
                # elaborate button
                btn_elaborate_id: int = dpg.add_button(
                    label="Process", tag="process_btn",
                    callback=lambda: self.__prepare_result_element(controller, "result_window"))
                dpg.bind_item_font(btn_elaborate_id, self.__fonts['large'])
                # clear button
                btn_clear_id: int = dpg.add_button(
                    label="Clear All", tag="clear_btn", callback=lambda: self.__clear_results("result_window"))
                dpg.bind_item_font(btn_clear_id, self.__fonts['large'])
                dpg.add_text(
                    'v' + AppConstants.version, color=Colors.GOLD.rgb,
                    indent=dpg.get_viewport_width() // 1.15)

            # set primary window
            dpg.set_primary_window('primary_window', True)
