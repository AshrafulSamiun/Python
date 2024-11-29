from wsgiref.simple_server import server_version

class GrandFather:
    p=10000
    m=50000



class Father(GrandFather):
    x=10
    y=20

    def __init__(self):
        print("Father Constructor")

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
    def __init__(self):
        super().__init__()
        print("Son Constructor")


#father=Father()
son=Son()