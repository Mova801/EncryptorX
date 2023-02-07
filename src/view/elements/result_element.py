"""
Module containing a layout item 'ResultElement' (use dearpygui).
"""
import dearpygui.dearpygui as dpg
import time
from typing import Callable, Any

from view.view_constants import ResultConstants


class ResultElement:

    def __init__(self, parent: str, result_id: int) -> None:
        self.__id: int = result_id
        self.__parent: str = parent
        with dpg.child_window(parent=self.__parent, tag=f"result{self.__id}", autosize_x=True,
                              height=ResultConstants.height):
            with dpg.group(horizontal=True):
                # loading indicator
                indicator_x: int = dpg.get_viewport_width() // 2 - 50
                indicator_y: int = ResultConstants.height // 3
                dpg.add_loading_indicator(tag=f"result_loading{self.__id}", pos=[indicator_x, indicator_y])

    @property
    def id(self) -> int:
        """Return the object id."""
        return self.__id

    def set_content(
            self, font: dpg.font, text0: tuple[str, str], text1: tuple[str, str],
            main_button: tuple[str, Callable[..., Any]],
            secondary_button: tuple[str, Callable[..., Any], str]
    ) -> None:
        """
        Set the content of the Result.
        Exit wait state.
        :param font: font used for the result elements.
        :param text0: tuple containing text_label and text_content for text0 element.
        :param text1: tuple containing text_label and text_content for text1 element.
        :param main_button: main button tuple containing btn_label and btn_function for the btn_0 element.
        :param secondary_button: main button tuple containing btn_tooltip_label, btn_function and btn_icon for the btn_1 and btn_2
        elements.
        """
        text0_label: str = text0[0]
        text0_data: str = text0[1]
        text1_label: str = text1[0]
        text1_data: str = text1[1]
        main_btn_label: str = main_button[0]
        main_btn_callback: Callable[..., Any] = main_button[1]
        secondary_btn_label: str = secondary_button[0]
        secondary_btn_callback: Callable[..., Any] = secondary_button[1]
        secondary_btn_image: str = secondary_button[2]

        date: str = time.strftime("%Y-%m-%d %H:%M:%S")
        with dpg.group(parent=f"result{self.__id}", tag=f"result_child{self.__id}", horizontal=True):
            main_btn_id: int = dpg.add_button(
                label=main_button[0], tag=f"result_main_btn{self.__id}", callback=main_button[1], width=80,
                height=80
            )
            dpg.bind_item_font(main_btn_id, font)
            with dpg.group():
                dpg.add_text(f"date: {date}", tag=f"date{self.__id}")

                with dpg.group(horizontal=True):
                    dpg.add_text(text0_label, tag=f"result_text0_label{self.__id}")
                    text0_id: int = dpg.add_input_text(
                        default_value=text0_data, tag=f"result_text0_data{self.__id}", multiline=True, readonly=True,
                        height=25
                    )
                    dpg.bind_item_font(text0_id, font)
                    dpg.add_image_button(
                        secondary_btn_image, tag=f"result_btn1{self.__id}", height=18, width=18,
                        callback=lambda: secondary_btn_callback(text0_data))
                    with dpg.tooltip(f"result_btn1{self.__id}"):
                        dpg.add_text(secondary_btn_label)

                with dpg.group(horizontal=True):
                    dpg.add_text(text1_label, tag=f"result_text1_label{self.__id}")
                    out_data_id: int = dpg.add_input_text(
                        default_value=text1_data, tag=f"result_text1_data{self.__id}", multiline=True, readonly=True,
                        height=25
                    )
                    dpg.bind_item_font(out_data_id, font)
                    dpg.add_image_button(
                        secondary_btn_image, tag=f"result_btn2{self.__id}", height=18, width=18,
                        callback=lambda: secondary_btn_callback(text1_data))
                    with dpg.tooltip(f'result_btn2{self.__id}'):
                        dpg.add_text(secondary_btn_label)

        dpg.delete_item(f"result_loading{self.__id}")

    def delete(self) -> None:
        dpg.delete_item(self.__parent, children_only=True)
