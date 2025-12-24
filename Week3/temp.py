import numpy as np
temp = [20,21,25,23,19,27,18]
npTemp = np.array(temp)
print("Temperature Array: ",end =" ")
for i in range(len(npTemp)):
    print(npTemp[i],"°C",end =" ")
print("\n")
print("Average Temperature: ",round(npTemp.mean(),2),"°C")
print("Maximum Temperature: ",npTemp.max(),"°C")
print("Minimum Temperature: ",npTemp.min(),"°C")
print("Deviation in Temperature: ",round(npTemp.std(),2),"°C")
print("Variance in Temperature: ",round(npTemp.var(),2),"°C")