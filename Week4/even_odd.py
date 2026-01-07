num = int(input("Enter the number: "))
count = flag = 0
for i in range(1,num+1):
    if i % 2 == 0:
        count = count + 1
    else:
        flag = flag + 1
print(f"There are {count} even numbers from 1 to {num}")
print(f"There are {flag} odd numbers from 1 to {num}")
