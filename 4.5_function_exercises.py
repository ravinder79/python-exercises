

# 1. Define a function named is_two. It should accept one input and return True if the passed input is 
#either the number or the string 2, False otherwise.
​
def is_two(x):
    if x == 2 or x ==  '2':
        return True
    else:
        return False


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
​
def is_vowel(str):
    if str.lower() in 'aeiou':
        return True
    else:
        return False


#Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise.
#Use your is_vowel function to accomplish this.
​
def is_consonant(str):
    if is_vowel(str):
        return False
    else:
        return True


#Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of the word if the word starts with a consonant.
​
def cap(str):
    if is_consonant(str[0]):
        return str[0].upper()+str[1:]
    else:
        return str


#Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the 
#bill total, and return the amount to tip.


def calculate_tip(tip_percent, total_bill):
    tip = total_bill * tip_percent
    return '%.2f'%tip



#Define a function named apply_discount. It should accept a original price, and a discount percentage, and return 
#the price after the discount is applied.
In [94]:

def apply_discount(original_price, discount_percentage):
    price_after_discount = (1 - discount_percentage) * original_percentage
    return '%.2f'%price_after_discount


#Define a function named handle_commas. It should accept a string that is a number that contains
#commas in it as input, and return a number as output.
​
def handle_commas(str):
    number = str.replace(',',"")
    return int(number)


#Define a function named get_letter_grade. It should accept a number and return
#the letter grade associated with that number (A-F).
​
def letter_grade(number):
    if number >= 88:
        return 'A'
    elif number >= 80:
        return 'B'
    elif number >= 67:
        return 'C'
    elif number >= 60:
        return 'D'
    else:
        return 'F'


#Define a function named remove_vowels that accepts a string and returns a string with all
#the vowels removed
​
def remove_vowels(str):
    new_word =''
    for char in str:
        if char.lower() not in 'aeiou':
           
            new_word = new_word+char
       
    return new_word


# #Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
​
def normalize_name(x):
    new_word = ''
    while not (x[0].isalpha() or x[0] == '_'):  # this block removes any charcters from front of input except '_' and alphabets
        x = x[1:]
    print(x)
   # x = x.strip()   # this block removes any trailing white spaces
   

    for char in x:       # this block removes any non-alphanumeric characters and replaces space with '_'
        if char == ' ':
            new_word = new_word + '_'
        elif char == "_":
            new_word = new_word + char
        elif not char.isalnum():
            new_word = new_word
        else:
            new_word = new_word + char
    return new_word.lower()
    
​


# Write a function named cumsum that accepts a list of numbers and returns a list that is
#the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]
​
​
def cumsum(x):
    for i in range(0,len(x)):
        if i >= 1 and i < len(x)-1:
            x[i] = x[i] + x[i-1]
        
        if i == len(x)-1:
            x[i] = x[i]+ x[i-1]
        
    
    return x
​
cumsum([1, 2, 3, 4])
    


# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return
# a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.
​
​
def twelveto24(x):
    hour =''
    minute = ''
    a_or_p = ''
   
    if (x[1] == ':'):
        hour = hour + x[0]
        minute = minute + x[2] + x[3]
        a_or_p = x[4]
       
    else:
        hour = hour + x[0] + x[1]
        minute = minute + x[3] + x[4]
        a_or_p = x[5]
       
 
    if (a_or_p == 'p') and (hour != '12'):
            hour = int(hour) + 12
        
        
    elif (a_or_p =='a' and hour == '12'):
            hour = int(hour) - 12
           
        
    else:
            hour = int(hour)
                 
    
    if len(str(hour) + ':' + str(minute)) == 4:
        return '0' + str(hour) + ':' + str(minute)
    
    else:
        return str(hour) + ':' + str(minute)
        
        

# Bonus: write a function that does the opposite.
​
def twentyhourto12(x):
    
    for i in x:
        hour = int(x[0] + x[1])
        minute = int(x[3] + x[4])
​
   
    if hour >= 12:
        am_or_pm = 'pm'
    else:
        am_or_pm = 'am'
​
 
    if hour > 12:
        hour -= 12
        
    
    elif hour == 0:
        hour = 12
        
    
    return  str(hour) + ':' + str(minute) + str(am_or_pm)
        

# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27
​
def col_index(x):
​
    dictt = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
        'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
        'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
        }
    y = x.lower()
    n = len(x)
    num = 0
​
    for i in range(0,n):
        num = (26**(n-1-i)) * int(dictt[y[i]]) +num
​
​
    return num


​
