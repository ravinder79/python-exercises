#Print out every line in the file. 
#Print out every line in the file, but add a line numbers
with open('4.6_import_exercises.py', 'r') as f:
    data = f.readlines()
    for i, line in enumerate(data):
        print(i+1, line)
    
#Print out every line in the file, but add a line numbers
#count = 0



# with open('4.6_import_exercises.py', 'r') as f:
#     for lines in f:
#         print(str(count)+'\t'+lines)
#         count = count +1


#  Create a variable named grocery_list. It should be a list, and the elements in the list should be a least 3 things
#  that you need to buy from the grocery store.

grocery_list = ['milk', 'eggs', 'coke', 'chips']


# Create a function named make_grocery_list. When run, this function should write the contents of the grocery_list 
# variable to a file named my_grocery_list.txt.
def make_grocery_list(list):
    with open("grocery_list.txt", "w") as f:
        for l in list:
            f.writelines(l + '\n)
    return f
    

make_grocery_list(grocery_list)


# Create a function named show_grocery_list. When run, it should read the items from the text file and show each item on the grocery list.

# def show_grocery_list(grocery_list):
#     with open("grocery_list.txt", "r") as f:
#         print(f.readlines())

def show_grocery_list(grocery_list):
    with open("grocery_list.txt", "r") as f:
        contents = f.readlines()
        for item in contents:
            print(item)

show_grocery_list(grocery_list)

# Create a function named buy_item. It should accept the name of an item on the grocery list, and remove that item from the list.

def buy_item(item):
    
    grocery_list.remove(item)
    make_grocery_list(grocery_list)
    return show_grocery_list(grocery_list)

buy_item('eggs')
