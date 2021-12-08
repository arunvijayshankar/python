"""

You have to order wrapping paper for presents. Given the length, width, and height of the boxes you need to wrap,
return the number of square feet (or whatever units you want) of wrapping paper you need to order. 
Extra credit: allow for other shapes of presents and their dimensions!

Example:

$ wrap(2, 3, 4)
$ 52 square feet


"""
import math

#Static methods to comute surface areas of varying shapes
#Accepts: list of objects dimensions
#Returns surface area
class Area:

	@staticmethod
	def rect(dim):
		return(dim[0] * dim[1] * dim[2])

	@staticmethod
	def sphere(dim):
		return((dim * dim) / 3.14)

	@staticmethod
	def cone(dim):
		l = dim[0]
		r = dim[1] / 2
		return(3.14 * r * (l + r))

	@staticmethod
	def cyl(dim):
		h = dim[0]
		r = dim[1] / 2
		return(2 * 3.14 * r * (r + h))

#Calls appropriate function to compute total area of wrapping paper needed 
#To wrap 'num' number of boxes of 'type' shape
#Accepts: type, num
#Returns: Total amount of wrapping paper needed in square feet
def paperArea(type, num):
	if type == "rect":
		return(Gifts.rectangle(num))
	elif type == "cube":
		return(Gifts.cube(num))
	elif type == "sph":
		return(Gifts.sphere(num))
	elif type == "cone":
		return(Gifts.cone(num))
	elif type == "cyl":
		return(Gifts.cylinder(num))
	elif type == "oval":
		return(Gifts.oval(num))
	else:
		return(Gifts.irr(num))

#Static methods to compute total surface area of 'num' number of objects
#of specified type
#Accepts: num
#Returns: Total surface area
class Gifts:

	@staticmethod
	def rectangle(num):
		print("Enter the dimensions of the rectangular gifts")
		A = 0
		for i in range(num):
			l = input("Length of gift " + str(i+1) +": ")
			b = input("Breadth of gift " + str(i+1) +": ")
			d = input("Depth of gift " + str(i+1) + ": ")
			A += Area.rect([l, b, d])
		return(A)

	@staticmethod
	def cube(num):
		print("Enter the dimensions of the cubical gifts")
		cubDim = list()
		A = 0
		for i in range(num):
			s = input("Length of side of gift " + str(i+1) +": ")
			cubDim.append([s, s, s])
			A += Area.rect(cubDim[i])
		return(A)

	@staticmethod
	def sphere(num):
		print("Enter the circumferences of the spherical gifts")
		A = 0
		for i in range(num):
			C = input("Circuference of gift " + str(i+1) + ": ")
			A += Area.sphere(C)
		return(A)

	@staticmethod
	def cone(num):
		print("Enter the dimensions of the conical gifts")
		A = 0
		for i in range(num):
			l = input("Length from tip to base of gift " + str(i+1) + ": ")
			d = input("Diameter of base of gift " + str(i+1) + ": ")
			A += Area.cone([l, d])
		return(A)

	@staticmethod
	def cylinder(num):
		print("Enter the dimensions of the cylindrical gifts")
		A = 0
		for i in range(num):
			l = input("Length of gift " + str(i+1) + ": ")
			d = input("Diameter of gift " + str(i+1) + ": ")
			A += Area.cyl([l, d])
		return(A)

	@staticmethod
	def oval(num):
		print("Enter the dimensions of the oval gifts")
		A = 0
		for i in range(num):
			d = input("Length of gift " + str(i+1) + " on longest side: ")
			A += Area.sphere(3.14 * d)
		return(A)

	def irr(num):
		print("Enter the dimensions of the boxes that the irregularly shaped gifts are in")
		A = 0
		for i in range(num):
			l = input("Length of box " + str(i+1) +": ")
			b = input("Breadth of box " + str(i+1) +": ")
			d = input("Depth of box " + str(i+1) + ": ")
			A += Area.rect([l, b, d])
		return(A)

