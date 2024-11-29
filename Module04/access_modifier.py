class Car:
    BRAND ="Toyoal"
    _COLOR="White"
    __SPREED=100

    def display(self):
        print(f"Our Brand Name is {self.BRAND}")
        print(f"Our SPREED Name is {self.__SPREED}")

    def amount(self):
        pass

class SubCar(Car):
    def dispayFormChild(self):
        print(f"Our Brand Name is {self.BRAND}")
        #print(f"Our Spreed is {self.__SPREED}")


obj=SubCar()

print(obj.BRAND)
print(obj._COLOR)

obj.dispayFormChild()
print(obj.__SPREED)