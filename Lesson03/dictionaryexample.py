"""
Python Dictionaries Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
Python dictionaries, starting from fundamental concepts and progressing to more
advanced uses. Work through each section and complete the tasks.
"""

print("--- Python Dictionaries Assignment ---")

# --- Section 1: Introduction to Dictionaries ---

print("\n--- Section 1: Introduction to Dictionaries ---")

# 1.1 Creating Dictionaries:
#    - Create an empty dictionary named 'empty_dict'.
#    - Create a dictionary named 'student' with the keys 'name', 'age', and 'grade',
#      and assign appropriate values.
#    - Create a dictionary named 'item_prices' using keyword arguments with keys
#      'apple', 'banana', and 'cherry' and their respective prices (e.g., apple=1.0).

# Your code here:
empty_dict = {}
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
item_prices = dict(apple=1.0, banana=0.5, cherry=2.5)

print(f"Empty dictionary: {empty_dict}")
print(f"Student dictionary: {student}")
print(f"Item prices dictionary: {item_prices}")

# 1.2 Dictionary Mutability:
#    - Change the 'age' of the 'student' to 21.
#    - Add a new key-value pair 'city': 'Ahmedabad' to the 'student' dictionary.
#    - Print the modified 'student' dictionary.

# Your code here:
student['age'] = 21
student['city'] = 'Ahmedabad'

print(f"Modified student dictionary: {student}")

# --- Section 2: Accessing Dictionary Elements ---

print("\n--- Section 2: Accessing Dictionary Elements ---")

# 2.1 Accessing Values using Keys:
#    - Access and print the 'name' of the 'student'.
#    - Access and print the price of 'banana' from 'item_prices'.

# Your code here:
student_name = student['name']
banana_price = item_prices['banana']

print(f"Student's name: {student_name}")
print(f"Price of banana: {banana_price}")

# 2.2 Using the `get()` method:
#    - Try to access a key that doesn't exist in 'student' (e.g., 'major') using direct access.
#    - Now, try to access the same key using the `get()` method and provide a default value of 'Unknown'.
#    - Access the 'age' from 'student' using the `get()` method without a default value.
#    - Print the results and explain the difference in behavior.

# Your code here:
try:
    major_direct = student['major']
    print(f"Major (direct access): {major_direct}")
except KeyError as e:
    print(f"\nError (direct access): Key '{e}' not found.")

major_get = student.get('major', 'Unknown')
age_get = student.get('age')

print(f"Major (using get()): {major_get}")
print(f"Age (using get()): {age_get}")
# Explanation: Direct access using square brackets raises a KeyError if the key
# is not found. The `get()` method returns None (or a specified default value)
# if the key is not found, preventing the error.

# --- Section 3: Dictionary Operations ---

print("\n--- Section 3: Dictionary Operations ---")

# 3.1 Adding and Updating Elements:
#    - Add a new item 'grape' with a price of 3.0 to 'item_prices'.
#    - Update the price of 'apple' in 'item_prices' to 1.2.

# Your code here:
item_prices['grape'] = 3.0
item_prices['apple'] = 1.2

print(f"Updated item prices: {item_prices}")

# 3.2 Removing Elements:
#    - Remove the 'age' key-value pair from the 'student' dictionary using `del`.
#    - Remove the 'banana' key-value pair from 'item_prices' using the `pop()` method and print the removed value.
#    - Try to remove a non-existent key ('orange') from 'item_prices' using `pop()` and handle the potential KeyError by providing a default value (e.g., None).

# Your code here:
del student['age']
print(f"Student dictionary after deleting 'age': {student}")

removed_banana_price = item_prices.pop('banana')
print(f"Removed 'banana' with price: {removed_banana_price}, updated item prices: {item_prices}")

removed_orange_price = item_prices.pop('orange', None)
print(f"Removed 'orange' (if present): {removed_orange_price}, updated item prices: {item_prices}")

# --- Section 4: Dictionary Views ---

print("\n--- Section 4: Dictionary Views ---")

# 4.1 `keys()`:
#    - Get a view object of all keys in the 'student' dictionary.
#    - Convert this view object to a list and print it.

# Your code here:
student_keys_view = student.keys()
student_keys_list = list(student_keys_view)
print(f"Keys of student dictionary: {student_keys_list}")

# 4.2 `values()`:
#    - Get a view object of all values in the 'item_prices' dictionary.
#    - Iterate through this view object and print each price.

# Your code here:
item_prices_values_view = item_prices.values()
print("Prices in item_prices:")
for price in item_prices_values_view:
    print(price)

# 4.3 `items()`:
#    - Get a view object of all key-value pairs in the 'student' dictionary.
#    - Iterate through this view object and print each key and its corresponding value.

# Your code here:
student_items_view = student.items()
print("\nItems in student dictionary:")
for key, value in student_items_view:
    print(f"{key}: {value}")

