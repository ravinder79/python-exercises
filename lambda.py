people = [{'name': 'Peter', 'pieces_of_flair': 5},
 {'name': 'Joanna', 'pieces_of_flair': 14},
 {'name': 'Samir', 'pieces_of_flair': 4},
 {'name': 'Milton', 'pieces_of_flair': 9}]
sorted(people, key=lambda person: person['name'])
# [{'name': 'Joanna', 'pieces_of_flair': 14},
#  {'name': 'Milton', 'pieces_of_flair': 9},
#  {'name': 'Peter', 'pieces_of_flair': 5},
#  {'name': 'Samir', 'pieces_of_flair': 4}]
sorted(people, key=lambda person: person['pieces_of_flair'])
# [{'name': 'Samir', 'pieces_of_flair': 4},
#  {'name': 'Peter', 'pieces_of_flair': 5},
#  {'name': 'Milton', 'pieces_of_flair': 9},
#  {'name': 'Joanna', 'pieces_of_flair': 14}]
def sort_by_flair(person):
    return  person["pieces_of_flair"]
sorted(people, key=sort_by_flair)
# [{'name': 'Samir', 'pieces_of_flair': 4},
#  {'name': 'Peter', 'pieces_of_flair': 5},
#  {'name': 'Milton', 'pieces_of_flair': 9},
#  {'name': 'Joanna', 'pieces_of_flair': 14}]
def sort_by_length_of_name(person):
        return len(person["name"])
people
# [{'name': 'Peter', 'pieces_of_flair': 5},
#  {'name': 'Joanna', 'pieces_of_flair': 14},
#  {'name': 'Samir', 'pieces_of_flair': 4},
#  {'name': 'Milton', 'pieces_of_flair': 9}]
sorted(people, key=sort_by_length_of_name)
# [{'name': 'Peter', 'pieces_of_flair': 5},
#  {'name': 'Samir', 'pieces_of_flair': 4},
#  {'name': 'Joanna', 'pieces_of_flair': 14},
#  {'name': 'Milton', 'pieces_of_flair': 9}]
def sort_alphabetically_by_last_letter_of_name(person):
    return person["name"][-1]
sorted(people, key=sort_alphabetically_by_last_letter_of_name)
# [{'name': 'Joanna', 'pieces_of_flair': 14},
#  {'name': 'Milton', 'pieces_of_flair': 9},
#  {'name': 'Peter', 'pieces_of_flair': 5},
#  {'name': 'Samir', 'pieces_of_flair': 4}]
sorted(people, key=lambda x: x["name"][-1])