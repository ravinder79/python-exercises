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


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]


sum_of_b = 0
for i  in range(0, len(b)):
    sum_of_b = (sum_of_b + sum(b[i]))

print(sum_of_b)


if min(b[0])< min(b[1]):
    min_of_b = min(b[0])
else:
    min_of_b = min(b[1])

print(min_of_b)


if max(b[0])< max(b[1]):
    max_of_b = max(b[1])
else:
    max_of_b = max(b[0])

print(max_of_b)

mean_of_b = sum_of_b/(len(b[0])+len(b[1]))
print(mean_of_b)

prod_of_b = 1
for i in b:
    for e in i:
        prod_of_b = prod_of_b * e

print(prod_of_b)

squares_of_b = []
for i in b:
    for e in i:
        squares_of_b.append(e ** 2)

print(squares_of_b)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array(b)

sum_of_b = b.sum()
print(sum_of_b)

# Exercise 2 - refactor the following to use numpy. 
#min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = b.min()
print(min_of_b)
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
#max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b = b.max()
print(max_of_b)

# Exercise 4 - refactor the following using numpy to find the mean of b
#mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b = b.mean()
print(mean_of_b)


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

product_of_b = b.prod()
print(prod_of_b)
# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

squares_of_b = np.square(b)
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

odds_in_b = b[b % 2 == 1]
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
print(evens_in_b)
# Exercise 9 - print out the shape of the array b.

print(b.shape)

# Exercise 10 - transpose the array b.

print(b.T)


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.reshape(1, 6)
print(b.reshape(1, 6))


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(-1,6)
print(b.reshape(-1,1))


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_of_c = c.min()
max_of_c = c.max()
sum_of_c = c.sum()
prod_of_c = c.prod()

print(min_of_c )
print(max_of_c)
print(sum_of_c)
print(prod_of_c)
# Exercise 2 - Determine the standard deviation of c.

std_dev_c = c.std()

print(std_dev_c)
# Exercise 3 - Determine the variance of c.

variance_c = c.var()
print(variance_c)

# Exercise 4 - Print out the shape of the array c
print(c.shape)

# Exercise 5 - Transpose c and print out transposed result.
c_transpose = c.T
print(c_transpose)

# Exercise 6 - Get the dot product of the array c with c. 
dot_product_c = np.dot(c, c)
print(dot_product_c)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

sum_prod_c = np.multiply(c, c.T).sum()
print(sum_prod_c)
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
c_times_c = np.multiply(c, c.T).prod()
print(c_times_c)

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
print(np.sin(d))

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
print(np.cos(d))
# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
print(np.tan(d))
# Exercise 4 - Find all the negative numbers in d
d[d < 0]

# Exercise 5 - Find all the positive numbers in d
d[d > 0]

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.
np.unique(d).size

# Exercise 8 - Print out the shape of d.
d.shape

# Exercise 9 - Transpose and then print out the shape of d.
d.T.shape

# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9, 2)
