from abc import ABC, abstractmethod

class Strategy(ABC):
    @staticmethod
    @abstractmethod
    def insert(lst):
        pass
