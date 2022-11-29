
#------------------------------------------------------------------
class Car:
    # create isnstructors (self do not need to be passed)
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self): # self is the object itself (here "self" must been called)
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
#------------------------------------------------------------------
# from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()# do not need to pass in "self" (self is the object itself)
car_2.stop()

#------------------------------------------------------------------
