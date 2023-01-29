from abc import ABC, abstractmethod


class AbstractView(ABC):

    @abstractmethod
    def build(self, controller) -> None:
        ...

    @abstractmethod
    def run(self) -> None:
        ...

    @abstractmethod
    def update_output_textbox(self, text: str) -> None:
        ...

    @abstractmethod
    def set_id(self, new_id: int) -> None:
        ...

    @abstractmethod
    def stop(self) -> None:
        ...
