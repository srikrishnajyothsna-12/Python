try:
    file = open("sample","w")
    file.write("Hello Python")
    file.flush()
    print("Flushed")

except FileNotFoundError:
    print("File doesn't exist")