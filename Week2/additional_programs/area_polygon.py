import math
n=int(input("Enter number of sides of polygon:"))
side=float(input("Enter the length of the side:"))
area=(n*math.pow(side,2))/(4*math.tan(math.pi/n))
print("Area of the polygon:",round(area,2))
