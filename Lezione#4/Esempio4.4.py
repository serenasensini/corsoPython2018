class Square(Polygon):

    def __init__(self):
        Polygon.__init__(self, 4)
		
	def insertSidesValues(self):
        self.side = float(input("Insert a side value: "))
	
	 def getArea(self):
        area = self.side*4
        print('The area is equal to %0.2f' %area)
