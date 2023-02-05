from abc import ABC, abstractmethod


class AbstractView(ABC):

    @abstractmethod
    def build(self, controller) -> None:
        ...

    @abstractmethod
    def run(self) -> None:
        ...

    @abstractmethod
    def stop(self) -> None:
        ...
