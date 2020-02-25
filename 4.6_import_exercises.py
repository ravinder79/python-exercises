import functions

functions.letter_grade(99)


#use from to import the function directly

from functions import remove_vowels  
remove_vowels('Monday')

#use from and give the function a different name

from functions import remove_vowels as rv   

rv('Monday')

#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools

for i in itertools.product('abc', '123'):
    print(i)

#How many different ways can you combine two of the letters from "abcd"?

for i in itertools.combinations('abcd', 2):
    print(i)

import json

profiles = json.load(open("profiles.json"))



#Total number of users
users = len(profiles)
print(users)
 
#Number of active users
user = profiles[0]

active_users = len([user for user in profiles if user["isActive"] == True])
print(active_users)

#Number of inactive users
active_users = len([user for user in profiles if user["isActive"] == False])
print(active_users)

#Grand total of balances for all users
balance = [user['balance'] for user in profiles]
total= 0.00

for i in balance:
    i = i[1:]
    i = i.replace(',', '')
    total = total + float(i)
print(total)


#Average balance per user

average_balance = total/users
print(average_balance)

#User with the lowest balance
low_balance = profiles[-1]['balance']
print(low_balance)
for i in range(0, len(profiles)):
    if profiles[i]['balance'] < low_balance:
        low_balance = profiles[i]['balance']
        low_user = profiles[i]['name']

print(low_user, low_balance) 

#User with the highest balance

high_balance = profiles[-1]['balance']

for i in range(0, len(profiles)):
    if profiles[i]['balance'] > high_balance:
        high_balance = profiles[i]['balance']
        high_balance_user = profiles[i]['name']
print(high_balance_user, high_balance)

#Most common favorite fruit
favoriteFruit = [user['favoriteFruit'] for user in profiles]
print(favoriteFruit)
fav_fruit_dict = {x: favoriteFruit.count(x) for x in favoriteFruit}

# fav_fruit = max(fav_fruit_dict.keys(), key=(lambda k: fav_fruit_dict[k]))
# print(fav_fruit)
most_fav_fruit = max(fav_fruit_dict, key = fav_fruit_dict.get)
print(most_fav_fruit)

#Least most common favorite fruit
# least_fav_fruit = min(fav_fruit_dict.keys(), key=(lambda k: fav_fruit_dict[k]))
# print(least_fav_fruit)
least_fav_fruit = min(fav_fruit_dict, key = fav_fruit_dict.get)
print(least_fav_fruit)


#Total number of unread messages for all users
