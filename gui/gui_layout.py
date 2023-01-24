import tkinter
import customtkinter as ct

from controller import controller
from gui.gui_constants import GuiConstants, ButtonConstants, LabelConstants, TextBoxConstants, FontConstants


def build_layout(gui) -> None:
    button_text: str = "COMPUTE"

    # set gui grid
    gui.grid_columnconfigure(0, weight=1)  # 1 column
    gui.grid_rowconfigure(0, weight=1)  # 1 row

    # ============ outer gui ============
    # gui.gui = ct.CTkFrame(
    #     master=gui, width=gui.size()[0],
    #     corner_radius=10)
    # gui.gui.grid(
    #     row=0, column=0,
    #     padx=GuiConstants.outer_pad, pady=GuiConstants.outer_pad,
    #     sticky=GuiConstants.sticky)
    # 
    # gui: ct.CTkFrame = gui.gui

    # set gui grid
    gui.grid_columnconfigure(0, weight=1)  # 1 column
    [gui.grid_rowconfigure(i, weight=0) for i in range(6)]  # 5 rows (id: 0 -> 4)

    # ============ title label for input ============
    gui.input_label = ct.CTkLabel(
        master=gui,
        text="Input",
        font=(FontConstants.font, FontConstants.size_T)
    )
    gui.input_label.grid(
        row=gui.id(), column=0,
        padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
        sticky=LabelConstants.sticky)

    # ============ text for input ============
    gui.input_textbox = ct.CTkTextbox(
        master=gui,
        font=(FontConstants.font, FontConstants.size_M),
    )
    gui.input_textbox.grid(
        row=gui.id(), column=0,
        padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
        sticky=TextBoxConstants.sticky)
    # gui.input_textbox.insert("0.0", TextBoxConstants.default_input_text)

    # ============ elaborate button ============
    gui.input_button = ct.CTkButton(
        master=gui,
        text=button_text,
        font=(FontConstants.font, FontConstants.size_L, 'bold'),
        # state=tkinter.DISABLED,
        command=lambda: controller.start_thread(
            controller.elaborate_button_callback,
            gui.output_textbox
            # command=lambda: controller.elaborate_button_callback(gui.output_textbox)
        ))

    gui.input_button.grid(
        row=gui.id(), column=0,
        padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
        sticky=ButtonConstants.sticky)

    # ============ title label for output ============
    gui.output_label = ct.CTkLabel(
        master=gui,
        text="Output",
        font=(FontConstants.font, FontConstants.size_T)
    )
    gui.output_label.grid(
        row=gui.id(), column=0,
        padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
        sticky=LabelConstants.sticky)

    # ============ text for output ============ì
    gui.output_textbox = ct.CTkTextbox(
        master=gui,
        font=(FontConstants.font, FontConstants.size_M),
    )
    gui.output_textbox.grid(
        row=gui.id(), column=0,
        padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
        sticky=TextBoxConstants.sticky)
    gui.output_textbox.insert("0.0", TextBoxConstants.default_output_text)

    controller.activate_button_when_text_is_present(
        gui.input_textbox,
        gui.input_button,
        gui.update_time_ms)
