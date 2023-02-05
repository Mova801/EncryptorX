import dearpygui.dearpygui as dpg

from view.view_constants import Colors
from view.view_constants import FontConstants
from view.view_constants import GuiConstants
from view.view_constants import TextBoxConstants

# dearpygui setup
dpg.create_context()
dpg.create_viewport(title='EncriptorX', width=900, height=550)
dpg.set_viewport_resizable(False)

# font registry
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("assets/fonts/ProggyCleanSZBP.ttf", FontConstants.size_M)
    medium_font = dpg.add_font("assets/fonts/ProggyCleanSZBP.ttf", FontConstants.size_M + 1)
    larger_font = dpg.add_font("assets/fonts/Roboto-Medium.ttf", FontConstants.size_M + 2)
    title_font = dpg.add_font("assets/fonts/Roboto-Medium.ttf", FontConstants.size_M + 3)
    large_font = dpg.add_font("assets/fonts/Roboto-Medium.ttf", FontConstants.size_L)

# window content
with dpg.window(label="EncriptorX", tag="PrimaryWindow"):
    dpg.bind_font(default_font)

    # spacing
    dpg.add_spacer(height=5)

    # header
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Open file", callback=lambda: print("text from file"))

            # file dialog
            with dpg.file_dialog(label="File Dialog", width=550, height=400, show=False,
                                 callback=lambda s, a, u: print(s, a, u), tag="filedialog"):
                dpg.add_file_extension(".*", color=(255, 255, 255, 255))
                dpg.add_file_extension(".txt{.txt}", color=(255, 0, 255, 255))

            # save button
            dpg.add_menu_item(label="Save", callback=lambda: dpg.show_item("filedialog"))

        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Full screen", check=True, callback=lambda: dpg.toggle_viewport_fullscreen())

        with dpg.menu(label="Help"):
            dpg.add_menu_item(label="Report bug", callback=lambda: print("Report bug"))

        sga_id: int = dpg.add_text("EncriptorX", indent=dpg.get_viewport_width() // 2.2)
        dpg.bind_item_font(sga_id, title_font)
        dpg.add_text("v0.0.1-alpha", color=Colors.GOLD.rgb, indent=dpg.get_viewport_width() // 1.15)

    # input
    dpg.add_text("Enter text to process", label="input")
    in_textbox_id: int = dpg.add_input_text(multiline=True, width=dpg.get_viewport_width(),
                                            height=dpg.get_viewport_height() // 3)
    dpg.bind_item_font(in_textbox_id, larger_font)

    # spacing
    dpg.add_spacer(height=1)

    # output
    with dpg.child_window(tag="output", autosize_x=True, height=(dpg.get_viewport_height() // 3) + 35):
        with dpg.child_window(autosize_x=True):
            with dpg.group(horizontal=True):
                win_width: int = (dpg.get_viewport_width() // 2) - 30
                win_height: int = dpg.get_viewport_height() // 7
                dpg.add_loading_indicator(
                    pos=[win_width, win_height], show=True)

                out_text_id: int = dpg.add_text(label="output_text", show=False)
                dpg.bind_item_font(out_text_id, larger_font)

    # elaborate button
    with dpg.group(horizontal=True):
        btn_elaborate_id: int = dpg.add_button(
            label="Process", enabled=False, callback=lambda: print("Processing"))
        dpg.bind_item_font(btn_elaborate_id, large_font)

    # spacing
    # dpg.add_spacer(height=2)
    # dpg.add_separator()
    #
    # # output
    # out_label_id: int = dpg.add_text("Output", label="output")
    # dpg.bind_item_font(out_label_id, large_font)
    # dpg.add_input_text(multiline=True, readonly=True,
    #                    default_value=TextBoxConstants.default_output_text,
    #                    width=dpg.get_viewport_width())

    # btn_bug_id: int = dpg.add_button(label="Save", callback=lambda: dpg.show_item("filedialog"))
    # dpg.bind_item_font(btn_bug_id, large_font)

    # spacing
    # dpg.add_spacer(height=2)
    # dpg.add_separator()

# window settings
dpg.set_viewport_small_icon(GuiConstants.icon_path + '/ex_logo2.ico')
dpg.set_primary_window("PrimaryWindow", True)
dpg.setup_dearpygui()
dpg.show_viewport()

# run
dpg.start_dearpygui()
# stop
dpg.destroy_context()
