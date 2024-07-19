# Creating NumPy Arrays With a Defined Data Type
import numpy as np

# create an array of 8-bit integers
array1 = np.array([1, 3, 7], dtype='int8')

# create an array of unsigned 16-bit integers
array2 = np.array([2, 4, 6], dtype='uint16')

# create an array of 32-bit floating-point numbers
array3 = np.array([1.2, 2.3, 3.4], dtype='float32')

# create an array of 64-bit complex numbers
array4 = np.array([1+2j, 2+3j, 3+4j], dtype='complex64')

# print the arrays and their data types
print(array1, array1.dtype)
print(array2, array2.dtype)
print(array3, array3.dtype)
print(array4, array4.dtype)