#prompt the user for a day of the week, print out whether the day is Monday or not

day = input("Enter the day of a week: ")
if day.lower().strip() == 'monday':
    print("Today is Monday!")
else:
    print("Today is not Monday!")


#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = input("Enter a day of the week: ")
if (day.lower() == 'sunday' or day.lower() == 'saturday'):
    print(f"{day} is a weekend")
else:
    print(f"{day} is a weekday")

#create variables and make up values for:
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours


hours_worked_per_week = 40
hourly_rate = 120
if hours_worked_per_week <= 40:
    weekly_paycheck = hours_worked_per_week * hourly_rate
else:
    weekly_paycheck = 40 * hourly_rate + (hours_worked_per_week-40) * hourly_rate * 1.5

print(f"Weekly paycheck is $ {weekly_paycheck}")



#While

#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1


#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0

while i <= 100:
    print(i)
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.
i =100
while i >= -10:
    print(i)
    i += -5

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
print(i)
while ((i * i) < 1000000):
    print (i * i)
    i = i * i

# Write a loop that uses print to create the output shown below.
 i = 100
 

 while i >= 5:
     print(i)
     i -= 5


#For Loops

#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

num = input(" Enter a number: ")
i = 1
for i in range(1,11):
    print(f"{num} * {i} = {int(num)*i}")
    i += 1

#Create a for loop that uses print to create the output shown below.

#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999

i = 1

for i in range (1,10):
    print(str(i)*i)

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user 
# if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the 
# continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

num = input("Enter a odd number between 1 and 50: ")

while (num.isdigit() and int(num) <1 or int(num) >50 or int(num) % 2 ==0):
    num = input("Enter a valid input: ")
    if (num.isdigit() and int(num) >1 and int(num) < 50 and (int(num) % 2 == 1)):
        break
        
for i in range(1,51):
    if i != int(num) and i % 2 == 1:
        print(f" Here is a odd number: {i}")
    else:
        continue

#The input function can be used to prompt for input and use that input in your python code. #
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. #
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function #
# returns a string, so you'll need to convert this to a numeric type.)

num = input("Enter a positive number: ")

while (num.isdigit() and int(num)) <= 0:
    num = input("Enter a positive number: ")
    if (num.isdigit() and int(num)>0):
        break
    

for i in range(0, int(num)+1):
    print(i)

#Write a program that prompts the user for a positive integer.#
# Next write a loop that prints out the numbers from the number the user entered down to 1.

num = input("Enter a positive number greater than 1: ")


while (num.isdigit()== False or int(num) <= 1):
    num = input("Enter a positive number greater than 1: ")
    if (num.isdigit() and int(num) > 1):
        break

for i in range(1, int(num)+1):
    print(int(num)+1-i)


 #Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.

for i in range(1,101):
    print(i)


# For multiples of three print "Fizz" instead of the number
for i in range(1,101):
    if i % 3 == 0:
        print("fizz")
    else:
         print(i)


# For the multiples of five print "Buzz".
for i in range(1,101):
    if i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
    if (i % 5 == 0 and i % 3 ==0):
        print("fizzbuzz")
    else:
        print(i)

#Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

num = input("What number would you like to go up to: ")
repeat = 'y'
while repeat == 'y':
    print("Here is your table!"" \n\nnumber | squared | cubed\n------ | ------- | -----")
    for i in range(1, int(num)+1):
        print(f"{i}      | {i*i}       | {i*i*i}")

    repeat = input("Do you want to continue? Type y for yes and n for no")
    num = input("What number would you like to go up to: ")



#Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# Bonus

# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
