try:
    file = open("demo","w+")
    file.write("Hello Chitti\nThis is Python class\nListen carefully ")
    buffer = file.read()
    # buffer1 = file.readline()
    # buffer2 = file.readlines()
    print(buffer)
    # print(buffer1)
    # print(buffer2)

except FileNotFoundError:
    print("File doesn't exist")