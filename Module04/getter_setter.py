class Car:
    __BRAND ="Toyoal"
    _COLOR="White"
    __SPREED=100

    def display(self):
        pass

    @property
    def BRAND(self):
        return self.__BRAND


    @BRAND.setter
    def BRAND(self,value):
        self.__BRAND=value


obj=Car()
# set value
obj.BRAND="Mazda"
print(obj.BRAND)

