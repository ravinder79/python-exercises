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
