import math
a,b,c=map(int,input("Enter co-effeicients of quadratic equation:").split())
root_1=(-b+math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
root_2=(-b-math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
print("Root 1:",root_1)
print("Root 2:",root_2)