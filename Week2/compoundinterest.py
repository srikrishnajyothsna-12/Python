import math
pri=float(input("Enter principal amount:"))
rate=float(input("Enter rate of interest:"))
time=float(input("Enter the time(in years):"))
interest=pri*(math.pow(1+(rate/100),time))-pri
print("Compound interest:",interest)