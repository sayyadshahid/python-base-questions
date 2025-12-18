# Abstraction means hiding complex details and showing only the essential features of an object or system

from abc import ABC, abstractmethod  #import abstraction

class Vehicle(ABC):  # Abstract class
    pass
    # @abstractmethod
    # def start_engine(self):  # Abstract method
    #     pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

# car = Vehicle()   Not allowed (can't create object of abstract class)
car = Car()
bike = Bike()

car.start_engine()   # Car engine started
bike.start_engine()  # Bike engine started
