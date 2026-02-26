dct = {"book":30,"pen":10,"pencil":5}
print("Keys:",dct.keys())
print("Values:",dct.values())
print("Items:",dct.items())
print("After popping:",dct.pop("pencil"))
del dct["pen"]
print("After deleting:",dct)