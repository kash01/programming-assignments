import math

class Polygon:
	def __init__(self,n):
		self.n = n
		self.sides = []

	def inputsides(self):
		for i in range(self.n):
			self.sides.append(float(input("Enter side\n")))
		return(self.sides)
		
	def dipsides(self):
		for i in range(self.n):
			print("Side ",i+1, "is ",self.sides[i])
			
class Triangle(Polygon):
	def __init__(self):
		Polygon.__init__(self,3)

	def findArea(self):
		a = self.sides[0]
		b = self.sides[1]
		c = self.sides[2]
		s = float(float(a+b+c) * 0.5)
		area = math.sqrt(s*(s-a)*(s-b)*(s-c))
		print("The area of the triangle is ",area)
		
t1 = Triangle()
t1.inputsides()
t1.dipsides()
t1.findArea()