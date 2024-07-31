""" Ques 1: Declare a div() function with two parameters. Then call the function
and pass two numbers and display their division."""

def div(a, b):
    return a / b

result = div(10, 2)
print(f"The division of 10 by 2 is {result}.")

""" Ques 2: Declare a square() function with one parameter.Then call the function
and pass one number and display the square of that number ."""

def square(x):
    return x * x

result = square(5)
print(f"The square of 5 is {result}.")

""" Ques 3: Using max() and min() functions display the maximum and minimum of 5
random numbers."""
import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
print(f"Random numbers: {random_numbers}")

maximum = max(random_numbers)
minimum = min(random_numbers)

print(f"The maximum number is {maximum}.")
print(f"The minimum number is {minimum}.")

# Ques 4: Accept a name from the user and display that in lower case using lower() function

name = input("Enter your name: ")

print(f"Your name in lower case is {name.lower()}.")

#==================================================================================

"""Ques 1. Write a Python program to count the occurrences of each word in a  
given sentence
string = “To change the overall look of your document. To change the look
available in the gallery”"""

sentence = "To change the overall look of your document. To change the look available in the gallery"

words = sentence.split()

word_count = {}
for word in words:
    word = word.strip('.').lower() 
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")

""" Ques 2. Write a Python program to remove a newline in Python
String = "\nBest \nDeeptech \nPython \nTraining\n"
"""
string = "\nBest \nDeeptech \nPython \nTraining\n"

string_without_newlines = string.replace("\n", "")

print(f"String without newlines: '{string_without_newlines}'")

""" Ques 3. Write a Python program to reverse words in a string
String = “Deeptech Python Training”"""
string = "Deeptech Python Training"

# Reversing the words
reversed_string = ' '.join(reversed(string.split()))

# Printing the result
print(f"Reversed words: '{reversed_string}'")

""" Ques 4. Write a Python program to count and display the vowels of a given text
String=”Welcome to python Training”  """

string = "Welcome to python Training"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string if char in vowels)

print(f"Total vowels are: {vowel_count}")

#================================================================================
""" Ques 1. Write a Python program to Count all letters, digits, and special
symbols from the given string
Input = “P@#yn26at^&i5ve”
Output: Chars = 8 Digits = 2 Symbol = 3"""
input_string = "P@#yn26at^&i5ve"

chars = digits = symbols = 0

for char in input_string:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")


""" Ques 2. Write a Python program to remove duplicate characters of a given string.
Input = “String and String Function”
"""
input_string = "String and String Function"

output_string = ""
for char in input_string:
    if char not in output_string:
        output_string += char

print(f"Output: {output_string}")

""" Ques 3. Write a Python program to count Uppercase, Lowercase, special
character and numeric values in a given string

Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”

Output:
UpperCase : 5
LowerCase : 18
NumberCase : 5
SpecialCase : 11
"""
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

upper_case = lower_case = number_case = special_case = 0

for char in input_string:
    if char.isupper():
        upper_case += 1
    elif char.islower():
        lower_case += 1
    elif char.isdigit():
        number_case += 1
    else:
        special_case += 1

print(f"UpperCase: {upper_case}")
print(f"LowerCase: {lower_case}")
print(f"NumberCase: {number_case}")
print(f"SpecialCase: {special_case}")


""" Ques 4. Write a Python Count vowels in a string
input= “Welcome to Python Assignment”
Output: Total vowels are: 8
"""
input_string = "Welcome to Python Assignment"

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in input_string if char in vowels)

print(f"Total vowels are: {vowel_count}")
