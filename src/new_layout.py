import dearpygui.dearpygui as dpg

from view.view_constants import Colors
from view.view_constants import FontConstants
from view.view_constants import GuiConstants
from view.view_constants import TextBoxConstants
import time

# dearpygui setup
dpg.create_context()
dpg.create_viewport(title='EncryptorX', width=900, height=550)
dpg.set_viewport_resizable(False)

# value registry
with dpg.value_registry():
    dpg.add_string_value(default_value="", tag="input_textbox_value")

# font registry
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("assets/fonts/ProggyCleanSZBP.ttf", FontConstants.size_M)
    medium_font = dpg.add_font("assets/fonts/ProggyCleanSZBP.ttf", FontConstants.size_M + 1)
    larger_font = dpg.add_font("assets/fonts/Roboto-Medium.ttf", FontConstants.size_M + 2)
    title_font = dpg.add_font("assets/fonts/Roboto-Medium.ttf", FontConstants.size_M + 3)
    large_font = dpg.add_font("assets/fonts/Roboto-Medium.ttf", FontConstants.size_L)

width, height, channels, data = dpg.load_image("assets/images/copy16.png")

with dpg.texture_registry():
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="copy_image")

encryption_number: int = 0


def _display_data(win_id: int) -> None:
    date: str = time.strftime("%Y-%m-%d %H:%M:%S")
    with dpg.group(parent=f"output_child{win_id}", horizontal=True):
        tag: str = f"btn_save{win_id}"
        btn_save_id: int = dpg.add_button(label="Save", tag=tag, callback=lambda: print("salva ora"),
                                          width=80, height=80)
        dpg.bind_item_font(btn_save_id, larger_font)
        with dpg.group():
            tag: str = f"date{win_id}"
            dpg.add_text(f"date: {date}", tag=tag)
            with dpg.group(horizontal=True):
                tag: str = f"keyText{win_id}"
                dpg.add_text("key: ", tag=tag)
                tag: str = f"output_text_key{win_id}"
                out_key_id: int = dpg.add_input_text(default_value="...", tag=tag,
                                                     multiline=True, readonly=True, height=25)
                dpg.bind_item_font(out_key_id, larger_font)
                tag: str = f"copyK{win_id}"
                dpg.add_image_button("copy_image", tag=tag, height=18, width=18,
                                     callback=lambda: print("copy key"))
                with dpg.tooltip(tag):
                    dpg.add_text("Copy key")
            with dpg.group(horizontal=True):
                tag: str = f"dataText{win_id}"
                dpg.add_text("data:", tag=tag)
                tag: str = f"output_text_data{win_id}"
                out_data_id: int = dpg.add_input_text(default_value="...",
                                                      tag=tag,
                                                      multiline=True, readonly=True, height=25)
                dpg.bind_item_font(out_data_id, larger_font)
                tag: str = f"copyD{win_id}"
                dpg.add_image_button("copy_image", tag=tag, height=18, width=18,
                                     callback=lambda: print("copy data"))
                with dpg.tooltip(tag):
                    dpg.add_text("Copy data")


def _show_new_encryption(parent: str) -> int:
    global encryption_number

    # output section
    tag: str = f"output_child{encryption_number}"
    with dpg.child_window(parent=parent, tag=tag, autosize_x=True, height=100):
        with dpg.group(horizontal=True):
            # loading indicator
            indicator_x: int = dpg.get_viewport_width() // 2 - 50
            indicator_y: int = 30
            tag = f"output_loading{encryption_number}"
            dpg.add_loading_indicator(tag=tag, pos=[indicator_x, indicator_y])
    win_id: int = encryption_number
    encryption_number += 1
    return win_id


def count(n: int) -> None:
    for i in range(n):
        print(i)


def process(parent: str) -> None:
    win_id: int = _show_new_encryption(parent)

    output_slot = dpg.get_item_children(parent, 1)
    output_slot.reverse()
    dpg.reorder_items(parent, 1, new_order=output_slot)

    count(109999)
    dpg.delete_item(f"output_loading{win_id}")
    _display_data(win_id)


def _clear_encryption_list(parent: str) -> None:
    global encryption_number
    dpg.delete_item(parent, children_only=True)
    encryption_number = 0

    # window content


with dpg.window(label="EncryptorX", tag="primary_window"):
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

        sga_id: int = dpg.add_text("EncryptorX", indent=dpg.get_viewport_width() // 2.2)
        dpg.bind_item_font(sga_id, title_font)
        dpg.add_text("v0.0.1-alpha", color=Colors.GOLD.rgb, indent=dpg.get_viewport_width() // 1.15)

    # input
    dpg.add_text("Enter text to process:", label="input_text")
    in_textbox_id: int = dpg.add_input_text(label="input_textbox", multiline=True,
                                            width=dpg.get_viewport_width(), height=dpg.get_viewport_height() // 3,
                                            source="input_textbox_value")
    dpg.bind_item_font(in_textbox_id, larger_font)

    # spacing
    dpg.add_spacer(height=1)

    # output window
    with dpg.child_window(tag="output_window", autosize_x=True, height=(dpg.get_viewport_height() // 3) + 35):
        pass

    # buttons
    with dpg.group(horizontal=True):
        # elaborate button
        btn_elaborate_id: int = dpg.add_button(
            label="Process", tag="process_btn", callback=lambda: process("output_window"))
        dpg.bind_item_font(btn_elaborate_id, larger_font)
        # clear button
        btn_clear_id: int = dpg.add_button(
            label="Clear All", tag="clear_btn", callback=lambda: _clear_encryption_list("output_window"))
        dpg.bind_item_font(btn_clear_id, larger_font)

# window settings
dpg.set_viewport_small_icon(GuiConstants.icon_path + '/ex_hq.ico')
dpg.set_primary_window("primary_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()

# run
# dpg.start_dearpygui()
while dpg.is_dearpygui_running():
    # enabled/disable process button if there is no text to process
    if dpg.get_value("input_textbox_value"):
        dpg.enable_item("process_btn")
    else:
        dpg.disable_item("process_btn")
    dpg.render_dearpygui_frame()
# stop
dpg.destroy_context()
