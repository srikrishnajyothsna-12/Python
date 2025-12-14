#Right angled Triangle
base=float(input("Enter the length of base of the triangle:"))
height=float(input("Enter the height of the triangle:"))
area=0.5*base*height
print("Area of Right angled triangle:",area)

#Equilateral Triangle
side=float(input("Enter the side of triangle:"))
area_equi=((3**0.5)*side*side)/4
print("Area of Equilateral triangle:",round(area_equi,2))

#Heron's Formula
a=float(input("Enter side a:"))
b=float(input("Enter side b:"))
c=float(input("Enter side c:"))
s=(a+b+c)/2
area_heron=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle(Heron's formula):",round(area_heron,2))