from dataclasses import dataclass
from util import color


@dataclass
class Colors:
    """Class containing default colors value."""
    BLACK = color.Color("#000000")
    CYAN = color.Color("#1F6AA5")
    DARK_CYAN = color.Color("#124063")
    DARK_GOLD = color.Color("#99692A")
    DARK_GRAY = color.Color("#2A2D2E")
    DARK_GREEN = color.Color("#027F45")
    GOLD = color.Color("#FFB144")
    GRAY = color.Color("#EEEEEE")
    GREEN = color.Color("#48B553")
    LIGHT_CYAN = color.Color("#477BA3")
    LIGHT_RED = color.Color("#C9515D")
    RED = color.Color("#FF0000")
    WHITE = color.Color("#FFFFFF")


@dataclass
class GuiConstants:
    """Class containing default values for application Frame elements."""
    inner_padx: int = 8
    inner_pady: int = 10
    icon_path: str = "EXTRA\images"
    icon: str = "redbunnyproject.ico"
    appearance_mode: str = "dark"
    color_theme: str = "blue"


@dataclass
class ButtonConstants:
    """Class containing default values for application Button elements."""
    inner_pad: int = 10
    sticky: str = "nsew"


@dataclass
class LabelConstants:
    """Class containing default values for application Label elements."""
    inner_pad: int = 5
    sticky: str = "nsew"


@dataclass
class TextBoxConstants:
    """Class containing default values for application Textbox elements."""
    inner_pad: int = 10
    sticky: str = "nsew"
    default_input_text: str = "Insert text"
    default_output_text: str = "Your result will be displayed here"


@dataclass
class FontConstants:
    """Class containing default values for application Font elements."""
    font: str = "Roboto Medium"
    size_M: int = 14
    size_L: int = 18
    size_T: int = 24
