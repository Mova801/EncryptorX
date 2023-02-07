import dearpygui.dearpygui as dpg

# from view.elements.error_popup import InvalidKeyErrorPopup
#
# dpg.create_context()
# dpg.create_viewport(title='Custom Title', width=800, height=600)
# dpg.setup_dearpygui()
#
# popup = ErrorPopup('bin', (dpg.get_viewport_width() // 2, dpg.get_viewport_height() // 2))
#
# with dpg.window(label="Tutorial"):
#     dpg.add_button(label="Open Dialog", callback=popup.show)
#
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

import dearpygui.dearpygui as dpg

from view.elements.init_loading_window import InitialLoading
from view.view_constants import AppConstants
from view.view_constants import ImageConstants
import time

width = height = 200

# dearpygui setup
dpg.create_context()
dpg.create_viewport(title='EncryptorX', width=width, height=height, decorated=False)
dpg.set_viewport_resizable(False)

initLoading = InitialLoading(width, height, "assets/images/ex100.png")

# window settings
dpg.set_viewport_small_icon(AppConstants.image_path.joinpath(ImageConstants.logo))
dpg.setup_dearpygui()
dpg.show_viewport()

# run
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    if dpg.is_key_down(dpg.mvKey_A):
        dpg.delete_item('loading_window')
# stop
dpg.destroy_context()
