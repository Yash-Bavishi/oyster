from abc import ABC, abstractmethod


class IMap(ABC):
    """
    type - interface
    description - Each match will have a map to be rendered in the background 

    """
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def gravity(self):
        """
        Each map will have its own gravtiy
        """
        pass

