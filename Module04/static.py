class myClass:
    x=10
    y=20

    @staticmethod
    def addTow():
        z=myClass.x+myClass.y
        print(z)

myClass.addTow()

obj=myClass()
obj.addTow()

print("x variable", myClass.x)