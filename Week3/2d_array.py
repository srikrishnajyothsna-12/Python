import numpy as np

lst1 = [[2,12],[4,24]]
lst2 = [[30,1],[11,7]]
arr1 = np.array(lst1)
arr2 = np.array(lst2)
print("2D Array-1:\n",arr1)
print("2D Array-2:\n",arr2)
print("Dimensions of the arrays:\n",arr1.ndim,arr2.ndim)
print("Addition of arrays:\n",np.add(arr1,arr2))
print("Subtraction of arrays:\n",np.subtract(arr1,arr2))
print("Multiplication of arrays:\n",np.dot(arr1,arr2))
print("Multiplication:\n",arr1 @ arr2)
# print("Inverse of a matrix:\n",np.linalg.inv(arr1),2)
print("Trace of Array 1:\n",np.trace(arr1))
print("Transpose of Array 1:\n",np.transpose(arr1))
print("Determinant of Array 1:",np.linalg.det(arr1))