"""class Profile:
    x=20
    y=10

    def addTwo(self):
        z=self.x+self.y
        print(z)

    @staticmethod
    def addTwoNum():
        z=Profile.x+Profile.y
        return z


obj1=Profile()
obj1.addTwo()
print(obj1.x)
print(obj1.y)
print(Profile.x)
print(Profile.y)
print(Profile.addTwoNum())"""
from Module_03.practics import calcu

"""
class Profile:
    x=20
    y=10

    # Constructor Funtion
    def __init__(self):
        z = self.x - self.y
        print(z)

    def addTwo(self):
        z=self.x+self.y
        print(z)

obj=Profile()
"""
# Inharitence
"""
class Father:
    x = 20
    y = 10

    # Constructor Funtion
    def __init__(self):
        z = self.x - self.y
        print(z)


    def addTwo(self):
        z = self.x + self.y
        print(z)
    @staticmethod
    def multiplyTwo():
        z=Father.x*Father.y
        print(z)




class Son(Father):
    pass
"""
"""son=Son()
son.multiplyTwo()
Son.multiplyTwo()
son.addTwo()"""

"""father=Father()
father.multiplyTwo()
Father.multiplyTwo()
father.addTwo()"""

# Method Overriding

"""
class Father:
    x = 20
    y = 10

    # Constructor Funtion
    def __init__(self):
        z = self.x - self.y
        print(z)


    def addTwo(self):
        z = self.x + self.y
        print(z)
    @staticmethod
    def multiplyTwo():
        z=Father.x*Father.y
        print(z)




class Son(Father):
    x=10
    y=5
    # method Overriding
    def addTwo(self):
        z=self.x+self.y
        print(z)
obj_son=Son()
obj_son.addTwo()"""

# Method Abstruction
"""
from abc import ABC, abstractmethod

class Father:
    x=10
    y=20

    @abstractmethod
    def addtwo(self):
        pass

class Son(Father):
    def addtwo(self):
        z = self.x + self.y
        print(z)

sonObj=Son()
sonObj.addtwo()"""

# Multiple inharitance
"""
class GrandFather:
    def addTwo(self):
        z=self.x+self.y
        print(z)


class Father(GrandFather):
    x=20
    y=10

    def addtwo(self):
        z=self.x+self.y
        print(z)


class Mother:
    def multi(self,n1,n2):
        print(n1*n2)

class Son(Father,Mother):
    pass

obj=Son()

obj.addtwo()
obj.multi(3,5)"""

# Multi Level inharitance
"""
class GrandFather:
    x=10
    y=20
    def addTwo(self):
        z=self.x+self.y
        print(z)

class Father(GrandFather):
    pass


class Son(Father):
    pass

objGrandSon=Son()
objGrandSon.addTwo()"""


# Access Modifier
"""
class Father:
    __x=10
    __y=20
    __amount=10000

    def addTwo(self):
        z=self.__x+self.__y
        print(z)

class Son:
    pass

obj=Father()
obj.addTwo()
#print(obj.__x)"""


# Method Over loading

class Father:
    x=10
    y=20
    amount=10000

    def addTwo(self,a,b,c=0):
        z=a+b+c
        print(z)
    def myNumbers(self,*args):
        print(*args)

obj=Father()
obj.addTwo(2,3,4)
obj.addTwo(10,12)
obj.myNumbers()
obj.myNumbers(2)
obj.myNumbers(2,3)
obj.myNumbers(3,5,8)