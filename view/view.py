import customtkinter as ct
from pathlib import Path
import tkinter as tk

from logger.logger import basic_init_log, basic_log
from view.abc_view import AbstractView
from view import view_exceptions
from view.view_constants import GuiConstants, ButtonConstants, LabelConstants, TextBoxConstants, FontConstants, Colors


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
        self.__input_label = None
        self.output_label = None
        self.__input_textbox = None
        self.__output_textbox = None

        # window
        self.title(title)
        try:
            self.geometry(f"{win_size[0]}x{win_size[1]}")
        except ValueError:
            raise gui_exceptions.GuiInvalidWindowSizeError(win_size)

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.stop)  # call self.close() when window gets closed

        # FIXME: not supported in recent lib update, must wait
        self.iconbitmap(Path.cwd().joinpath(GuiConstants.icon_path).joinpath(GuiConstants.icon))

        # setting window theme and appearance
        ct.set_appearance_mode(GuiConstants.appearance_mode)
        ct.set_default_color_theme(GuiConstants.color_theme)

        self.update_time_ms: int = 100

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
            btn_to_activate.configure(fg_color=Colors.CYAN.hex)
        else:
            btn_to_activate.configure(state=tk.DISABLED)
            btn_to_activate.configure(fg_color=Colors.LIGHT_CYAN.hex)

    def set_id(self, element: ct.CTkTextbox, new_id: str) -> None:
        """Set the received id as an element-id."""
        element.grid(row=new_id)

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
        button_text: str = "COMPUTE"

        # set view grid
        self.grid_columnconfigure(0, weight=1)  # 1 column
        self.grid_rowconfigure(0, weight=1)  # 1 row

        # set self grid
        self.grid_columnconfigure(0, weight=1)  # 1 column
        [self.grid_rowconfigure(i, weight=0) for i in range(6)]  # 5 rows (id: 0 -> 4)

        # ============ title label for input ============
        self.__input_label = ct.CTkLabel(
            master=self,
            text=input_label_text,
            font=(FontConstants.font, FontConstants.size_T)
        )
        self.__input_label.grid(
            row=controller.handle_id_request(self.__input_label), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky=LabelConstants.sticky)

        # ============ text for input ============
        self.__input_textbox = ct.CTkTextbox(
            master=self,
            font=(FontConstants.font, FontConstants.size_M),
        )
        self.__input_textbox.grid(
            row=controller.handle_id_request(self.__input_textbox), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky=TextBoxConstants.sticky)
        # self.input_textbox.insert("0.0", TextBoxConstants.default_input_text)

        # ============ elaborate button ============
        self.__input_button = ct.CTkButton(
            master=self,
            text=button_text,
            font=(FontConstants.font, FontConstants.size_L, 'bold'),
            # state=tkinter.DISABLED,
            command=lambda: controller.handle_elaborate_click(self.__output_textbox.get(0.0, tk.END))
        )

        self.__input_button.grid(
            row=controller.handle_id_request(self.__input_button), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky=ButtonConstants.sticky)

        # ============ title label for output ============
        self.output_label = ct.CTkLabel(
            master=self,
            text=output_label_text,
            font=(FontConstants.font, FontConstants.size_T)
        )
        self.output_label.grid(
            row=controller.handle_id_request(self.output_label), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky=LabelConstants.sticky)

        # ============ text for output ============ì
        self.__output_textbox = ct.CTkTextbox(
            master=self,
            font=(FontConstants.font, FontConstants.size_M),
        )
        self.__output_textbox.grid(
            row=controller.handle_id_request(self.__output_textbox), column=0,
            padx=GuiConstants.inner_padx, pady=GuiConstants.inner_pady,
            sticky=TextBoxConstants.sticky)
        self.__output_textbox.insert("0.0", TextBoxConstants.default_output_text)

        # UPDATE BUTTON STATE
        self.__activate_button_when_text_is_present(self.__input_button, self.update_time_ms)
