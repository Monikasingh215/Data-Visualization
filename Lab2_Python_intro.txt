# Ques 1: Python program to check leap year

year = int(input("Enter a year: "))

# Checking condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Ques 2: Python Program to Find the Largest Among Three Numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")

#Ques 3: Python Program to Check if a Number is Positive, Negative or 0

number = float(input("Enter a number: "))

# Checking if the number is positive, negative or 0
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

""" Ques 4: A toy vendor supplies three types of toys: Battery Based Toys, Key-based
Toys, and Electrical Charging Based Toys. The vendor gives a discount of
10% on orders for battery-based toys if the order is for more than Rs. 1000.
On orders of more than Rs. 100 for key-based toys, a discount of 5% is
given, and a discount of 10% is given on orders for electrical charging based
toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
are used for battery based toys, key-based toys, and electrical charging based
toys respectively. Write a program that reads the product code and the order
amount and prints out the net amount that the customer is required to pay
after the discount.
"""

product_code = int(input("Enter the product code (1 for Battery Based, 2 for Key-based, 3 for Electrical Charging Based): "))
order_amount = float(input("Enter the order amount: "))

# Applying the discount based on the product code and order amount
if product_code == 1 and order_amount > 1000:
    discount = 0.10
elif product_code == 2 and order_amount > 100:
    discount = 0.05
elif product_code == 3 and order_amount > 500:
    discount = 0.10
else:
    discount = 0

net_amount = order_amount * (1 - discount)

print(f"The net amount to be paid after discount is Rs. {net_amount:.2f}.")

"""Ques 5: A transport company charges the fare according to following table:
Distance Charges
1-50 8 Rs./Km
51-100 10 Rs./Km
> 100 12 Rs/Km
"""

distance = float(input("Enter the distance traveled in kilometers: "))

if 1 <= distance <= 50:
    fare = distance * 8
elif 51 <= distance <= 100:
    fare = (50 * 8) + ((distance - 50) * 10)
else:
    fare = (50 * 8) + (50 * 10) + ((distance - 100) * 12)

print(f"The total fare for traveling {distance} kilometers is Rs. {fare:.2f}.")

#Ques 6: Write a python program to reverse a number using a while loop.

number = int(input("Enter a number: "))
reversed_number = 0

while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10

print(f"The reversed number is {reversed_number}.")

#Ques 7: Write a python program to check whether a number is palindrome or not?

number = int(input("Enter a number: "))
original_number = number
reversed_number = 0

while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10

if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")

#Ques 8: Write a python program finding the factorial of a given number using a while loop.

number = int(input("Enter a number: "))
fact = 1
i = number
while i > 0:
    fact *= i
    i -= 1

print(f"The factorial of {number} is {fact}.")

"""9. Accept numbers using input() function until the user enters 0. If user
input 0 then break the while loop and display the sum of all the numbers."""

total_sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number

print(f"The sum of all the numbers entered is {total_sum}.")

#10. Print the first 10 natural numbers using for loop
# Printing the first 10 natural numbers using a for loop
for i in range(1, 11):
    print(i)

#11. Python program to check if the given string is a palindrome

string = input("Enter a string: ")

if string == string[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

#12. Python program to check if a given number is an Armstrong number

number = int(input("Enter a number: "))
sum_of_cubes = sum(int(digit)**3 for digit in str(number))

if number == sum_of_cubes:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

#13. Python program to get the Fibonacci series between 0 to 50
a, b = 0, 1

while a <= 50:
    print(a, end=" ")
    a, b = b, a + b
print()

#14. Python program to check the validity of password input by users

def check_password_validity(password):
    # Initialize flags for password criteria
    has_lower = has_upper = has_digit = has_special = False
    special_characters = "@#$%^&+="

    # Check the length of the password
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Check each character in the password
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Validate all criteria
    if not has_lower:
        return "Password must contain at least one lowercase letter."
    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_digit:
        return "Password must contain at least one digit."
    if not has_special:
        return "Password must contain at least one special character (@#$%^&+=)."

    return "Password is valid."

password = input("Enter a password: ")

result = check_password_validity(password)

print(result)


