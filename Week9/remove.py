import os
try:
    file = input("Enter file name to delete: ")

    if os.path.exists(file):
        os.remove(file)
        print("File deleted successfully.")

except FileNotFoundError:
    print("File does not exist.")