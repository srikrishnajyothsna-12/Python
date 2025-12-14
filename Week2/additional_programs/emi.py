import math
prin=float(input("Enter principal amount:"))
rate=float(input("Enter monthly interest rate:"))
n=int(input("Enter number of installments:"))
emi=(prin * rate * (math.pow(1+rate,n))) / ((math.pow (1+rate,n)-1))
print("EMI :",round(emi,2))