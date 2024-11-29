from wsgiref.simple_server import server_version

class GrandFather:
    p=10000
    m=50000
class Father(GrandFather):
    x=10
    y=20
    def sub(self):
        print(self.x-self.y)

    def mul(self):
        print(self.x*self.y)

    def property(self):
        self.p=(self.p)/2
        return self.p



class Mother:
    a=100
    b=200
    def add(self):
        print(self.a+self.b)

    def div(self):
        print(self.b/self.a)

class Son(Father,Mother):
    pass

print("Property From Father")
obj=Son()
print(obj.x)
print(obj.y)
obj.sub()
obj.mul()


print("Property From Mother")


print(obj.a)
print(obj.b)
obj.add()
obj.div()
print(obj.property())