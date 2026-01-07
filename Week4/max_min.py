a,b,c = map(int, input("Enter three numbers: ").split())
ch = int(input("Enter 1 to find max or 0 to find min: "))
if(ch == 1):
    if(a > b and a > c):
        print(f"{a} is largest number")
    elif(b > c):
        print(f"{b} is largest number")
    else:
        print(f"{c} is largest number")
else:
        if(a < b and a < c):
            print(f"{a} is smallest number")
        elif(b < c):
            print(f"{b} is smallest number")
        else:
            print(f"{c} is smallest number")
