

#20 Python Data Structure Manipulation Exercises
students = [
    {
"id": "100001",
"student": "Ada Lovelace",
"coffee_preference": "light",
"course": "web development",
"grades": [70, 91, 82, 71],
"pets": [{"species": "horse", "age": 8}],
    },
    {
"id": "100002",
"student": "Thomas Bayes",
"coffee_preference": "medium",
"course": "data science",
"grades": [75, 73, 86, 100],
"pets": [],
    },
    {
"id": "100003",
"student": "Marie Curie",
"coffee_preference": "light",
"course": "web development",
"grades": [70, 89, 69, 65],
"pets": [{"species": "cat", "age": 0}],
    },
    {
"id": "100004",
"student": "Grace Hopper",
"coffee_preference": "dark",
"course": "data science",
"grades": [73, 66, 83, 92],
"pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
"id": "100005",
"student": "Alan Turing",
"coffee_preference": "dark",
"course": "web development",
"grades": [78, 98, 85, 65],
"pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
"id": "100006",
"student": "Rosalind Franklin",
"coffee_preference": "dark",
"course": "data science",
"grades": [76, 70, 96, 81],
"pets": [],
    },
    {
"id": "100007",
"student": "Elizabeth Blackwell",
"coffee_preference": "dark",
"course": "web development",
"grades": [69, 94, 89, 86],
"pets": [{"species": "cat", "age": 10}],
    },
    {
"id": "100008",
"student": "Rene Descartes",
"coffee_preference": "medium",
"course": "data science",
"grades": [87, 79, 90, 99],
"pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
"id": "100009",
"student": "Ahmed Zewail",
"coffee_preference": "medium",
"course": "data science",
"grades": [74, 99, 93, 89],
"pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
"id": "100010",
"student": "Chien-Shiung Wu",
"coffee_preference": "medium",
"course": "web development",
"grades": [82, 92, 91, 65],
"pets": [{"species": "cat", "age": 8}],
    },
    {
"id": "100011",
"student": "William Sanford Nye",
"coffee_preference": "dark",
"course": "data science",
"grades": [70, 92, 65, 99],
"pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
"id": "100012",
"student": "Carl Sagan",
"coffee_preference": "medium",
"course": "data science",
"grades": [100, 86, 91, 87],
"pets": [{"species": "cat", "age": 10}],
    },
    {
"id": "100013",
"student": "Jane Goodall",
"coffee_preference": "light",
"course": "web development",
"grades": [80, 70, 68, 98],
"pets": [{"species": "horse", "age": 4}],
    },
    {
"id": "100014",
"student": "Richard Feynman",
"coffee_preference": "medium",
"course": "web development",
"grades": [73, 99, 86, 98],
"pets": [{"species": "dog", "age": 6}],
    },
]

def students_coffee_pref(x): 
     light_coffee_drinkers = 0 
     medium_coffee_drinkers = 0 
     dark_coffee_drinkers = 0 
    
  
     if x == 'light': 
         for i in range(0,len(students)): 
             if students[i]['coffee_preference'] == 'light': 
                 light_coffee_drinkers += 1 
         return light_coffee_drinkers 
     if x == 'medium':  
          for i in range(0,len(students)):  
                if students[i]['coffee_preference'] == 'medium':  
                 medium_coffee_drinkers += 1  
          return medium_coffee_drinkers

print(students_coffee_pref('light'))

#How many grades does each student have? Do they all have the same number of grades?

def student_grades(x):
    if x == 'grades':

        count = 0
    for i in range(0, len(students)):
        count = len(students[i]['grades'])
        print(f"{students[i]['student']} = {count}")
    

student_grades('grades')

#How many types of each pet are there?

pet_list = []
for i in range(0, len(students)):
    pet_list = pet_list + students[i]['pets']

print(pet_list)

pet_species = pet_list[0]

pet_dict = {x:pet_list.count(x) for x in pet_list}

print(pet_dict)