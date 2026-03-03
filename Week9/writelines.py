try:
    file = open("demo","a+")
    file.writelines("Hello students\nGain knowledge")

except FileNotFoundError:
    print("File doesn't exist")