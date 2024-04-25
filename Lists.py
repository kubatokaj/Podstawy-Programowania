# Task 1
# Write a Python program to sum all the items in a list.

def sum_list(list_task1):
   sum_task1 = 0
   for element_task1 in list_task1:
      sum_task1 += element_task1
      
   return sum_task1
print("Sum of elements in list:", sum_list([3,5,2]))

# Task 2
# Write a Python program to multiply all the items in a list.

def multiply_list(list_task2):
   mult_task2 = 1
   for element_task2 in list_task2:
      mult_task2 *= element_task2
      
   return mult_task2
print("Multiplied list elements:", multiply_list([3,5,2]))

# Task 3
# Write a Python program to get the largest number from a list.

def largest_task3(list_task3):
   max_task3 = list_task3[0]
   for element_task3 in list_task3:
      if element_task3 > max_task3:
         max_task3 = element_task3
         
   return max_task3
print("Largest numnber in list:", largest_task3([4,7,23,5,2,1]))

# Task 4
# Write a Python program to get the smallest number from a list. 

def smallest_task4(list_task4):
   min_task4 = list_task4[0]
   for element_task4 in list_task4:
      if element_task4 < min_task4:
         min_task4 = element_task4
         
   return min_task4
print("Smallest numnber in list:", smallest_task4([4,7,23,5,2,1]))

# Task 5
# Write a Python program to remove duplicates from a list.

list_task5 = [13, 31, 4, 4, 214, 214, 5, 53, 53, 54, 3, 10, 10, 20]
dup_items_task5 = set()
uniq_items_task5 = []
for x in list_task5:
    if x not in dup_items_task5:
        uniq_items_task5.append(x)
        dup_items_task5.add(x)
print("List without duplicates:", dup_items_task5)

# Task 6
# Write a Python program to check if a list is empty or not.

empty_list_task6 = []
list_task6 = [3, 6, 45, 34]
if empty_list_task6 == list_task6:
   print("List is empty")
else:
   print("List is not empty")
   
# Task 7
# Write a Python program to clone or copy a list.

list_task7 = [4,34,32,6,3,1]
new_list_task7 = list(list_task7)
print("Original list:", list_task7)
print("Copied list:", new_list_task7)

# Task 8
# Write a Python function that takes two lists and returns True if they have at least one common member.
def common_member(list_task8_1, list_task8_2):
   result = False
   for x in list_task8_1:
      for y in list_task8_2:
         if x == y:
            result = True
            return result
     
print(common_member([5,4,3,2,1], [5,6,7,8,9]))
print(common_member([1,2,3,4,5], [6,7,8,9]))

# Task 9
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

list_task9 = ['Zero','One', 'Two', 'Three', 'Four', 'Five', 'Six']
list_task9 = [x for (i, x) in enumerate(list_task9) if i not in (0, 4, 5)]
print("List without 0th 4th and 5th elements:", list_task9)

# Task 10
# Write a Python program to print the numbers of a specified list after removing even numbers from it.

list_task10 = [2,54,3,56,53,77,90,32,1,99]
list_task10 = [x for x in list_task10 if x % 2 != 0]
print(list_task10)

# Task 11
# Write a Python program to select an item randomly from a list. Use random.choice() to get a random element from a given list.

import random

list_task11 = [43,6,23,642,12,4,123,54]
print("Full list:", list_task11)
print("Random number from list:", random.choice(list_task11))

# Task 12
# Write a Python program to find the index of an item in a specified list.
list_task12 = [4,231,45,24,54,26,53,23,5,4,2,1]
print("Index:", list_task12.index(4))

# Task 13
# Write a Python program to append a list to the second list.
list_task13_1 = [1,5,2,6,8,4,2]
list_task13_2 = ["blue", "black", "white"]
final_list_task13 = list_task13_1 + list_task13_2
print(final_list_task13)

# Task 14
# Write a Python program to count the number of elements in a list within a specified range.

def elements_in_range(list_task14, min, max):
   counter = 0
   
   for i in list_task14:
      if min <= i <= max:
         counter +=1 
         
   return counter

test_list_task14 = [10,43,23,543,24,1,47,2,4,5]
print("Amount of numbers that are in range of 5 and 40:", elements_in_range(test_list_task14, 5, 40))

# Task 15
# Write a Python program to find common items in two lists.

list_task15_1 = ["White", "Blue", "Green", "Yellow"]
list_task15_2 = ["Black", "Blue", "Red", "Green"]
print("Colors that are common in both lists:", set(list_task15_1) & set(list_task15_2))

# Task 16 
# Write a Python program to select the odd items from a list.

list_task16 = [1,2,3,4,5,6,7,8,9]
print(list_task16[::2])

# Task 17
# Write a Python program to print a list of space-separated elements.

list_task17 = [9,8,6,4,3,2]
print("Original list:", list_task17)
print("Space separated elements:",*list_task17)

# Task 18
# Write a Python program to generate all permutations of a list in Python.
import itertools
print(list(itertools.permutations([3,2,1])))

# Task 19
# Write a Python program to convert a list of characters into a string.
list_task19 = ['c','sq', 'sd', 'ds','w']
string_task19 = ''.join(list_task19)
print("Original list:" , list_task19)
print("List converted to string:", string_task19)

# Task 20
# Write a Python program to flatten a shallow list.

import itertools

list_task20 = [[12] , [243] , [2 , 43 , 23] , [23] , [4] , [5] , [6 , 4 , 7]]
merged_task20 = list(itertools.chain(*list_task20))
print("Original list:" , list_task20)
print("Merged list:", merged_task20)