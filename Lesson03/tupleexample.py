"""
Python Tuple Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
Python tuples, starting from fundamental concepts and progressing to more
advanced uses. Work through each section and complete the tasks.
"""

print("--- Python Tuples Assignment ---")

# --- Section 1: Introduction to Tuples ---

print("\n--- Section 1: Introduction to Tuples ---")

# 1.1 Creating Tuples:
#    - Create an empty tuple named 'empty_tuple'.
#    - Create a tuple named 'my_tuple' containing the elements 10, 20, 30.
#    - Create a tuple named 'mixed_tuple' containing an integer, a string, and a boolean.
#    - Create a tuple named 'single_element_tuple' containing only the number 5.
#      (Remember the special syntax for a single-element tuple!)

# Your code here:
empty_tuple = ()
my_tuple = (10, 20, 30)
mixed_tuple = (100, "hello", True)
single_element_tuple = (5,)  # Important: comma is needed

print(f"Empty tuple: {empty_tuple}")
print(f"My tuple: {my_tuple}")
print(f"Mixed tuple: {mixed_tuple}")
print(f"Single element tuple: {single_element_tuple}")

# 1.2 Tuple Immutability:
#    - Try to change the first element of 'my_tuple' to 15.
#    - What happens? Explain the error you encounter in a comment.

# Your code here:
try:
    my_tuple[0] = 15
except TypeError as e:
    print(f"\nError encountered while trying to modify tuple: {e}")
    # Explanation: Tuples are immutable, meaning their elements cannot be changed
    # after the tuple is created. Attempting to assign a new value to an element
    # at a specific index raises a TypeError.

# --- Section 2: Accessing Tuple Elements ---

print("\n--- Section 2: Accessing Tuple Elements ---")

# 2.1 Indexing:
#    - Access and print the second element of 'my_tuple'.
#    - Access and print the last element of 'mixed_tuple' using negative indexing.

# Your code here:
second_element_my_tuple = my_tuple[1]
last_element_mixed_tuple = mixed_tuple[-1]

print(f"Second element of my_tuple: {second_element_my_tuple}")
print(f"Last element of mixed_tuple: {last_element_mixed_tuple}")

# 2.2 Slicing:
#    - Create a new tuple 'slice_tuple' containing the first two elements of 'my_tuple'.
#    - Create another tuple 'reverse_tuple' containing 'my_tuple' in reverse order using slicing.

# Your code here:
slice_tuple = my_tuple[0:2]
reverse_tuple = my_tuple[::-1]

print(f"Slice of my_tuple (first two elements): {slice_tuple}")
print(f"Reversed my_tuple: {reverse_tuple}")

# --- Section 3: Tuple Operations ---

print("\n--- Section 3: Tuple Operations ---")

# 3.1 Concatenation:
#    - Create two tuples: 'tuple1' with (1, 2) and 'tuple2' with (3, 4).
#    - Concatenate 'tuple1' and 'tuple2' to create a new tuple 'combined_tuple'.

# Your code here:
tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2

print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Combined tuple: {combined_tuple}")

# 3.2 Repetition:
#    - Create a tuple 'repeat_tuple' by repeating 'tuple1' three times.

# Your code here:
repeat_tuple = tuple1 * 3

print(f"Repeated tuple: {repeat_tuple}")

# 3.3 Membership:
#    - Check if the number 20 is present in 'my_tuple'. Print the boolean result.
#    - Check if the string "world" is present in 'mixed_tuple'. Print the boolean result.

# Your code here:
is_20_present = 20 in my_tuple
is_world_present = "world" in mixed_tuple

print(f"Is 20 present in my_tuple? {is_20_present}")
print(f"Is 'world' present in mixed_tuple? {is_world_present}")

# --- Section 4: Tuple Functions and Methods ---

print("\n--- Section 4: Tuple Functions and Methods ---")

# 4.1 `len()` function:
#    - Find and print the number of elements in 'combined_tuple'.

# Your code here:
length_combined_tuple = len(combined_tuple)
print(f"Length of combined_tuple: {length_combined_tuple}")

