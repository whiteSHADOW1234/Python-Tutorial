#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation.

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod # abstract method (the class inherits from this class must have this method)
    def go(self):
        pass

    @abstractmethod # abstract method (the class inherits from this class must have this method)
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()