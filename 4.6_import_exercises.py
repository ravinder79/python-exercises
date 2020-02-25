import functions

functions.letter_grade(99)


#use from to import the function directly

from functions import remove_vowels  
remove_vowels('Monday')
print(remove_vowels('Monday'))

#use from and give the function a different name

from functions import remove_vowels as rv   

rv('Monday')
print(rv('Monday'))

#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools
print("\nCombine letters from abc with numbers 1,2 3")
list(itertools.product('abc', '123'))
print(list(itertools.product('abc', '123')))
# for i in itertools.product('abc', '123'):
#     print(i)

#How many different ways can you combine two of the letters from "abcd"?
import itertools
print("\nCombine two letters from abcd")
l = list(itertools.combinations('abcd', 2))
print(l)
# for i in itertools.combinations('abcd', 2):
#     print(i)

import json

profiles = json.load(open("profiles.json"))



#Total number of users
users = len(profiles)
print(f"Total number of users {users}")
 
#Number of active users
user = profiles[0]
active_users = len([user for user in profiles if user["isActive"]])
print(f" Number of active users: {active_users}")

#Number of inactive users
inactive_users = len([user for user in profiles if user["isActive"] == False])
print(f" Number of inactive users: {inactive_users}")

#Grand total of balances for all users
balance = [user['balance'] for user in profiles]
total= 0.00

for i in balance:
    i = i[1:]
    i = i.replace(',', '')
    total = total + float(i)
print(f" Grand total of balances: $ {'%.2f'%total}")


#Average balance per user

average_balance = total/users
print(f" Average balance: {'%.2f'%average_balance}")

#User with the lowest balance
low_balance = profiles[-1]['balance']

for i in range(0, len(profiles)):
    if profiles[i]['balance'] < low_balance:
        low_balance = profiles[i]['balance']
        low_user = profiles[i]['name']

print(f" User with lowest balance: {low_user}, balance:  {low_balance}") 

#min(profiles, key = balance)['name']

#User with the highest balance

high_balance = profiles[-1]['balance']

for i in range(0, len(profiles)):
    if profiles[i]['balance'] > high_balance:
        high_balance = profiles[i]['balance']
        high_balance_user = profiles[i]['name']
print(f"User with highest balance: {high_balance_user}, Balance: {high_balance}")

#Most common favorite fruit
favoriteFruit = [user['favoriteFruit'] for user in profiles]

fav_fruit_dict = {x: favoriteFruit.count(x) for x in favoriteFruit}

# fav_fruit = max(fav_fruit_dict.keys(), key=(lambda k: fav_fruit_dict[k]))
# print(fav_fruit)
most_fav_fruit = max(fav_fruit_dict, key = fav_fruit_dict.get)
print(f" Most common fav fruit is: {most_fav_fruit}")

#Least most common favorite fruit
# least_fav_fruit = min(fav_fruit_dict.keys(), key=(lambda k: fav_fruit_dict[k]))
# print(least_fav_fruit)
least_fav_fruit = min(fav_fruit_dict, key = fav_fruit_dict.get)
print(f" Least most common favorite fruit is : {least_fav_fruit}")


#Total number of unread messages for all users
def message_count(str):
    num = ''
    count = 0   
    for i in str:
        if i in '1234567890':
            num = num + i
        
    count = int(num)
    return count


total_messages = 0
for i in range(0, len(profiles)):
    total_messages = total_messages + message_count(profiles[i]['greeting'])
print(f" total unread messages = {total_messages}")
    