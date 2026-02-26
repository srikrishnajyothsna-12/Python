dct = {"book":30,"pen":10,"pencil":5,"eraser":5}
dct2 = [k for k,v in dct.items() if v == 5]
print(dct2)