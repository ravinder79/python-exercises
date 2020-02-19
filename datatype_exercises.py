#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?*/
The_little_mermaid = 3
Brother_bear = 5
Hercules = 1

total_cost = (The_little_mermaid + Brother_bear + Hercules)*3
print(f"We spent {total_cost} on movies")


#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

Google = [400, 10]
Amazon = [380, 6]
Facebook = [350, 4]

payment = Google[0]*Google[1] + Amazon[0] * Amazon[1] + Facebook[0]*Facebook[1]
print(payment)

#A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

is_class_not_full = True
no_conflict_with_schedule = True

can_enroll = is_class_not_full and no_conflict_with_schedule

print(can_enroll)



#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

buy_two_or_more_items = False
offer_not_expired = True
is_premium_member = False

product_offer = (buy_two_or_more_items and offer_not_expired) or (offer_not_expired and is_premium_member)
print(product_offer)



#
username = 'codeup'
password = 'notastrongpassword'


#the password must be at least 5 characters

password_char = len(password) >= 5
print(password)


In [4]: #the username must be no more than 20 characters                                                                                      

In [5]: username_len = len(username)<=20                                                                                                      



In [7]: #the password must not be the same as the username                                                                                    

In [8]: same_u_p = username == password                                                                                                       



In [10]: #bonus neither the username or password can start or end with whitespace                                                             


 whitespace = username[0] == ' ' or password[0] == ' '                                                                                


# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

## Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits] 


## Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]


capitalized_fruits = [fruit.capitalize() for fruit in fruits]

## Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
 def has_vowels_count(x): 
     ...:     count = 0 
     ...:     for char in x: 
     ...:         if char.lower() in 'aeiou': 
     ...:             count = count+1 
     ...:      
     ...:     return count 


fruits_with_more_than_two_vowels = [fruit for fruit in fruits if has_vowels_count(fruit) > 2]

# Exercise 4 - make a variable named # Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']. The result should be ['mango', 'kiwi', 's
fruits_with_only_two_vowels = [fruit for fruit in fruits if has_vowels_count(fruit) == 2] 

#Exercise 5 - make a list that contains each fruit with more than 5 characters

fruits_with_more_than_five_char = [fruit for fruit in fruits if len(fruit)>5]

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_exactly_five_char = [fruit for fruit in fruits if len(fruit) == 5]

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_char = [fruit for fruit in fruits if len(fruit) < 5]

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

numb_of_char = [len(fruit) for fruit in fruits]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

even_numbers = [n for n in numbers if n % 2 == 0] 

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [n for n in numbers if n % 2 == 1]

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = [n for n in numbers if n>0]

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [n for n in numbers if n<0] 

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_or_more_numerals = [n for n in numbers if len(str(abs(n))) >=2]]



# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [n**2 for n in numbers]


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if n<0 and n % 2 != 0]

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [n+5 for n in numbers]

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

def is_prime(x):  
           if x > 1: 
              for n in range(2,x): 
                   if x % n == 0: 
                       return False 
                   else: 
                        return True  
           else: 
              return False
primes = [n for n in numbers if is_prime(n) == True]

#20 Python Data Structure Manipulation Exercises

#How many students are there?
len(students)

#How many students prefer light coffee? For each type of coffee roast?
 light_coffee_students = len([student for student in students if student['coffee_preference'] == 'light'])
 medium_coffee_students = len([student for student in students if student['coffee_preference'] == 'medium'])
 dark_coffee_students = len([student for student in students if student['coffee_preference'] == 'dark'])
#How many types of each pet are there?


#How many grades does each student have? Do they all have the same number of grades?
#What is each student's grade average?
#How many pets does each student have?
#How many students are in web development? data science?
#What is the average number of pets for students in web development?
#What is the average pet age for students in data science?
#What is most frequent coffee preference for data science students?
#What is the least frequent coffee preference for web development students?
#What is the average grade for students with at least 2 pets?
#How many students have 3 pets?
#What is the average grade for students with 0 pets?
#What is the average grade for web development students? data science students?
#What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
#What is the average number of pets for medium coffee drinkers?
#What is the most common type of pet for web development students?
#What is the average name length?
#What is the highest pet age for light coffee drinkers?