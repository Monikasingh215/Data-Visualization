"""Ques 1 : Using input() function take one number from the user and using 
ternary operators check whether the number is even or odd"""

num = int(input("Enter a number: "))

# Using ternary operator to check if the number is even or odd
res = "Even" if num % 2 == 0 else "Odd"
4
print(f"The number {num} is {res}.")

"""Ques 2: Using input function take two number and then swap the number"""
# Taking input from the user
a = int(input("Enter the first number 1: "))
b = int(input("Enter the second number 2: "))

# Swapping the numbers
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")

"""Ques 3: Write a Program to Convert Kilometers to Miles"""

kilometers = float(input("Enter the distance in kilometers: "))

conversion_factor = 0.621371
# Converting kilometers to miles
miles = kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles} miles.")

"""4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year """
# Given values
principal = 200  
rate = 5  
time = 5  

# Calculating simple interest
simple_interest = (principal * rate * time) / 100

# Printing the result
print(f"The Simple Interest on Rs. {principal} for {time} years at {rate}% per year is Rs. {simple_interest}.")
