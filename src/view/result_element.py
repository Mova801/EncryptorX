import dearpygui.dearpygui as dpg
from src.view.view_constants import ResultConstants
import time


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
            self, font: dpg.font, text0: tuple[str, str], text1: tuple[str, str], btn_0: tuple[str, str],
            btn_1: tuple[str, str, str]
    ) -> None:
        """
        Set the content of the Result.
        Exit wait state.
        :param font: font used for the result elements.
        :param text0: tuple containing text_label and text_content for text0 element.
        :param text1: tuple containing text_label and text_content for text1 element.
        :param btn_0: main button tuple containing btn_label and btn_function for the btn_0 element.
        :param btn_1: main button tuple containing btn_tooltip_label, btn_function and btn_icon for the btn_1 and btn_2
        elements.
        """
        date: str = time.strftime("%Y-%m-%d %H:%M:%S")
        with dpg.group(parent=f"result{self.__id}", tag=f"result_child{self.__id}", horizontal=True):
            btn_0_id: int = dpg.add_button(
                label=btn_0[0], tag=f"result_save{self.__id}", callback=btn_0[1], width=80,
                height=80
            )
            dpg.bind_item_font(btn_0_id, font)
            with dpg.group():
                dpg.add_text(f"date: {date}", tag=f"date{self.__id}")
                with dpg.group(horizontal=True):
                    dpg.add_text(text0[0], tag=f"result_text00{self.__id}")
                    text0_id: int = dpg.add_input_text(
                        default_value=text0[1], tag=f"result_text01{self.__id}", multiline=True, readonly=True,
                        height=25
                    )
                    dpg.bind_item_font(text0_id, font)
                    dpg.add_image_button(
                        btn_1[2], tag=f"result_btn0{self.__id}", height=18, width=18,
                        callback=btn_1[1])
                    with dpg.tooltip(f"result_btn0{self.__id}"):
                        dpg.add_text(btn_1[0])
                with dpg.group(horizontal=True):
                    dpg.add_text(text1[0], tag=f"result_text10{self.__id}")
                    out_data_id: int = dpg.add_input_text(
                        default_value=text1[1], tag=f"result_text11{self.__id}", multiline=True, readonly=True,
                        height=25
                    )
                    dpg.bind_item_font(out_data_id, font)
                    dpg.add_image_button(btn_1[2], tag=f"result_btn1{self.__id}", height=18, width=18,
                                         callback=btn_1[1])
                    with dpg.tooltip(f'result_btn1{self.__id}'):
                        dpg.add_text(btn_1[0])

        dpg.delete_item(f"result_loading{self.__id}")
