try:
    file = open("demo","r")
    buffer = file.readlines()
    print(buffer)
    
except FileNotFoundError:
    print("File doesn't exist")