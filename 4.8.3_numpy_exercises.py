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
stddev = a.std()
mean = a.mean()
a = a - mean
print(a)


# Calculate the z-score for each data point. Recall that the z-score is given by:


# Z=x−μ/σ

z_scores = a/stddev
print(z_scores)

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
# a = np.array(a)

# sum_of_a = a.sum()
# print(sum_of_a)

sum_of_a = sum(a)
print(sum_of_a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# min_of_a = a.min()
# print(min_of_a)
min_of_a = min(a)
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a)/len(a)
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

prod = 1
for i in range(0, len(a)):
    prod = a[i] * prod

product_of_a = prod
print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [i*i for i in a]


print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [i for i in a if i % 2 ==1]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [i for i in a if i % 2 == 0]
print(evens_in_a)