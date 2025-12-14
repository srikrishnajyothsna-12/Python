import math
x1,y1=map(int,input("Enter co-ordinates of A:").split())
x2,y2=map(int,input("Enter co-ordinates of B:").split())
distance=math.sqrt(math.pow(x1-x2,2)-math.pow(y1-y1,2))
print("Distance between A and B:",round(distance,2))