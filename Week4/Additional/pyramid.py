num = int(input("Enter number of lines the pattern should be printed: "))
for i in range(0, num):
    print(" " * (num - i),end = " ")
    print("*" * (2*i+1))


