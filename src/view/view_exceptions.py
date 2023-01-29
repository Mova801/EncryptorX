from typing import Any


class GuiException(Exception):
    def __init__(self, msg: str = "Gui Exception.", value: Any = None) -> None:
        super().__init__()
        self.msg = msg
        self.value = value

    def __str__(self) -> None:
        return f"{self.msg}:{self.value}"


class GuiInvalidWindowSizeError(GuiException):
    """Gui invalid window size error."""

    def __init__(self, msg: str = f"Invalid GUI window geometry size", value: Any = None) -> None:
        super().__init__(msg, value)
