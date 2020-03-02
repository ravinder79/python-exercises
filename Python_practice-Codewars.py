# Welcome. In this kata, you are asked to square every digit of a number.
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    list = []
    a = str(num)
    for i in range(0, len(a)):
        list.append(str(int(a[i])**2))
    return int(''.join(list))


# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

def get_Middle(s): 
    if len(s)> 1:
    
        if len(s)% 2 == 1:
            middle = s[int((len(s)-1)/2)]
            return middle
        else:
            middle = s[int(len(s)/2-1)]+ s[int(len(s)/2)]
            return middle
    else:
          return s

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value
#  next to each other and preserving the original order of elements.

def unique_in_order(s):
    if len(s)>1:
        list = [s[0]]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                list.append(s[i])
        return list
    else:
        return s

# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    list = []
    for i in range(0, len(s)):
        list.append(s[i]*(i+1))
    for i in range(0, len(list)):
        list[i] = list[i].capitalize()
    
    return '-'.join(list)
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(num):
    if num > 3:
        list = []
        for i in range(2, num):
            if i % 3 == 0 or i % 5 == 0:
                list.append(i)
                
        l = list[0]
        return sum([l for l in list])
        return list
    elif num == 3:
            return 3
    else:
        return 0
    

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

# we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
# In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

def dig_pow(n, p):
    # your code
    return -1