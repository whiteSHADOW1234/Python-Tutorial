#---------------------------------------------------------------------
class Car:

    wheels = 4 # class variable

    def __init__(self,make,model,year,color):
        self.make = make    #instance variable
        self.model = model  #instance variable
        self.year = year    #instance variable
        self.color = color  #instance variable

#---------------------------------------------------------------------
# from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

#Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
#---------------------------------------------------------------------