# 4.2 `count()` method:
#    - Count and print the number of times the number 2 appears in the tuple '(1, 2, 2, 3, 2, 4)'.

# Your code here:
count_of_2 = (1, 2, 2, 3, 2, 4).count(2)
print(f"Count of 2 in the tuple: {count_of_2}")

# 4.3 `index()` method:
#    - Find and print the index of the first occurrence of the number 20 in 'my_tuple'.

# Your code here:
index_of_20 = my_tuple.index(20)
print(f"Index of 20 in my_tuple: {index_of_20}")

# --- Section 5: Tuple Unpacking ---

print("\n--- Section 5: Tuple Unpacking ---")

# 5.1 Basic Unpacking:
#    - Given the tuple 'point' = (5, 10), unpack its elements into variables 'x' and 'y'.
#    - Print the values of 'x' and 'y'.

# Your code here:
point = (5, 10)
x, y = point
print(f"x: {x}, y: {y}")

# 5.2 Unpacking with Ignoring Elements:
#    - Given the tuple 'data' = ('John', 30, 'New York'), unpack it into 'name' and 'city',
#      ignoring the age. Use the underscore '_' for the element to be ignored.

# Your code here:
data = ('John', 30, 'New York')
name, _, city = data
print(f"Name: {name}, City: {city}")

# 5.3 Unpacking with `*args`:
#    - Given the tuple 'numbers' = (1, 2, 3, 4, 5), unpack the first element into 'first',
#      the last element into 'last', and the remaining elements into a list called 'middle'.

# Your code here:
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# --- Section 6: Tuples and Other Data Structures ---

print("\n--- Section 6: Tuples and Other Data Structures ---")

# 6.1 Tuples in Lists:
#    - Create a list named 'list_of_tuples' containing three tuples, each representing
#      a point with (x, y) coordinates.
#    - Iterate through the list and print the coordinates of each point.

# Your code here:
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
print("Coordinates in list_of_tuples:")
for point in list_of_tuples:
    print(f"x: {point[0]}, y: {point[1]}")

# 6.2 Converting List to Tuple and Vice Versa:
#    - Create a list 'my_list' = [100, 200, 300]. Convert it to a tuple named 'tuple_from_list'.
#    - Create a tuple 'my_other_tuple' = ('apple', 'banana', 'cherry'). Convert it to a list named 'list_from_tuple'.

# Your code here:
my_list = [100, 200, 300]
tuple_from_list = tuple(my_list)
my_other_tuple = ('apple', 'banana', 'cherry')
list_from_tuple = list(my_other_tuple)

print(f"Tuple from list: {tuple_from_list}")
print(f"List from tuple: {list_from_tuple}")

# --- Section 7: Advanced Tuple Uses (Optional) ---

print("\n--- Section 7: Advanced Tuple Uses (Optional) ---")

# 7.1 Named Tuples (using `collections.namedtuple`):
#    - Import the `namedtuple` factory function from the `collections` module.
#    - Create a named tuple called 'Person' with fields 'name', 'age', and 'city'.
#    - Create an instance of 'Person' named 'person1' with the values ('Alice', 25, 'London').
#    - Access and print the name and age of 'person1' using both attribute access and index access.

# Your code here:
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
person1 = Person('Alice', 25, 'London')

print(f"Person 1 (attribute access): Name: {person1.name}, Age: {person1.age}")
print(f"Person 1 (index access): Name: {person1[0]}, Age: {person1[1]}")

# 7.2 Tuples as Dictionary Keys:
#    - Create a dictionary where the keys are tuples representing (country, city) pairs,
#      and the values are the population of that city.
#    - Add at least three entries to the dictionary.
#    - Iterate through the dictionary and print each (country, city) pair and its population.

# Your code here:
city_populations = {
    ('USA', 'New York'): 8419000,
    ('India', 'Mumbai'): 12442000,
    ('Japan', 'Tokyo'): 13929000
}

print("\nCity Populations:")
for (country, city), population in city_populations.items():
    print(f"({country}, {city}): {population}")

print("\n--- End of Python Tuples Assignment ---")