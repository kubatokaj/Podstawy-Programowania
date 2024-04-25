# Task 1 
# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included.)
list_task1 = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        list_task1.append(str(x))
        print(','.join(list_task1))
# Task 2 
# Write a  Python program to guess a number between 1 and 9.

import random
target_task2, guess_task2 = random.randint(1, 10), 0
while target_task2 != guess_task2:
     guess_task2 = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')
# Task 3
# Write a Python program to construct the following pattern, using a nested for loop.
n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')
for i in range(n, 0, -1):
            for j in range(i):
                print('* ', end="")
            print('')
# Task 4
# Write a Python program that accepts a word from the user and reverses it.
word_task4 = input("Input a word to reverse: ")
for char_task4 in range(len(word_task4) - 1, -1, -1):
    print(word_task4[char_task4], end="")
print("\n")
# Task 5
# Write a Python program to count the number of even and odd numbers in a series of numbers
numbers_task5 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd_task5= 0
count_even_task5 = 0
for x in numbers_task5:
    if not x % 2:
        count_even_task5 += 1
    else:
        count_odd_task5 += 1
        print("Number of even numbers:", count_even_task5)
print("Number of odd numbers:", count_odd_task5)
# Task 6 
# Write a Python program that prints each item and its corresponding type from the following list. 

list_task6 = [1452, 11.23, 1+2j, True, 'task', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for item in list_task6:
    print("Type of", item, "is", type(item))
# Task 7 
# Write a  Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.
for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x, end=' ')
    print("\n")
# Task 8 
# Write a  Python program to get the  Fibonacci series between 0 and 50. 

x, y = 0, 1
while y < 50:
    print(y)
    x, y = y, x + y
# Task 9 
# Write a  Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
list_task9 = []
while True:
    line_task9 = input("Type in line of text: ")
    if line_task9:
         list_task9.append(line_task9.upper())
    else:
        break;
    for line_task9 in list_task9:
        print(line_task9)
# Task 10 
# Write a Python program that accepts a string and calculates the number of digits and letters.
string_task10 = input("Input a string: ")
digits_task10 = letters_task10 = 0
for c in string_task10:
    if c.isdigit():
        digits_task10 = digits_task10 + 1
    elif c.isalpha():
        letters_task10 = letters_task10 + 1
    else:
        pass
print("Letters", letters_task10)
print("Digits", digits_task10)
# Task 11 
# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. 
#The numbers obtained should be printed in a comma-separated sequence.
list_taks11 = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        list_taks11.append(s)
print(",".join(list_taks11))
# Task 12 
# Write a Python program to print the alphabet pattern 'A'.
def print_A(n):
    for i in range(n):
        for j in range((n // 2) + 1):
            if ((j == 0 or j == n // 2) and i != 0 or
                i == 0 and j != 0 and j != n // 2 or
                i == n // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()
height_task12 = 7
print_A(height_task12)
# Task 13 
# Write a Python program to print the alphabet pattern 'T'.
result_string_task13="";    
for row_task13 in range(0,7):    
    for column_task13 in range(0,7):     
        if (column_task13 == 3 or (row_task13 == 0 and column_task13 > 0 and column_task13 <6)):  
            result_string_task13=result_string_task13+"*"    
        else:      
            result_string_task13=result_string_task13+" "    
    result_string_task13=result_string_task13+"\n"    
print(result_string_task13);
# Task 14 
# Write a Python program to calculate a dog's age in dog years. Note: For the first two years, a dog year is equal to 10.5 human years. 
# After that, each dog year equals 4 human years.
human_age_task14 = int(input("Input a dog's age in human years: "))
if human_age_task14 < 0:
    print("Age must be a positive number.")
    exit()
elif human_age_task14 <= 2:
    dog_age_task14 = human_age_task14 * 10.5
else:
    dog_age_task14 = 21 + (human_age_task14 - 2) * 4
print("The dog's age in dog's years is", dog_age_task14)
# Task 15 
# Write a Python program to check whether an alphabet is a vowel or consonant.
letter_task15 = input("Input a letter of the alphabet: ")
if letter_task15 in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % letter_task15)
elif letter_task15 == 'y':
    print("Sometimes the letter y stands for a vowel, sometimes for a consonant.")
else:
    print("%s is a consonant." % letter_task15)
# Task 16 
# Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
def sum(x, y):
    sum_task16 = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum_task16
print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))
# Task 17
# Write a  Python program to check if a triangle is equilateral, isosceles or scalene. Note :An equilateral triangle is a 
# triangle in which all three sides are equal.A scalene triangle is a triangle that has three unequal sides.An isosceles triangle 
# is a triangle with (at least) two equal sides.
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or z == x:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
#Task 18 
# Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
print("Input some integers to calculate their sum and average. Input 0 to exit.: ")
counter_task18 = 0
sum = 0.0
number_task18 = 1
while number_task18 != 0:
    number_task18 = int(input(""))
    sum = sum + number_task18
    counter_task18 += 1
if counter_task18 == 0:
    print("Input some numbers")
else:
    print("Averege of the above numbers is: ", sum / (counter_task18-1),"Sum: ", sum)
# Task 19 
# Write a Python program to create the multiplication table (from 1 to 10) of a number.
number_task19 = int(input("Input a number: "))
for i in range(1, 11):
    print(number_task19, 'x', i, '=', number_task19 * i)
# Task 20
# Write a Python program to construct the following pattern, using a nested loop number.
for i in range(10):
    print(str(i) * i)