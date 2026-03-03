import os
try:
    demo = input("Enter source file name: ")
    destination = input("Enter new file name or path: ")

    if os.path.exists(demo):
        os.rename(demo, destination)
        print("File moved successfully.")

except FileNotFoundError:
    print("Source file does not exist.")