try:
    file = open("demo","r")
    buffer1 = file.readline()
    buffer2 = file.readline()
    buffer3 = file.readline()
    print("Line 1:",buffer1)
    print("Line 2:",buffer2)
    print("Line 3:",buffer3)

except FileNotFoundError:
    print("File doesn't exist")