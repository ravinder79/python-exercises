import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
import math
# How many negative numbers are there?


mask = a < 0
negative_num = mask.sum()


# How many positive numbers are there?

mask = a > 0
positive_num = mask.sum()

# How many even positive numbers are there?

a = a[a > 0]
a = a[a % 2 == 0]
even_positives = len(a)


# If you were to add 3 to each data point, how many positive numbers would there be?
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a = a + 3
mask = a > 0
mask.sum()


# If you squared each number, what would the new mean and standard deviation be?
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
 
a = a ** 2

print(a.mean())
print(a.std())


# A common statistical operation on a dataset is centering.
#  This means to adjust the data such that the center of the data is at 0.
#  This is done by subtracting the mean from each data point. Center the data set.

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

mean = a.mean()
a = a - mean
print(a)


