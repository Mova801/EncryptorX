class GuiInvalidWindowSizeError(Exception):
    def __init__(self, win_size: tuple[int, int]) -> None:
        super(f"Gui window geometry size received invalid data: {win_size}")
