from abc import ABC, abstractmethod
from engine import engine
from battery import battery
from servicable import serviceable


class Car(engine, battery, serviceable, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
