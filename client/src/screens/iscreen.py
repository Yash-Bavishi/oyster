from abc import ABC, abstractmethod


class IScreen(ABC):
    """
    type - interface
    description - each game screen inherits this interface

    """
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def start(self):
        pass
