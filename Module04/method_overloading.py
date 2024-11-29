class Father:
    x=10
    y=20

    def addTow(self):
        print(self.x+self.y)

    def mymethod(self,*a):
        print(a)

obj=Father()

print(obj.mymethod(1,2,3))