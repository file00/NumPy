# NumPy Type Conversion

import numpy as np

# create an array of integers
int_array = np.array([1, 3, 5, 7])

# convert data type of int_array to float
float_array = int_array.astype('float')

# print the arrays and their data types
print(int_array, int_array.dtype)
print(float_array, float_array.dtype)