# --- Section 5: Dictionary Methods ---

print("\n--- Section 5: Dictionary Methods ---")

# 5.1 `update()`:
#    - Create a new dictionary 'additional_info' = {'major': 'Computer Science', 'gpa': 3.8}.
#    - Update the 'student' dictionary with the key-value pairs from 'additional_info'.
#    - Create another dictionary 'new_prices' = {'grape': 3.2, 'mango': 2.0}.
#    - Update the 'item_prices' dictionary with 'new_prices'.

# Your code here:
additional_info = {'major': 'Computer Science', 'gpa': 3.8}
student.update(additional_info)
print(f"Student dictionary after update: {student}")

new_prices = {'grape': 3.2, 'mango': 2.0}
item_prices.update(new_prices)
print(f"Item prices after update: {item_prices}")

# 5.2 `popitem()`:
#    - While the 'item_prices' dictionary is not empty, remove and print the last inserted key-value pair using `popitem()`.

# Your code here:
print("\nRemoving items from item_prices (last in, first out):")
while item_prices:
    last_item = item_prices.popitem()
    print(f"Removed: {last_item}")
print(f"Final item prices: {item_prices}")

# 5.3 `setdefault()`:
#    - Create a dictionary 'word_counts' = {'the': 5, 'quick': 2}.
#    - Use `setdefault()` to get the count of 'the'.
#    - Use `setdefault()` to get the count of 'fox'. If 'fox' is not present, set its count to 0 and return 0.
#    - Print the 'word_counts' dictionary after these operations.

# Your code here:
word_counts = {'the': 5, 'quick': 2}
count_the = word_counts.setdefault('the')
count_fox = word_counts.setdefault('fox', 0)

print(f"\nCount of 'the': {count_the}")
print(f"Count of 'fox': {count_fox}")
print(f"Updated word counts: {word_counts}")

# --- Section 6: Dictionary Comprehension ---

print("\n--- Section 6: Dictionary Comprehension ---")

# 6.1 Basic Dictionary Comprehension:
#    - Use dictionary comprehension to create a new dictionary 'square_numbers' where keys are numbers from 1 to 5,
#      and values are their squares.

# Your code here:
square_numbers = {x: x**2 for x in range(1, 6)}
print(f"Square numbers: {square_numbers}")

# 6.2 Dictionary Comprehension with Condition:
#    - Given a list of names 'names' = ['Alice', 'Bob', 'Charlie', 'David'], use dictionary comprehension
#      to create a dictionary 'name_lengths' where keys are names and values are their lengths, but only for names
#      with a length greater than 4.

# Your code here:
names = ['Alice', 'Bob', 'Charlie', 'David']
name_lengths = {name: len(name) for name in names if len(name) > 4}
print(f"Name lengths (length > 4): {name_lengths}")

# 6.3 Swapping Keys and Values (with unique values):
#    - Given the dictionary 'student_grades' = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'},
#      use dictionary comprehension to create a new dictionary 'grade_students' where keys are grades
#      and values are the corresponding students. Assume grades are unique.

# Your code here:
student_grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}
grade_students = {grade: student for student, grade in student_grades.items()}
print(f"Students by grade: {grade_students}")

# --- Section 7: Advanced Dictionary Uses (Optional) ---

print("\n--- Section 7: Advanced Dictionary Uses (Optional) ---")

# 7.1 Merging Dictionaries:
#    - Create two dictionaries 'dict1' = {'a': 1, 'b': 2} and 'dict2' = {'b': 3, 'c': 4}.
#    - Merge these two dictionaries into a new dictionary 'merged_dict'. If there are common keys,
#      the values from 'dict2' should take precedence (using the `**` operator).

# Your code here:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(f"Merged dictionary: {merged_dict}")

# 7.2 Using Dictionaries for Counting:
#    - Given a string 'text' = "this is a sample text with some repeated words this is".
#    - Use a dictionary to count the occurrences of each word in the text (case-sensitive).
#    - Print the word counts.

# Your code here:
text = "this is a sample text with some repeated words this is"
word_counts_from_text = {}
words = text.split()
for word in words:
    word_counts_from_text[word] = word_counts_from_text.get(word, 0) + 1
print(f"\nWord counts from text: {word_counts_from_text}")

# 7.3 Using `collections.defaultdict`:
#    - Import `defaultdict` from the `collections` module.
#    - Given a list of items 'items' = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple'],
#      use `defaultdict(int)` to count the occurrences of each item.
#    - Print the counts.

# Your code here:
from collections import defaultdict

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
item_counts = defaultdict(int)
for item in items:
    item_counts[item] += 1
print(f"\nItem counts (using defaultdict): {item_counts}")

print("\n--- End of Python Dictionaries Assignment ---")