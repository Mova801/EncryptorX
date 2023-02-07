"""
Module containing application layout constants.
"""
from dataclasses import dataclass
from pathlib import Path

from util import color


@dataclass
class Colors:
    """Class containing default colors value."""
    AZZURE = color.Color("#569EFF")
    BLACK = color.Color("#000000")
    CYAN = color.Color("#1F6AA5")
    DARK_CYAN = color.Color("#124063")
    DARK_GOLD = color.Color("#99692A")
    DARK_GRAY = color.Color("#2A2D2E")
    DARKER_GRAY = color.Color("#070707")
    DARK_GREEN = color.Color("#027F45")
    GOLD = color.Color("#FFB144")
    GRAY = color.Color("#EEEEEE")
    GREEN = color.Color("#48B553")
    LIGHT_CYAN = color.Color("#477BA3")
    LIGHT_RED = color.Color("#C9515D")
    MAGENTA = color.Color("#A100FF")
    RED = color.Color("#FF0000")
    SMOKE_WHITE = color.Color("#919191")
    WHITE = color.Color("#FFFFFF")


@dataclass
class AppConstants:
    """Class containing default values for application GUI elements."""
    app_name: str = 'EncryptorX'
    version: str = '0.0.3-alpha'
    generated_file_extension: str = '.encx'
    resizable: bool = False
    image_path = Path("assets/images")
    font_path = Path("assets/fonts")
    appearance_mode: str = "dark"
    color_theme: str = "blue"


class ResultConstants:
    """Class containing default values for application Result element."""
    height: int = 100


class ImageConstants:
    """"""
    copy = Path("copy16.png")
    logo = Path("ex_hq.ico")
    loading = Path("ex100.png")
    # size: tuple[int, int] = (25, 25)


@dataclass
class ButtonConstants:
    """Class containing default values for application Button elements."""
    inner_pad: int = 10
    width: int = 200
    height: int = 40
    text_color: str = Colors.CYAN.hex
    fg_color: str = Colors.WHITE.hex
    hover_color: str = Colors.GRAY.hex
    disabled_text_color: str = Colors.LIGHT_CYAN.hex
    disabled_fg_color: str = Colors.SMOKE_WHITE.hex
    sticky: str = "nsew"


@dataclass
class LabelConstants:
    """Class containing default values for application Label elements."""
    inner_pad: int = 5
    text_color: str = Colors.WHITE.hex
    fg_color: str = Colors.CYAN.hex
    corner_rad: int = 4
    sticky: str = "nsew"


@dataclass
class TextBoxConstants:
    """Class containing default values for application Textbox elements."""
    inner_pad: int = 10
    sticky: str = "nsew"
    default_input_text: str = "Insert text"
    default_output_text: str = "Your result will be displayed here"
    height: int = 160


@dataclass
class FontConstants:
    """Class containing default values for application Font elements."""
    ProggyCleanSZBP = Path("ProggyCleanSZBP.ttf")
    RobotoMedium = Path("Roboto-Medium.ttf")
    size_D: int = 13
    size_M: int = 15
    size_L: int = 18
