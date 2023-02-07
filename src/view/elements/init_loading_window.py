from __future__ import annotations
import dearpygui.dearpygui as dpg
from pathlib import Path
import pyautogui

from view.view_constants import Colors


def _get_screen_center() -> tuple[int, int]:
    screen_w, screen_h = pyautogui.size()
    return screen_w // 2, screen_h // 2


class InitialLoading:

    def __init__(self, img_width: int, img_height: int, image: Path, pos: str = 'center') -> None:
        self.width: int = img_width
        self.height: int = img_height
        self.image_path: str = image
        self.pos: str = pos
        self.__id: str = 'loading_window'

        dpg.create_context()
        dpg.create_viewport(width=img_width, height=img_height)
        dpg.set_viewport_resizable(False)
        dpg.set_viewport_decorated(False)

        if pos == 'center':
            center_x, center_y = _get_screen_center()
            self.pos = center_x - self.width // 2, center_y - self.height // 2
        dpg.set_viewport_pos(self.pos)

        img_width, img_height, channels, data = dpg.load_image(str(self.image_path))

        with dpg.texture_registry():
            dpg.add_static_texture(width=img_width, height=img_height, default_value=data, tag="loading_image")

        # window content
        with dpg.window(tag=self.__id):
            img_pos: tuple[int, int] = dpg.get_viewport_width() // 2 - img_width // 2, dpg.get_viewport_height() // 8
            dpg.add_image('loading_image', pos=img_pos, border_color=[0, 0, 0, 0])
            dpg.add_loading_indicator(
                tag='init_load',
                style=0,
                color=Colors.AZZURE.rgb,
                secondary_color=Colors.MAGENTA.rgb,
                pos=(dpg.get_viewport_width() // 2 - 17, dpg.get_viewport_height() // 2 + 45)
            )

        # add theme
        with dpg.theme() as global_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (0, 0, 0), category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, 0)

        dpg.bind_item_theme(self.__id, global_theme)
        dpg.set_primary_window(self.__id, True)
        # dpg.set_viewport_always_top(True)

    def delete(self) -> None:
        dpg.delete_item(self.__id)
