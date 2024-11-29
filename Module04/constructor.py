class myClass:

    x=10
    y=20

    def __init__(self,a,b,z,xval):
        #print("Hello i constructor")
        sum=self.x+self.y+a+b
        #print(sum)
        self.z=z
        self.x=xval

    def add(self):
        print(self.x+self.y+self.z)


obj=myClass(20,40,10,5)
obj.add()
