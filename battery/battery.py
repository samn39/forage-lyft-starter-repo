from abc import ABC, abstractmethod

class batter(ABC):
    @abstractmethod
    def needs_service(self):
        pass