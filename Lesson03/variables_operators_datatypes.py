"""
Python Variables, Datatypes, and Operators Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
Python variables, fundamental datatypes, and various operators, starting
from basic concepts and progressing to more advanced uses. Work through
each section and complete the tasks.
"""

print("--- Python Variables, Datatypes, and Operators Assignment ---")

# --- Section 1: Variables and Basic Datatypes ---

print("\n--- Section 1: Variables and Basic Datatypes ---")

# 1.1 Variable Assignment:
#    - Assign the integer value 10 to a variable named 'number'.
#    - Assign the string value "Hello, Python!" to a variable named 'message'.
#    - Assign the floating-point value 3.14 to a variable named 'pi_value'.
#    - Assign the boolean value True to a variable named 'is_python_fun'.

# Your code here:
number = 10
message = "Hello, Python!"
pi_value = 3.14
is_python_fun = True

print(f"Number: {number}")
print(f"Message: {message}")
print(f"Pi Value: {pi_value}")
print(f"Is Python Fun? {is_python_fun}")

# 1.2 Checking Datatypes:
#    - Use the `type()` function to print the datatype of each of the variables created above.

# Your code here:
print(f"Type of 'number': {type(number)}")
print(f"Type of 'message': {type(message)}")
print(f"Type of 'pi_value': {type(pi_value)}")
print(f"Type of 'is_python_fun': {type(is_python_fun)}")

# --- Section 2: Basic Operators ---

print("\n--- Section 2: Basic Operators ---")

# 2.1 Arithmetic Operators:
#    - Create two variables, 'num1' with the value 20 and 'num2' with the value 5.
#    - Perform the following operations and print the results:
#      - Addition (+)
#      - Subtraction (-)
#      - Multiplication (*)
#      - Division (/)
#      - Floor Division (//)
#      - Modulo (%)
#      - Exponentiation (**)

# Your code here:
num1 = 20
num2 = 5

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")

# 2.2 Assignment Operators:
#    - Initialize a variable 'count' to 0.
#    - Use the following assignment operators to modify 'count' and print its value after each operation:
#      - `+= 5`
#      - `-= 2`
#      - `*= 3`
#      - `/= 2`
#      - `//= 2`
#      - `%= 3`
#      - `**= 2`

# Your code here:
count = 0
print(f"Initial count: {count}")
count += 5
print(f"count += 5: {count}")
count -= 2
print(f"count -= 2: {count}")
count *= 3
print(f"count *= 3: {count}")
count /= 2
print(f"count /= 2: {count}")
count //= 2
print(f"count //= 2: {count}")
count %= 3
print(f"count %= 3: {count}")
count **= 2
print(f"count **= 2: {count}")

# --- Section 3: Comparison Operators ---

print("\n--- Section 3: Comparison Operators ---")

# 3.1 Comparison Operations:
#    - Create two variables, 'val1' with the value 15 and 'val2' with the value 15.
#    - Perform the following comparisons and print the boolean results:
#      - Equal to (==)
#      - Not equal to (!=)
#      - Greater than (>)
#      - Less than (<)
#      - Greater than or equal to (>=)
#      - Less than or equal to (<=)

# Your code here:
val1 = 15
val2 = 15

print(f"{val1} == {val2}: {val1 == val2}")
print(f"{val1} != {val2}: {val1 != val2}")
print(f"{val1} > {val2}: {val1 > val2}")
print(f"{val1} < {val2}: {val1 < val2}")
print(f"{val1} >= {val2}: {val1 >= val2}")
print(f"{val1} <= {val2}: {val1 <= val2}")

# --- Section 4: Logical Operators ---

print("\n--- Section 4: Logical Operators ---")

# 4.1 Logical Operations:
#    - Create two boolean variables, 'condition1' with the value True and 'condition2' with the value False.
#    - Perform the following logical operations and print the boolean results:
#      - Logical AND (and)
#      - Logical OR (or)
#      - Logical NOT (not) applied to 'condition1'

# Your code here:
condition1 = True
condition2 = False

print(f"{condition1} and {condition2}: {condition1 and condition2}")
print(f"{condition1} or {condition2}: {condition1 or condition2}")
print(f"not {condition1}: {not condition1}")

# --- Section 5: String Datatype and Operators ---

print("\n--- Section 5: String Datatype and Operators ---")

# 5.1 String Concatenation:
#    - Create two string variables, 'first_name' with "John" and 'last_name' with "Doe".
#    - Concatenate them with a space in between to create a 'full_name' variable and print it.

# Your code here:
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")

# 5.2 String Repetition:
#    - Create a string 'greeting' with "Hello".
#    - Repeat the 'greeting' three times and print the result.

# Your code here:
greeting = "Hello"
repeated_greeting = greeting * 3
print(f"Repeated Greeting: {repeated_greeting}")

# --- Section 6: List and Tuple Datatypes (Introduction) ---

print("\n--- Section 6: List and Tuple Datatypes (Introduction) ---")

# 6.1 Creating Lists and Tuples:
#    - Create a list named 'my_list' containing the numbers 1, 2, 3.
#    - Create a tuple named 'my_tuple' containing the strings 'a', 'b', 'c'.
#    - Print both the list and the tuple.

# Your code here:
my_list = [1, 2, 3]
my_tuple = ('a', 'b', 'c')

print(f"My List: {my_list}")
print(f"My Tuple: {my_tuple}")

# 6.2 Accessing Elements (Basic):
#    - Print the first element of 'my_list'.
#    - Print the second element of 'my_tuple'.

# Your code here:
first_element_list = my_list[0]
second_element_tuple = my_tuple[1]

print(f"First element of my_list: {first_element_list}")
print(f"Second element of my_tuple: {second_element_tuple}")

# --- Section 7: Advanced Concepts (Type Conversion and Operator Precedence) ---

print("\n--- Section 7: Advanced Concepts (Type Conversion and Operator Precedence) ---")

# 7.1 Type Conversion:
#    - You have a string 'num_str' = "123" and an integer 'factor' = 2.
#    - Convert 'num_str' to an integer and multiply it by 'factor'. Print the result.
#    - You have a float 'float_num' = 3.7 and you want to convert it to an integer. Print the result.
#    - You have an integer 'int_num' = 5 and you want to convert it to a string. Print the result.

# Your code here:
num_str = "123"
factor = 2
result_int_mult = int(num_str) * factor
print(f"Integer conversion and multiplication: {result_int_mult}")

float_num = 3.7
result_int_conv = int(float_num)
print(f"Float to integer conversion: {result_int_conv}")

int_num = 5
result_str_conv = str(int_num)
print(f"Integer to string conversion: {result_str_conv}, Type: {type(result_str_conv)}")

# 7.2 Operator Precedence:
#    - Evaluate the following expressions manually and then print the Python result to verify:
#      - `10 + 2 * 3`
#      - `(10 + 2) * 3`
#      - `2 ** 3 + 1`
#      - `2 ** (3 + 1)`
#      - `5 + 10 / 2 - 1`

# Your code here:
expression1 = 10 + 2 * 3
expression2 = (10 + 2) * 3
expression3 = 2 ** 3 + 1
expression4 = 2 ** (3 + 1)
expression5 = 5 + 10 / 2 - 1

print(f"10 + 2 * 3 = {expression1}")
print(f"(10 + 2) * 3 = {expression2}")
print(f"2 ** 3 + 1 = {expression3}")
print(f"2 ** (3 + 1) = {expression4}")
print(f"5 + 10 / 2 - 1 = {expression5}")

print("\n--- End of Python Variables, Datatypes, and Operators Assignment ---")