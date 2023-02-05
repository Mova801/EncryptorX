import PIL.Image
import customtkinter as ct
from pathlib import Path
import tkinter as tk

from src.logger.logger import basic_init_log, basic_log
from src.view.abc_view import AbstractView
from src.view import view_exceptions
from src.view.view_constants import GuiConstants, ButtonConstants, LabelConstants, TextBoxConstants, FontConstants
from src.controller import controller_constants


@basic_init_log
class Gui(ct.CTk, AbstractView):
    """
    Graphical User Interface class used to display the graphical interface
    In order to use a new window you must ensure to:
        - instantiate a new window
        - run the window
    """

    def __init__(self, title: str, win_size: tuple[int, int]) -> None:
        super().__init__()

        # elements
        self.__input_button = None
        self.__bug_button = None
        self.__input_label = None
        self.__output_label = None
        self.__input_textbox = None
        self.__output_textbox = None

        self.__id_counter: int = 0

        # window
        self.title(title)
        try:
            self.geometry(f"{win_size[0]}x{win_size[1]}")
        except ValueError:
            raise view_exceptions.GuiInvalidWindowSizeError(value=win_size)

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.stop)  # call self.close() when window gets closed

        # FIXME: not supported in recent lib update, must wait
        self.iconbitmap(Path.cwd().joinpath(GuiConstants.icon_path).joinpath(GuiConstants.logo))

        # setting window theme and appearance
        ct.set_appearance_mode(GuiConstants.appearance_mode)
        ct.set_default_color_theme(GuiConstants.color_theme)

        self.update_time_ms: int = 100

    def __generate_id(self) -> int:
        """
        Generate a row id for an element.
        :return: a new id.
        """
        new_id: int = self.__id_counter
        self.__id_counter += 1
        return new_id

    def __set_id(self, element: ct.CTkBaseClass) -> None:
        """
        Set the received id as a row id for an element.
        :param element: element that needs a row id.
        :return: None.
        """
        new_id: int = self.__generate_id()
        element.grid(row=new_id)

    @basic_log
    def update_output_textbox(self, text: str) -> None:
        """
        Set the text of the textbox to the given :param text:
        :param text: text to insert.
        :return: None.
        """
        self.__output_textbox.delete(0.0, tk.END)
        self.__output_textbox.insert(0.0, text)

    def __activate_button_when_text_is_present(self, btn_to_activate: ct.CTkButton, check_time: int) -> None:
        """
        Every :param check_time: checks if the input textbox has text in it, if so activate :param btn_to_activate:
        :param btn_to_activate: button to activate.
        :param check_time: time to wait between checks.
        :return: None.
        """
        btn_to_activate.after(check_time, self.__activate_button_when_text_is_present, btn_to_activate, check_time)
        if self.__input_textbox.get(0.0, tk.END) != "\n":
            btn_to_activate.configure(state=tk.NORMAL)
            btn_to_activate.configure(fg_color=ButtonConstants.fg_color)
        else:
            btn_to_activate.configure(state=tk.DISABLED)
            btn_to_activate.configure(fg_color=ButtonConstants.disabled_fg_color)

    @basic_log
    def run(self) -> None:
        """Run the view mainloop."""
        self.mainloop()

    @basic_log
    def stop(self) -> None:
        """Destroy the window when closed."""
        self.destroy()

    @basic_log
    def build(self, controller) -> None:
        """
        Build the Gui layout.
        :param controller: controller that handles the data user interactions.
        :return: None.
        """
        input_label_text: str = "Input"
        output_label_text: str = "Output"
        input_button_text: str = "COMPUTE"
        bug_button_text: str = "Report Bug"

        # set view grid
        self.grid_columnconfigure(0, weight=1)  # 1 column
        self.grid_rowconfigure(0, weight=1)  # 1 row

        # set self grid
        self.grid_columnconfigure(0, weight=1)  # 1 column
        [self.grid_rowconfigure(i, weight=0) for i in range(8)]  # 5 rows (id: 0 -> 4)

        # ============ title label for input ============
        self.__input_label = ct.CTkLabel(
            master=self,
            text=input_label_text,
            corner_radius=LabelConstants.corner_rad,
            text_color=LabelConstants.text_color,
            fg_color=LabelConstants.fg_color,
            font=(FontConstants.font, FontConstants.size_T)
        )
        self.__input_label.grid(
            row=self.__set_id(self.__input_label), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky=LabelConstants.sticky)

        # ============ text for input ============
        self.__input_textbox = ct.CTkTextbox(
            master=self,
            height=TextBoxConstants.height,
            font=(FontConstants.font, FontConstants.size_M),
        )
        self.__input_textbox.grid(
            row=self.__set_id(self.__input_textbox), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky=TextBoxConstants.sticky)
        # self.input_textbox.insert("0.0", TextBoxConstants.default_input_text)

        # ============ elaborate button ============
        self.__input_button = ct.CTkButton(
            master=self,
            text=input_button_text,
            height=ButtonConstants.height,
            width=ButtonConstants.width,
            text_color=ButtonConstants.text_color,
            fg_color=ButtonConstants.fg_color,
            hover_color=ButtonConstants.hover_color,
            text_color_disabled=ButtonConstants.disabled_text_color,
            font=(FontConstants.font, FontConstants.size_L, 'bold'),
            command=lambda: controller.handle_elaborate_click(self.__output_textbox.get(0.0, tk.END))
        )
        self.__input_button.grid(
            row=self.__set_id(self.__input_button), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky='sn')

        # ============ title label for output ============
        self.__output_label = ct.CTkLabel(
            master=self,
            text=output_label_text,
            corner_radius=LabelConstants.corner_rad,
            text_color=LabelConstants.text_color,
            fg_color=LabelConstants.fg_color,
            font=(FontConstants.font, FontConstants.size_T)
        )
        self.__output_label.grid(
            row=self.__set_id(self.__output_label), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky=LabelConstants.sticky)

        # ============ text for output ============ì
        self.__output_textbox = ct.CTkTextbox(
            master=self,
            height=TextBoxConstants.height,
            font=(FontConstants.font, FontConstants.size_M),
        )
        self.__output_textbox.grid(
            row=self.__set_id(self.__output_textbox), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky=TextBoxConstants.sticky)
        self.__output_textbox.insert("0.0", TextBoxConstants.default_output_text)

        image = PIL.Image.open(Path.cwd().joinpath(GuiConstants.icon_path).joinpath(GuiConstants.bug_icon))

        # ============ bug_icon button ============
        self.__bug_button = ct.CTkButton(
            master=self,
            text=bug_button_text,
            height=ButtonConstants.height,
            text_color=ButtonConstants.text_color,
            fg_color=ButtonConstants.fg_color,
            hover_color=ButtonConstants.hover_color,
            font=(FontConstants.font, FontConstants.size_M),
            image=ct.CTkImage(dark_image=image, size=GuiConstants.icon_size),
            command=lambda: controller.handle_open_link_request(controller_constants.RequestType.BUG_REPORT)
        )
        self.__bug_button.grid(
            row=self.__set_id(self.__bug_button), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady)

        # UPDATE BUTTON STATE
        self.__activate_button_when_text_is_present(self.__input_button, self.update_time_ms)
