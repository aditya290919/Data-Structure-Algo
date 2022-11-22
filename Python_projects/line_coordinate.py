class Line():

	def __init__(self,cord1,cord2):

		self.cord1 = cord1
		self.cord2 = cord2

	def distance(self):

		x1,y1 = self.cord1
		x2,y2 = self.cord2

		return ((x2-x1)**2+(y2-y1)**2)**0.5


	def slope(self):
		x1,y1 = self.cord1
		x2,y2 = self.cord2

		return (y2-y1)/(x2-x1)




c1 = (2,3)
c2 = (8,10)

l1 = Line(c1,c2)

l1.distance()
l1.slope()