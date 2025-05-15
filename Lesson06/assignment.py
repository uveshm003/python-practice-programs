"""
Python Functions and Recursion Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
Python functions and recursion, starting from fundamental concepts and
progressing to more advanced uses. Work through each section and complete
the tasks.
"""

print("--- Python Functions and Recursion Assignment ---")

# --- Section 1: Basic Functions ---

print("\n--- Section 1: Basic Functions ---")

# 1.1 Defining and Calling a Simple Function:
def greet():
    print("Hello!")

greet()

# 1.2 Function with a Parameter:
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("User")

# 1.3 Function with a Return Value:
def add_numbers(num1, num2):
    return num1 + num2

sum_result = add_numbers(5, 3)
print(f"The sum is: {sum_result}")

# --- Section 2: Scope and Arguments ---

print("\n--- Section 2: Scope and Arguments ---")

# 2.1 Local vs. Global Scope:
global_var = 10

def modify_var():
    global_var = 5
    print(f"Inside function, local global_var: {global_var}")

modify_var()
print(f"Outside function, global global_var: {global_var}")

# 2.2 Default Argument Values:
def power(base, exponent=2):
    return base ** exponent

result1 = power(4)
result2 = power(3, 3)
print(f"4 raised to the power of default exponent: {result1}")
print(f"3 raised to the power of 3: {result2}")

# 2.3 Keyword Arguments:
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Lucy", animal_type="dog")

# --- Section 3: Recursion ---

print("\n--- Section 3: Recursion ---")

# 3.1 Basic Recursive Function (Factorial):
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

factorial_result = factorial_recursive(5)
print(f"The factorial of 5 (recursive) is: {factorial_result}")

# 3.2 Another Meaningful Recursive Function (Sum of List):
def sum_list_recursive(data_list):
    if not data_list:
        return 0
    else:
        return data_list[0] + sum_list_recursive(data_list[1:])

list_to_sum = [1, 2, 3, 4]
sum_of_list = sum_list_recursive(list_to_sum)
print(f"The sum of the list {list_to_sum} (recursive) is: {sum_of_list}")

# --- Section 4: Advanced Function Concepts (Optional) ---

print("\n--- Section 4: Advanced Function Concepts (Optional) ---")

# 4.1 Anonymous Functions (Lambda):
square_lambda = lambda x: x**2
lambda_result = square_lambda(7)
print(f"The square of 7 (using lambda): {lambda_result}")

# 4.2 Higher-Order Functions (Map):
numbers_to_square = [1, 2, 3, 4, 5]
squared_numbers = list(map(square_lambda, numbers_to_square))
print(f"Squared numbers (using map and lambda): {squared_numbers}")

# 4.3 Recursion with Multiple Recursive Calls (Fibonacci):
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

fibonacci_result = fibonacci_recursive(7)
print(f"The 7th Fibonacci number (recursive) is: {fibonacci_result}")

# --- Section 5: Variable Length Arguments (*args and **kwargs) ---

print("\n--- Section 5: Variable Length Arguments (*args and **kwargs) ---")

# 5.1 Using *args (Arbitrary Positional Arguments):
#    - Define a function 'sum_all' that takes an arbitrary number of positional
#      arguments using *args and returns their sum.
#    - Call 'sum_all' with different numbers of arguments (e.g., sum_all(1, 2, 3), sum_all(10, 20)).

# Your code here:
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

sum1 = sum_all(1, 2, 3)
sum2 = sum_all(10, 20, 30, 40, 50)
print(f"Sum of (1, 2, 3): {sum1}")
print(f"Sum of (10, 20, 30, 40, 50): {sum2}")

# 5.2 Using **kwargs (Arbitrary Keyword Arguments):
#    - Define a function 'describe_user' that takes an arbitrary number of keyword
#      arguments using **kwargs and prints each key-value pair.
#    - Call 'describe_user' with different keyword arguments (e.g.,
#      describe_user(name="Alice", age=30), describe_user(city="Ahmedabad", country="India")).

# Your code here:
def describe_user(**kwargs):
    print("\n--- User Description ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_user(name="Alice", age=30)
describe_user(city="Ahmedabad", country="India", occupation="Engineer")

# 5.3 Combining *args and **kwargs:
#    - Define a function 'process_info' that takes arbitrary positional arguments (*args)
#      and arbitrary keyword arguments (**kwargs).
#    - Print the positional arguments as a tuple and the keyword arguments as a dictionary.
#    - Call 'process_info' with a mix of positional and keyword arguments
#      (e.g., process_info(1, 2, "hello", name="Bob", age=25)).

# Your code here:
def process_info(*args, **kwargs):
    print("\n--- Processed Information ---")
    print(f"Positional arguments (args): {args}")
    print(f"Keyword arguments (kwargs): {kwargs}")

process_info(1, 2, "hello", name="Bob", age=25)

print("\n--- End of Python Functions and Recursion Assignment ---")