from abc import ABC, abstractmethod

class BaseUtility(ABC):

    @abstractmethod
    def display(self):
        pass