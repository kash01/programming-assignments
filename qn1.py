import numpy as np

def ipmatrix():
	r = int(input("Enter number of rows"))
	c = int(input("Enter number of columns"))
	A = mymatrix(r,c)
	return(A)

class mymatrix:
	def __init__(self,rows,cols):
		self.rows=rows
		self.cols=cols
		self.m=[]
		for i in range(0,self.rows):
			self.m.append([])
			for j in range(0,self.cols):
				x=float(input("Enter element:"))
				self.m[i].append(x)
			self.mat = np.array(self.m)
			
	def addmatrix(self,mat2):
		return(self.mat+mat2.mat)
		
	def submatrix(self,mat2):
		return(self.mat-mat2.mat)
		
	def mulmatrix(self,mat2):
		if(self.cols == mat2.rows):
			return(self.mat.dot(mat2.mat))
		else:
			return("Not possible to multiply")
			
	def invmatrix(self):
		y = np.linalg.inv(self.mat)
		return(y)
		
class Sqmatrix(mymatrix):
	def __init__(self):
		self.matrix = ipmatrix()
		if(self.matrix.rows!=self.matrix.cols):
			print("Since number of rows and columns are not equal, this is not a square matrix")
		else:
			print("This is a square matrix")
			
	def eigenvaluematrix(self):
		y = np.linalg.eig(self.matrix.mat)
		return(y)
		
A = ipmatrix()
print(A)