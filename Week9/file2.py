try:
    file = open("demo","r+")
    file.seek(12)
    print("Current position:",file.tell())
    buffer = file.read()
    print("After seek:",buffer)

except FileNotFoundError:
    print("File doesn't exist")