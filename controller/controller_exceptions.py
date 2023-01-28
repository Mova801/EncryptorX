from typing import Any


class ControllerException(Exception):
    """Generic controller class exception."""

    def __init__(self, msg: str = "Controller Exception.", value: Any = None) -> None:
        super().__init__()
        self.msg = msg
        self.value = value

    def __str__(self) -> None:
        return f"{self.msg}: {self.value}"


class UnfilledElaborationFunctionError(ControllerException):
    """Unfilled elaboration function error."""

    def __init__(self,
                 msg: str = "Unfilled elaboration function. Define the main function body of the module to import:",
                 value: Any = None) -> None:
        super().__init__(msg, value)
