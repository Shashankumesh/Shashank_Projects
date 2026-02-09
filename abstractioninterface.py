from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Sleeping...")

# Interface-like abstract class
class Pet(ABC):
    @abstractmethod
    def play(self):
        pass