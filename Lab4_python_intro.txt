# Ques 1. Write a Python program to sum all the items in a list.
def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total

items = [1, 2, 3, 4, 5]
print("The sum of all items in the list is: ",sum_list(items))

""" Ques 2. Write a Python program to get the largest and smallest number from a
list without builtin functions."""
def largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

numbers = [1, 2, 3, 4, 5]
largest, smallest = largest_smallest(numbers)
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")

# Ques 3.Write a Python program to find duplicate values from a list and display those.

def find_duplicates(lst):
    duplicates = []
    seen = set()
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates

lst = [1, 1, 2, 3, 4, 4, 5, 1]
print(f"Duplicate values in the list are: {find_duplicates(lst)}")

""" Ques 4. Write a Python program to split a given list into two parts where the
length of the first part of the list is given.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splitted the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])"""

def split_list(lst, length):
    return lst[:length], lst[length:]

lst = [1, 1, 2, 3, 4, 4, 5, 1]
first_part, second_part = split_list(lst, 3)
print(f"First part: {first_part}")
print(f"Second part: {second_part}")


""" Ques 5. Write a Python program to traverse a given list in reverse order, and 
print the elements with the original index.
Original list:
['red', 'green', 'white', 'black']
Traverse the said list in reverse order:
black
white
green
red
"""
def traverse_reverse(lst):
    for i in range(len(lst)-1, -1, -1):
        print(f"{lst[i]} (Index: {i})")

# Example usage
lst = ['red', 'green', 'white', 'black']
print("Traverse the list in reverse order:")
traverse_reverse(lst)


#==================================================================================


""" Ques 1. Write a Python program and calculate the mean of the below dictionary.

test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

Output: 6.2
"""
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

mean_value = sum(test_dict.values()) / len(test_dict)
print(f"The mean value is: {mean_value}")


""" Ques 2.Write a Python script to concatenate the following dictionaries to create
a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

concatenated_dict = {**dic1, **dic2, **dic3}
print(f"Concatenated Dictionary: {concatenated_dict}")


""" Ques 3.Write a Python program to get the key, value and item in a dictionary.
input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Output:
Key 	Value
1	10
2	20
3	30
4	40
5	50
6	60
"""
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("Key\tValue")
for key, value in dict_num.items():
    print(f"{key}\t{value}")


""" Ques 4.Write a Python program to get the key, value and item in a dictionary.
Input: input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}
Output:
dict with empty items Dropped :
{1:10,2:40,4:40,6:60}
"""

input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

filtered_dict = {k: v for k, v in input_dict.items() if v is not None}
print(f"Dict with empty items dropped: {filtered_dict}")


 #================================================================================
 
""" Ques 1.Write a Python program to find the number of times 4 appears in the tuple.
Input:
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
Output: 3"""

tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
count_4 = tuplex.count(4)
print(f"The number 4 appears {count_4} times in the tuple.")

""" Ques 2.Write a Python program to convert a list to a tuple.
Input: listx = [5, 10, 7, 4, 15, 3]
Output: (5, 10, 7, 4, 15, 3)
"""
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print(f"The converted tuple is: {tuplex}")

"""
3. Write a Python program to calculate the sum of the numbers in a given tuple.
Input: tuples_list = [(1, 2), (3, 4), (5, 6)]
Output:
sum of tuple is : 21 
"""
tuples_list = [(1, 2), (3, 4), (5, 6)]

sum_of_tuples = sum(sum(t) for t in tuples_list)
print(f"The sum of the tuple is: {sum_of_tuples}")


""" Ques 4.Write a python program and iterate the given tuples
Input:
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

Output:
Employee Records :
Name : John Doe
Employee ID : 101
Department : Human Resources
Salary	:  60000
Name : Alice Smith
Employee ID : 102
Department :Marketing
Salary	:  55000
Name : Bob Johnson
Employee ID : 103
Department : Engineering
Salary	:  75000
"""
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employees = [employee1, employee2, employee3]

print("Employee Records:")
for emp in employees:
    print(f"Name: {emp[0]}")
    print(f"Employee ID: {emp[1]}")
    print(f"Department: {emp[2]}")
    print(f"Salary: {emp[3]}")
    print("")

#====================================================================================

""" Ques 1. Write a Python program to Get Only unique items from two sets.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output:
{70, 40, 10, 50, 20, 60, 30}
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_items = set1.union(set2)
print(f"Unique items from both sets: {unique_items}")


""" Ques2. Write a Python program to Return a set of elements present in Set A or B,
but not both.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output:
{20, 70, 10, 60}
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

symmetric_diff = set1.symmetric_difference(set2)
print(f"Elements present in either set, but not both: {symmetric_diff}")

""" Ques 3. Write a Python program to Check if two sets have any elements in common.
If yes, display the common elements.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
Output:
{10}
"""
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

common_elements = set1.intersection(set2)
print(f"Common elements in both sets: {common_elements}")


""" Ques 3. Write a Python program to Remove items from set1 that are not common to
both set1 and set2.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output:
{40, 50, 30}
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(f"Items common to both sets: {set1}")
