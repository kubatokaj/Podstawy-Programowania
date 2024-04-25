# Task 1
# Write a Python program to calculate the length of a string.
string_task1 = "Hello World"
print(len(string_task1))

# Task 2
# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
def swap_task2(string1_task2, string2_task2):
   new_string1_task2 = string2_task2[:2] + string1_task2[2:]
   new_string2_task2 = string1_task2[:2] + string2_task2[2:]
   return new_string1_task2 + " " + new_string2_task2

print(swap_task2("abc", "xyz"))

# Task 3
#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing', add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
def add_string_task3(string_task3):
   len_task3 = len(string_task3)
   if len_task3 > 2:
      if string_task3[-3:] == "ing":
         string_task3 += "ly"
      else :
         string_task3 += "ing"
   return string_task3

print (add_string_task3("si"))
print (add_string_task3("singing"))
print (add_string_task3("sing"))

# Task 4
#Write a Python script that takes input from the user and displays that input back in upper and lower cases.

user_input_task_4 = input("What is your favorite color? ")
print(user_input_task_4.upper())
print(user_input_task_4.lower())

# Task 5
# Write a Python function to get a string made of 4 copies of the last two characters of a specified string 
# (length must be at least 2).
def last_two_copy(string_task5):
   if len(string_task5) > 1:
      new_string_task5 = string_task5 [-2:]
      
   return new_string_task5 * 4
print(last_two_copy("banana"))

# Task 6
# Write a Python function to get a string made of the first three characters of a specified string. 
# If the length of the string is less than 3, return the original string.
def first_three(string_task6):
   if len(string_task6) < 3:
      return string_task6
   else:
      new_string_task6 = string_task6[:3]
      return new_string_task6
   
print(first_three("Banana"))
print(first_three("Ba"))

# Task 7
# Write a Python program to check whether a string starts with specified characters.
string_task7 = "Monkey"
print("String: ",string_task7)
letter_task7 = input ("Type in letter to check if string starts with this characters: ")

print(string_task7.startswith(letter_task7))

# Task 8
#Write a Python program to display formatted text (width=50) as output.
import textwrap
text_taks8 = "Text with which uses textwap library to set the width of the text to 50 (first one is normal without width)"
print(text_taks8)
print(textwrap.fill(text_taks8, width=50))

# Task 9
def reverse(string_task9):
   return "" .join(reversed(string_task9))

print("Normal string")
print(reverse("Normal string"))

#Task 10
# Write a Python program to lowercase the first n characters in a string.
string_task10 = "WWWXXX"
print(string_task10[:3].lower() + string_task10[3:])

# Task 11
#Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
# If the string length is less than 2, return the empty string instead.
def two_first_two_last(string_task_11):
   if len(string_task_11) < 2:
      return ""
   else:
      return string_task_11[0:2] + string_task_11[-2:]
   
print(two_first_two_last("TestString"))
print(two_first_two_last("T"))
print("Emptry strning should be above")

# Task 12
# Write a Python program to remove spaces from a given string.
def remove_space_task12(string_task12):
   string_task12 = string_task12.replace(" ", "")
   return string_task12

print(remove_space_task12("Text With Removec Spaces"))

# Task 13
#Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.
def count_chars(string_task13):

  upper_task13, lower_task13, number_task13, special_task13 = 0, 0, 0, 0

  for i in range(len(string_task13)):

    if string_task13[i] >= 'A' and string_task13[i] <= 'Z':
      upper_task13 += 1
    elif string_task13[i] >= 'a' and string_task13[i] <= 'z':
      lower_task13 += 1
    elif string_task13[i] >= '0' and string_task13[i] <= '9':
      number_task13 += 1
    else:
      special_task13 += 1

  return upper_task13, lower_task13, number_task13, special_task13

string_task13 = "Wsacv342#$wsaf!@#asdASFD"
 
print("Original Substrings:",string_task13)

u, l, n, s = count_chars(string_task13)

print('\nUpper case characters: ',u) 
print('Lower case characters: ',l)
print('Number case: ',n)
print('Special case characters: ',s)

# Task 14
# Write a Python program to print four integer values - decimal, octal, hexadecimal (capitalized), binary - in a single line.
int_task14 = int(input("Input an integer: "))

octal_task14 = str(oct(int_task14))[2:]
	
hex_task14 = str(hex(int_task14))[2:].upper()

binary_task14 = str(bin(int_task14))[2:]

decimal_task14 = str(int_task14)

print("Decimal:" ,decimal_task14, "Octal:", octal_task14, "Hexadecimal (capitalized):", hex_task14, "Binary:", binary_task14)

# Task 15
# Write a Python program to delete all occurrences of a specified character in a given string.
def delete_all_occurance(string_task15, char_task15):
   new_string_task15 = string_task15.replace(char_task15, "")
   return new_string_task15

string1_task15 = "Delete all occurrences of letter o in this messege"
print("Original string: ",  string1_task15)
char_task15 = "o"
print("Modified string below:")
print(delete_all_occurance(string1_task15,char_task15))

# Task 16 
# Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).

string_task16 = input("Input comma-separated sequence of words: ")
words_task16 = [word_task16 for word_task16 in string_task16.split(",")]
print(",".join(sorted(list(set(words_task16)))))

#Task 17
# Write a Python function to reverse a string if its length is a multiple of 4.
def reverse_string(string_task17):
    if len(string_task17) % 4 == 0:
        return ''.join(reversed(string_task17))
    
    return string_task17

print(reverse_string('test'))   
print(reverse_string('Python')) 

# Task 18
# Write a Python program to format a number with a percentage.

task18 = 0.25
task18_1 = -0.25
print("Original Number: ", task18)
print("Formatted Number with percentage: "+"{:.2%}".format(task18))
print("Original Number: ", task18_1)
print("Formatted Number with percentage: "+"{:.2%}".format(task18_1))

# Task 19
# Write a Python program to convert a given string into a list of words.

string_task19 = "This is a test string."
print(string_task19.split(' '))
string_task19_1 = "This-is-second-test-string."
print(string_task19_1.split('-'))

#Task 20
# Write a Python program to add two strings as if they were numbers (positive integer values). Return a message if the numbers are strings.

def test(number1_task20, number2_task20):
    number1_task20, number2_task20 = '0' + number1_task20, '0' + number2_task20
    if (number1_task20.isnumeric() and number2_task20.isnumeric()):
        return str(int(number1_task20) + int (number2_task20))
    else:
        return 'Error in input!'

# Test the function with different input strings and print the results
print(test("10", "53"))
print(test("32", "22.6"))
print(test("1003", "-200")) 
