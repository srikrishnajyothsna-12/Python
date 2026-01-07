a, b = map(int, input("Enter two numbers to perform GCD: ").split())
while b != 0:
    a, b = b, a % b
print(f"GCD = {a}")