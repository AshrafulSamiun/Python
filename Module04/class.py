class myClass:
    x=10
    y=20
   # z=10

    def __init__(self,zvalue):
        self.z=zvalue
        print("This is First Class")

    def addTow(self,a,b):
        sum=self.x+self.y+a+b
        return sum

    def addNew(self):
        return self.addTow(5,6)


obd=myClass(15)
#print(obd.z)
#print(obd.addTow(30,10))
print(obd.addNew())