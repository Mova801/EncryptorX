import dearpygui.dearpygui as dpg

from view.view_constants import Colors


class InvalidKeyErrorPopup:
    def __init__(self, pos: tuple[int, int]) -> None:
        self.__id: str = "error_popup"
        with dpg.window(modal=True, show=False, tag="error_popup", no_title_bar=True, autosize=True):
            dpg.add_text("Invalid Key!", color=Colors.RED.rgb)
            with dpg.group(horizontal=True, horizontal_spacing=0):
                dpg.add_text("Valid keys are ")
                dpg.add_text("'bin'", color=Colors.GOLD.rgb)
                dpg.add_text(" and ")
                dpg.add_text("'hex'", color=Colors.GOLD.rgb)
                dpg.add_text("!")
            dpg.add_separator()
            dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("error_popup", show=False))
        self.pos: tuple[int, int] = (
            pos[0] + dpg.get_item_width('error_popup'),
            pos[1] - dpg.get_item_height('error_popup')
        )
        dpg.set_item_pos('error_popup', self.pos)

    def show(self) -> None:
        dpg.configure_item(self.__id, show=True)

    def delete(self) -> None:
        dpg.delete_item(self.__id)
