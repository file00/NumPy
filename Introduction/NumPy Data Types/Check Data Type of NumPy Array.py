# Check Data Type of NumPy Array
import numpy as np

# create an array of  integers
int_array = np.array([-3, -1, 0, 1])

# create an array of floating-point numbers
float_array = np.array([0.1, 0.2, 0.3])

# create an array of complex numbers
complex_array = np.array([1+2j, 2+3j, 3+4j])

# check the data type of int_array
print(int_array.dtype)  # prints int64

# check the data type of float_array
print(float_array.dtype)  # prints float64

# check the data type of complex_array
print(complex_array.dtype)  # prints complex128