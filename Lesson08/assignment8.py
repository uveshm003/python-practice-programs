"""
Python Scopes and Closures Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
variable scope (local, global, nonlocal) and closures in Python, starting
from fundamental concepts and progressing to more advanced uses. Work
through each section and complete the tasks.
"""

print("--- Python Scopes and Closures Assignment ---")

# --- Section 1: Variable Scope (Local and Global) ---

print("\n--- Section 1: Variable Scope (Local and Global) ---")

# 1.1 Understanding Local Variables:
#    - Define a global variable 'global_value' = 10.
#    - Define a function 'local_scope_example' that declares a local variable
#      also named 'local_value' and prints both the global and local values.
#    - Call 'local_scope_example' and observe the output.

# Your code here:
global_value = 10

def local_scope_example():
    local_value = 5
    print(f"Inside function: global_value = {global_value}, local_value = {local_value}")

local_scope_example()
print(f"Outside function: global_value = {global_value}")

# 1.2 Modifying Global Variables (using 'global' keyword):
#    - Define a global variable 'counter' = 0.
#    - Define a function 'increment_counter' that uses the 'global' keyword to
#      modify the global 'counter' variable.
#    - Call 'increment_counter' twice and then print the value of 'counter'.

# Your code here:
counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
increment_counter()
print(f"Global counter after two increments: {counter}")

# --- Section 2: Variable Scope (Nonlocal) ---

print("\n--- Section 2: Variable Scope (Nonlocal) ---")

# 2.1 Understanding Nonlocal Variables (Nested Functions):
#    - Define an outer function 'outer_function' that has a local variable 'outer_var' = "outer".
#    - Inside 'outer_function', define an inner function 'inner_function' that tries to
#      print 'outer_var'.
#    - Call 'outer_function'. What is the output?

# Your code here:
def outer_function():
    outer_var = "outer"
    def inner_function():
        print(f"Inside inner function: outer_var = {outer_var}")
    inner_function()

outer_function()

# 2.2 Modifying Nonlocal Variables (using 'nonlocal' keyword):
#    - Modify the 'outer_function' from the previous exercise.
#    - Inside 'inner_function', use the 'nonlocal' keyword to modify 'outer_var' to "modified outer".
#    - After calling 'inner_function', print the value of 'outer_var' within 'outer_function'.

# Your code here:
def outer_function_modified():
    outer_var = "outer"
    def inner_function_modified():
        nonlocal outer_var
        outer_var = "modified outer"
        print(f"Inside inner function: outer_var = {outer_var}")
    inner_function_modified()
    print(f"Inside outer function (after inner call): outer_var = {outer_var}")

outer_function_modified()

# --- Section 3: Closures ---

print("\n--- Section 3: Closures ---")

# 3.1 Creating a Basic Closure:
#    - Define an outer function 'multiplier' that takes an argument 'factor'.
#    - Inside 'multiplier', define an inner function 'multiply' that takes an
#      argument 'number' and returns 'number' multiplied by 'factor'.
#    - 'multiplier' should return the 'multiply' function.
#    - Create two closures by calling 'multiplier' with different factors (e.g.,
#      'multiply_by_2' = multiplier(2), 'multiply_by_5' = multiplier(5)).
#    - Call these closures with different numbers and print the results.

# Your code here:
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

multiply_by_2 = multiplier(2)
multiply_by_5 = multiplier(5)

print(f"Multiply 10 by 2: {multiply_by_2(10)}")
print(f"Multiply 3 by 5: {multiply_by_5(3)}")

# 3.2 Understanding Closure Behavior:
#    - In the 'multiplier' example, even after 'multiplier' has finished executing,
#      the 'multiply' function still "remembers" the value of 'factor'. Explain why this happens in a comment.

# Your code here:
# Explanation: This happens because of the concept of closures. When an inner
# function is defined within an outer function, it forms a closure. A closure
# remembers the environment in which it was created. In this case, 'multiply'
# remembers the 'factor' from the 'multiplier' function's scope, even after
# 'multiplier' has returned.

# 3.3 A Meaningful Closure Example (Counter):
#    - Define an outer function 'counter_maker' that initializes a 'count' variable to 0.
#    - Inside 'counter_maker', define an inner function 'increment' that increments
#      'count' (using 'nonlocal') and returns the new 'count'.
#    - 'counter_maker' should return the 'increment' function.
#    - Create two independent counters: 'counter1' = counter_maker(), 'counter2' = counter_maker().
#    - Call each counter multiple times and observe that they maintain their own separate counts.

# Your code here:
def counter_maker():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = counter_maker()
counter2 = counter_maker()

print(f"Counter 1: {counter1()}")  # Output: 1
print(f"Counter 1: {counter1()}")  # Output: 2
print(f"Counter 2: {counter2()}")  # Output: 1
print(f"Counter 1: {counter1()}")  # Output: 3
print(f"Counter 2: {counter2()}")  # Output: 2

# --- Section 4: Advanced Closure Uses (Optional) ---

print("\n--- Section 4: Advanced Closure Uses (Optional) ---")

# 4.1 Closures as Decorators (Introduction):
#    - Define a simple function 'say_hello' that prints "Hello!".
#    - Define an outer function 'make_uppercase' that takes a function 'func' as an argument.
#    - Inside 'make_uppercase', define an inner function 'wrapper' that calls 'func' and
#      then prints " (in uppercase)".
#    - 'make_uppercase' should return 'wrapper'.
#    - Create a decorated version of 'say_hello': 'decorated_hello' = make_uppercase(say_hello).
#    - Call 'decorated_hello' and observe the output. This is a basic example of how closures
#      are used in decorators.

# Your code here:
def say_hello():
    print("Hello!")

def make_uppercase(func):
    def wrapper():
        func()
        print(" (in uppercase)")
    return wrapper

decorated_hello = make_uppercase(say_hello)
decorated_hello()

# 4.2 Closures with Multiple Inner Functions:
#    - Define an outer function 'operation_maker' that takes an 'operator' string ('add' or 'multiply').
#    - Inside 'operation_maker', define two inner functions: 'add' (takes two numbers and returns their sum)
#      and 'multiply' (takes two numbers and returns their product).
#    - 'operation_maker' should return the appropriate inner function based on the 'operator' argument.
#    - Create functions for addition and multiplication using 'operation_maker' and call them.

# Your code here:
def operation_maker(operator):
    def add(a, b):
        return a + b
    def multiply(a, b):
        return a * b

    if operator == 'add':
        return add
    elif operator == 'multiply':
        return multiply
    else:
        return None

add_func = operation_maker('add')
multiply_func = operation_maker('multiply')

if add_func:
    print(f"5 + 3 = {add_func(5, 3)}")
if multiply_func:
    print(f"5 * 3 = {multiply_func(5, 3)}")

print("\n--- End of Python Scopes and Closures Assignment ---")