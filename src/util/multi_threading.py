"""
Module implementing multi-threading features.
"""
import threading
from typing import Callable, Any
import functools

from src.logger.logger import basic_log


@basic_log
def start_thread(target_function: Callable, *args) -> None:
    """
    Start a new daemon thread.
    :param target_function: thread target function.
    :param args: args to the target_function.
    :return: None.
    """
    thread = threading.Thread(target=target_function, daemon=True, args=args)
    thread.start()


def as_thread(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Start a new daemon thread.
    :param func: function to thread.
    :return: None.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return start_thread(func, *args, **kwargs)

    return wrapper
