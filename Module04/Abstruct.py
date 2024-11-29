from abc import ABC, abstractmethod


class Bangladesh(ABC):
    @abstractmethod
    def print10to20(self):
        pass

    @abstractmethod
    def printOto10(self):
        pass
    def print2Oto30(self):
        for i in range(11,20):
            print(i)




class Dhaka(Bangladesh):
    def print10to20(self):
        pass

    def printOto10(self):
        for i in range(11,20):
            print(i)

obj=Dhaka()
obj.printOto10()