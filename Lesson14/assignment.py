"""
Python Lambda Functions Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
anonymous functions (lambda functions) in Python, starting from fundamental
concepts and progressing to more advanced uses. Work through each section
and complete the tasks.
"""

print("--- Python Lambda Functions Assignment ---")

# --- Section 1: Basic Lambda Functions ---

print("\n--- Section 1: Basic Lambda Functions ---")

# 1.1 Creating a Simple Lambda Function:
#    - Create a lambda function that takes one argument 'x' and returns 'x + 10'.
#    - Assign this lambda function to a variable named 'add_ten'.
#    - Call the 'add_ten' function with the argument 5 and print the result.

# Your code here:
add_ten = lambda x: x + 10
result1 = add_ten(5)
print(f"Adding 10 to 5 using lambda: {result1}")

# 1.2 Lambda Function with Multiple Arguments:
#    - Create a lambda function that takes two arguments 'a' and 'b' and returns their product.
#    - Assign this lambda function to a variable named 'multiply'.
#    - Call the 'multiply' function with the arguments 4 and 6, and print the result.

# Your code here:
multiply = lambda a, b: a * b
result2 = multiply(4, 6)
print(f"Multiplying 4 and 6 using lambda: {result2}")

# 1.3 Lambda Function with a Conditional Expression:
#   - Create a lambda function called 'get_grade' that takes a score as an argument
#   - Return 'A' if score is 90 or above, 'B' if between 80 and 89, and 'C' otherwise.
#   - Call the function with scores 95, 85, and 75 and print the results.

# Your code here
get_grade = lambda score: 'A' if score >= 90 else ('B' if 80 <= score <= 89 else 'C')

print(f"Grade for 95: {get_grade(95)}")
print(f"Grade for 85: {get_grade(85)}")
print(f"Grade for 75: {get_grade(75)}")

# --- Section 2: Lambda Functions with Built-in Functions ---

print("\n--- Section 2: Lambda Functions with Built-in Functions ---")

# 2.1 Lambda with `map()`:
#    - Create a list of numbers: `numbers = [1, 2, 3, 4, 5]`.
#    - Use the `map()` function along with a lambda function to square each number in the list.
#    - Convert the result to a list and print it.

# Your code here:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers using map and lambda: {squared_numbers}")

# 2.2 Lambda with `filter()`:
#    - Use the `filter()` function along with a lambda function to filter out the even numbers
#      from the `numbers` list.
#    - Convert the result to a list and print it.

# Your code here:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers using filter and lambda: {even_numbers}")

# 2.3 Lambda with `sorted()`:
#    - Create a list of tuples representing students and their scores:
#      `students = [('Alice', 88), ('Bob', 92), ('Charlie', 75), ('David', 90)]`.
#    - Use the `sorted()` function along with a lambda function to sort the list of students
#      based on their scores (the second element of each tuple).
#    - Print the sorted list.

# Your code here:
students = [('Alice', 88), ('Bob', 92), ('Charlie', 75), ('David', 90)]
sorted_students = sorted(students, key=lambda student: student[1])
print(f"Sorted students by score using sorted and lambda: {sorted_students}")

# --- Section 3: Lambda Functions and Scope ---

print("\n--- Section 3: Lambda Functions and Scope ---")

# 3.1 Lambda Functions and Enclosing Scope:
#    - Define a function 'outer_func' that takes an argument 'n'.
#    - Inside 'outer_func', define a lambda function that multiplies its argument by 'n'.
#    - 'outer_func' should return the lambda function.
#    - Create two closures by calling 'outer_func' with different values for 'n' (e.g., 2 and 3).
#    - Call these closures with a number and print the results. Explain how the lambda
#      function "remembers" the value of 'n'.

# Your code here:
def outer_func(n):
    return lambda x: x * n

multiply_by_2 = outer_func(2)
multiply_by_3 = outer_func(3)

print(f"5 multiplied by 2 (using closure): {multiply_by_2(5)}")
print(f"5 multiplied by 3 (using closure): {multiply_by_3(5)}")
# Explanation: The lambda function "remembers" the value of 'n' from the enclosing
# scope of the 'outer_func' due to the concept of closures in Python.

# --- Section 4: Advanced Lambda Function Uses (Optional) ---

print("\n--- Section 4: Advanced Lambda Function Uses (Optional) ---")

# 4.1 Lambda Function as a Key for `max()`:
#   - Given a list of dictionaries:
#     `data = [{'name': 'Alice', 'age': 25, 'city': 'New York'},
#              {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
#              {'name': 'Charlie', 'age': 20, 'city': 'Chicago'}]`
#   - Use the `max()` function and a lambda function to find the dictionary with the maximum age.

# Your code here:
data = [{'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 20, 'city': 'Chicago'}]
oldest_person = max(data, key=lambda person: person['age'])
print(f"Oldest person: {oldest_person}")

# 4.2 Lambda Function with Reduce (from functools):
#    - Import the `reduce` function from the `functools` module.
#    - Use `reduce()` and a lambda function to calculate the product of all numbers in a list:
#      `numbers_for_product = [1, 2, 3, 4, 5]`.

# Your code here:
from functools import reduce
numbers_for_product = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers_for_product)
print(f"Product of numbers using reduce and lambda: {product}")

# 4.3 Combining Lambda Functions:
#   - Create a function `create_multiplier` that takes a number `n` and returns a lambda
#     function that multiplies its input by `n`.
#   - Use this function to create `multiply_by_4` and `multiply_by_5`.
#   - Then, create another lambda function that takes a number `x` and returns the
#     result of `multiply_by_4(x) + multiply_by_5(x)`.
#   - Call this combined lambda function with a number and print the result.

def create_multiplier(n):
    return lambda x: x * n

multiply_by_4 = create_multiplier(4)
multiply_by_5 = create_multiplier(5)

combined_multiplier = lambda x: multiply_by_4(x) + multiply_by_5(x)
result_combined = combined_multiplier(2)
print(f"Combined multiplication result: {result_combined}")

print("\n--- End of Python Lambda Functions Assignment ---")
