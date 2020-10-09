
# observer_pattern_01
from abc import ABCMeta, abstractmethod

class WaterHeater:

    def __init__(self):
        self._observers = []
        self._temperature =25
    def get_temperature(self):
        return self._temperature
    def set_temperature(self, temperature):
        self._temperature = temperature
        print("the current temperature:" + str(self._temperature) + " ")
        self.notifies()
    def add_observer(self, observer):
        try:
            self._observers.append(observer)
        except (KeyError, AttributeError):
            print("error")
    def notifies(self):
        for o in self._observers:
            o.update(self)

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, water_heater):
        pass
    
class WashingMode(Observer):
    def update(self, water_heater):
        if water_heater.get_temperature() >= 50 and water_heater.get_temperature() < 70:
            print("Hot water is ready for shower.")

class DrinkingMode(Observer):
    def update(self, water_heater):
        if water_heater.get_temperature() >= 100:
            print("Hot Water is ready for drinking")


heater = WaterHeater()
washing_obser = WashingMode()
drinking_obser = DrinkingMode()
heater.add_observer(washing_obser)
heater.add_observer(drinking_obser)
heater.set_temperature(40)
heater.set_temperature(60)
heater.set_temperature(100)
