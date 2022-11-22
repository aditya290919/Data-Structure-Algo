class Cylinder():

	pi = 3.14

	def __init__(self,rad,height):

		self.rad = rad
		self.height = height

	def volume(self):

		return self.pi * self.rad * self.rad * self.height

	def surface_area(self):

		self.rad = rad
		self.height = height

		return 2* self.pi * self.rad * self.height + 2 * pi * self.rad * self.rad

cylinder1 = Cylinder(3,9)

cylinder1.volume()

cylinder1.surface_area()