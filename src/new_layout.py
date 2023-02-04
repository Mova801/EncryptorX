import dearpygui.dearpygui as dpg

from view.view_constants import Colors
from view.view_constants import FontConstants
from view.view_constants import GuiConstants

dpg.create_context()
dpg.create_viewport(title='MovaApp', width=640, height=480)
dpg.setup_dearpygui()


def check_input_textbox(textbox) -> None:
    if dpg.get_value(textbox) != "":
        pass


with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("assets/fonts/ProggyCleanSZBP.ttf", FontConstants.size_M)
    title_font = dpg.add_font("assets/fonts/Roboto-Bold.ttf", FontConstants.size_T)

with dpg.window(label="MovaApp", tag="PrimaryWindow"):
    center: tuple[int,]

    dpg.bind_font(default_font)

    input_id = dpg.add_text("Input", label="input_title", color=Colors.CYAN.rbg)
    dpg.bind_item_font(input_id, title_font)

    input_textbox_id = dpg.add_input_text(multiline=True, width=dpg.get_viewport_width(), label="input_textbox",
                                          default_value="Enter text...")

    elaborate_button_id = dpg.add_button(label="Elaborate", callback=lambda: print("Button pressed"))

    input_id = dpg.add_text("Output", label="output_title", color=Colors.CYAN.rbg)
    dpg.bind_item_font(input_id, title_font)

    dpg.add_input_text(multiline=True, width=dpg.get_viewport_width(), label="output_textbox",
                       default_value="Your results will be displayed here.", readonly=True)

dpg.set_viewport_small_icon(GuiConstants.icon_path + '/' + GuiConstants.logo)
dpg.show_viewport()
dpg.set_primary_window("PrimaryWindow", True)

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    check_input_textbox(input_textbox_id)
    dpg.render_dearpygui_frame()

dpg.destroy_context()
