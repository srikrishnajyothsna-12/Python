import random
file = open("Random.txt","w")
for i in range(20):
    buffer = random.randint(1,100)
    file.write(str(buffer) + "\n")