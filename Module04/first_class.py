"""class my_class:
    value1=10

a_obj= my_class()
print(type(a_obj))"""
import time


# Class Variable vs Instant Variable

class Car:
    color="White"
    make="Toyota"
    model="Corolla"

    def __init__(self,a,b,c="White",d=2024):
        self.color=a
        self.make=b
        self.model=c
        self.year=d

    def __str__(self):
        return f'{self.color}-{self.make}-{self.model}-{self.year}'
    def start_engin(self,t=1):
        print("Car Starting...........")
        time.sleep(t)
        print("Car Started! Ready to Go!")

car1=Car("Subaru","forester","Bronze")
#car1.color="Blue"
car2=Car("Toyata","Prado","White")
car3=Car("Trak","Tata")
#print(car3)
#print(car2)
#print((car1.color, car1.make,car1.model))
print(car1.start_engin())
print(car2.start_engin(2))
print(car3.start_engin(4))