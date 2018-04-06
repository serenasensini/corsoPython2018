class Polygon:
    
    def __init__(self, numberSides):
        self.n = numberSides
        self.sides = [0 for i in range(numberSides)]

    def insertSidesValues(self):
        self.sides = [float(input("Insert a side value " + str(i + 1) + " : ")) for i in range(self.n)]

    def corrSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])

class Square(Polygon):

    def __init__(self):
        Polygon.__init__(self, 4)
        
    def insertSidesValues(self):
        self.side = float(input("Insert a side value: "))
    
    def getArea(self):
       area = self.side*4
       print('The area is equal to %0.2f' %area)

class Triangle(Polygon):

    def __init__(self):
        Polygon.__init__(self, 3)

    def getArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area is equal to %0.2f' %area)


t = Triangle()

print isinstance(t,Triangle)
True
print isinstance(t,Polygon)
True
print isinstance(t,Square)
False
