# Task 1
# Write a Python script to sort (ascending and descending) a dictionary by value.

import operator

dict_task1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}	
print('Original dictionary : ',dict_task1)
sorted_dict_task1 = sorted(dict_task1.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_dict_task1)
sorted_dict_task1 = dict( sorted(dict_task1.items(), key=operator.itemgetter(1), reverse=True))
print('Dictionary in descending order by value : ',sorted_dict_task1)  

# Task 2
# Write a Python script to add a key to a dictionary.

dict_task2 = {0:10, 1:20}
print("Dictionary before added key:", dict_task2)
dict_task2.update({2:30})
print("Dictionary after added key:", dict_task2)

# Task 3
# Write a Python script to concatenate the following dictionaries to create a new one.

dict1_task3 = {1:10, 2:20}
dict2_task3 = {3:30, 4:40}
dict3_task3 = {5:50, 6:60}
dict4_task3 = {}

for d in (dict1_task3, dict2_task3, dict3_task3):
   dict4_task3.update(d)
   
print("Dictionary made out of 3 smaller dictionaries:", dict4_task3)

#Task 4
# Write a Python script to check whether a given key already exists in a dictionary.

dict_task4 = {1:10, 2:20, 3:30, 4:40}

def chceck_in_dict(x):
   if x in dict_task4:
      print("Key is already in dictionary")
   else:
      print("Key is not in dictionary")
      
chceck_in_dict(3)
chceck_in_dict(5)

# Taks 5
# Write a Python program to iterate over dictionaries using for loops.

dict_task5 = {'a': 1, 'b': 5, 'c': 10} 
for dict_key, dict_value in dict_task5.items():
    print(dict_key, '->', dict_value)

# Task 6
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input("Input a number "))
dict_task6 = dict()
for x in range(1, n + 1):
    dict_task6[x] = x * x

print(dict_task6) 

# Task 7
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
dict_task7 = dict()

for x in range(1,16):
   dict_task7[x] = x ** 2
   
print(dict_task7)

# Task 8
# Write a Python script to merge two Python dictionaries.

dict1_task8 = {1:10, 2:20}
dict2_task8 = {3:30, 4:40}
print("Separated dictionaries")
print(dict1_task8)
print(dict2_task8)
dict1_task8.update(dict2_task8)
print("Merged dictionaries")
print(dict1_task8)

# Task 9
# Write a Python program to iterate over dictionaries using for loops.

dict_task9 = {'Black': 1, 'Yellow': 2, 'Red': 3}
for color_key, value in dict_task9.items():
    print(color_key, 'corresponds to ', dict_task9[color_key])
    
# Task 10
# Write a Python program to sum all the items in a dictionary.

dict_task10 = {'x': -53, 'y': 23, 'z': 392}
sum_task10 = sum(dict_task10.values())
print("Sum of dictionary items:", sum_task10)

# Task 11
# Write a Python program to multiply all the items in a dictionary.

dict_task11 = {'data1': 100, 'data2': 24, 'data3': -142}
result = 1
for key in dict_task11:
    result = result * dict_task11[key]

print(result) 

# Task 12
# Write a Python program to remove a key from a dictionary.
dict_task12 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict_task12)
if 'a' in dict_task12:
    del dict_task12['a']

print(dict_task12)

# Task 13
# Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']
values = [1, 2, 3]
dict_task13 = dict(zip(keys, values))
print(dict_task13)

# Task 14
# Write a Python program to get a dictionary from an object's fields.

class dict_task14(object):
    def __init__(self):
        self.a = 'red'
        self.b = 'Yellow'
        self.c = 'Green'
    def do_nothing(self):
        pass

test = dict_task14()
print(test.__dict__) 

# Task 15
# Write a Python program to check if a dictionary is empty or not.

# Create an empty dictionary 'my_dict'.
dict_task15 = {}
if not bool(dict_task15):
    print("Dictionary is empty")
    
# Task 16
# Write a Python program to combine two dictionary by adding values for common keys.

# Import the 'Counter' class from the 'collections' module.
from collections import Counter

dict1_task16 = {'a': 100, 'b': 200, 'c': 300}
dict2_task16 = {'a': 300, 'b': 200, 'd': 400}
dict_task16 = Counter(dict1_task16) + Counter(dict2_task16)
print(dict_task16)

# Task 17
# Write a Python program to sort a list alphabetically in a dictionary.

dict_task17= {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict_task17 = {x: sorted(y) for x, y in dict_task17.items()}
print(sorted_dict_task17)

# Task 18
# Write a Python program to sort Counter by value.

from collections import Counter

dict_task18 = Counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})
print(dict_task18.most_common())

# Task 19
# Write a Python program to match key values in two dictionaries.

dict1_task19 = {'key1': 5, 'key2': 6, 'key3': 5}
dict2_task19 = {'key1': 5, 'key2': 48}
for (key, value) in set(dict1_task19.items()) & set(dict2_task19.items()):
    print('%s: %s is present in both x and y' % (key, value))

# Task 20
# Write a Python program to access dictionary key's element by index.

dict_task20 = {'physics': 43, 'math': 100, 'chemistry': 13}
print("\nAccess the keys of the dictionary as a list:")
print(list(dict_task20)[0])
print(list(dict_task20)[1])
print(list(dict_task20)[2])