#calculates area of wrapping paper needed to wrap one rectangular gift,
#given gift dimensions
def wrap(l, b, h):
	print(str(Area.rect([l, b, h])) + " square feet")


#calculates are of wrapping paper needed to wrap one gift of various shapes,
#given gift dimensions
def wrapShapes():

	pi = 3.14

	print("How is the gift shaped?")
	print("Choose from: rectangle, sphere, cube, cone, cylinder, oval, other")
	shape = str(raw_input(" ")).lower()

	if shape == "rectangle":
		dim = tuple()
		print("What are the dimensions of the gift? Separate the values with commas")
		print("E.g., 3, 4, 5")
		dim = input("Enter dimensions: ")
		return(Area.rect(dim))
	elif shape == "cube":
		s = input("What is the length of the side? E.g., 5: ")
		return(Area.rect([s, s, s]))
	elif shape == "cone":
		l = input("What is the length of the gift from tip to base? E.g., 10: ")
		d = input("What is the diameter of the base of the gift? E.g., 3: ")
		return(Area.cone([l, d]))
	elif shape == "cylinder":
		h = input("What is the length of the gift? E.g., 5: ")
		d = input("What is the diameter of the base of gift? E.g., 5: ")
		return(Area.cyl([h, d]))
	elif shape == "oval":
		d = input("What is the approximate length of the gift on it's longest side? E.g., 5: ")
		return(Area.sphere(pi * d))
	elif shape == "sphere":
		C = input("What is the circumference of the gift? E.g., 5: ")
		return(Area.sphere(C))
	elif shape == "other":
		l = input("What is the approximate length of the gift on it's longest side? E.g., 10: ")
		h = input("What is the approximate length of the second longest side? E.g., 5: ")
		b = input("What is the approximate length of the smallest side? E.g., 2: ")
		return(Area.rect([l, b, h]))
	else:
                l = input("What is the approximate length of the gift on it's longest side? E.g., 10: ")
                h = input("What is the approximate length of the second longest side? E.g., 5: ")
                b = input("What is the approximate length of the smallest side? E.g., 2: ")
                return(Area.rect([l, b, h]))

#calculates total amount of wrapping paper needed in square feet needed
#to wrap multiple gifts of varying shapes
def wrapMultiple():
	gifts = dict()
	print("How many are rectangular in shape?")
	gifts["rect"] = input("")
	print("How many are spherical?")
	gifts["sph"] = input("")
	print("How many are cube shaped")
	gifts["cube"] = input("")
	print("How many are conical?")
	gifts["cone"] = input("")
	print("How many are oval in shape?")
	gifts["oval"] = input("")
	print("How many are cylindrical?")
	gifts["cyl"] = input("")
	print("How many are irregularly shaped?")
	gifts["irr"] = input("")
	if gifts["irr"]:
		print("Put the irregularly shaped gifts into rectangular boxes")
	A = 0
	for key in gifts.keys():
		if gifts[key]:
			A += paperArea(key, gifts[key])
	print(str(math.ceil(A)) + " square feet")

if __name__ == "__main__":
	numGifts = input("How many gifts are you wrapping: ")
	if numGifts <= 0:
		print("Congratulations! You don't need any wrapping paper!!")
	elif numGifts == 1:
		isRect = str(raw_input("Is the gift rectangular? [y/n]: ")).lower()
		while isRect not in ['y', 'n', "yes", "no"]:
			isRect = str(raw_input("Is the gift rectangular? [y/n]: "))
		if isRect in ['y', "yes"]:
			print("Enter the dimensions of the gift")
			l = input("Length of gift: ")
			b = input("Breadth of gift: ")
			d = input("Depth of gift: ")
			wrap(l, b, d)
		else:
			A = wrapShapes()
			print(str(math.ceil(A)) + " square feet")
	else:
		wrapMultiple()
