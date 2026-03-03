import os
try:
    demo = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    if os.path.exists(demo):
        with open(demo, 'r') as f1:
            data = f1.read()

        with open(destination, 'w') as f2:
            f2.write(data)

        print("File copied successfully.")
except FileNotFoundError:
    print("Source file does not exist.")