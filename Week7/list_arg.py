def total(marks):
    sum=0
    for i in range(len(marks)):
        sum = sum + marks[i]
    return sum
marks= [98,97,87,99,95]
print("Marks are:",marks)
print("Total marks are:",total(marks))