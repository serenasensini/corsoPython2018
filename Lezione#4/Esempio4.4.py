class Polygon:
    
    def __init__(self, numberSides):
        self.n = numberSides
        self.sides = [0 for i in range(numberSides)]

    def insertSidesValues(self):
        self.sides = [float(input("Insert a side value " + str(i + 1) + " : ")) for i in range(self.n)]

    def corrSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])
    
    def getArea(self):
        return self.sides * self.n

class Square(Polygon):

    def __init__(self):
        Polygon.__init__(self, 4)
		
    def insertSidesValues(self):
        self.side = float(input("Insert a side value: "))
        
    def getArea(self):
        area = self.side*4
        print('The area is equal to %0.2f' %area)
        
square = Square()
square.insertSidesValues()
square.getArea()