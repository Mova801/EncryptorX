from enum import Enum, auto


class ViewStatus(Enum):
    INIT = auto()
    RUNNING = auto()
    STOPPED = auto()
