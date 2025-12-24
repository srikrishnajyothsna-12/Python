import numpy as np

arr = np.ndarray((5), dtype=int)
arr[:] = [10, 20, 30, 40, 50]
print("1D Array:\n",arr)

arr2 = np.ndarray((2,2),dtype = int)
arr2[:] = [[2,12],[4,24]]
print("2D Array:\n",arr2)