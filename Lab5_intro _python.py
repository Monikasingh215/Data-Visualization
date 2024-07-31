"""Ques 1: Write a function in python to read the content from a text file 
"ABC.txt" line by line and display the same on screen.
"""

def read_file_line_by_line(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())  
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

file_path = 'C:\\crc\\ABC.txt'
read_file_line_by_line(file_path)

"""Ques 2: Write a function in Python to count and display the total number
of words in a text file “ABC.txt”
"""

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

file_path = 'C:\\crc\\ABC.txt'
count_words_in_file(file_path)


""" Ques 3: Write a function in Python to count uppercase character in a text 
    file “ABC.txt”"""
    
def count_uppercase_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            uppercase_count = sum(1 for char in text if char.isupper())
            print(f"Total number of uppercase characters: {uppercase_count}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

file_path = 'C:\\crc\\ABC.txt'
count_uppercase_characters(file_path)

"""Ques 4:Write a function display_words() in python to read lines from a text 
file "story.txt", and display those words, which are less than 4 characters.
"""
def display_words(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                short_words = [word for word in words if len(word) < 4]
                print(' '.join(short_words))
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

f_path="C:\\crc\\story.txt"
display_words(f_path)

#==================================================================================

#Ques 1: Wap to handle ZeroDivisionError exception when dividing by zero
try:
    divisor =int(input("enter the divisor"))
    dividend =int(input("enter the dividend"))
    quotient = divisor/dividend
    print("The result is :",quotient)
except ZeroDivisionError as e:
    print(e)



#Quws 2: Wap that prompts the user to input an integer and raises a ValueErrorException
# if the input is not a valid interger

try:
    num = int(input("Enter an integer: "))
    print(f"You entered: {num}")
except ValueError:
    print("Error: That was not a valid integer.")


"""Ques 3:Write a Python program that opens a file and handles a FileNotFoundError
exception if the file does not exist."""

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

# Usage
open_file('non_existent_file.txt')


"""Ques 4: Write a Python program that prompts the user to input two numbers 
and raises a TypeError exception if the inputs are not numerical
"""

def input_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"You entered: {num1} and {num2}")
    except ValueError:
        print("Error: Both inputs must be numbers.")


input_two_numbers()



