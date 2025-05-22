"""
Python Exceptions Handling Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
exception handling in Python, including `try-except`, `else`, `finally`,
raising exceptions, and creating custom exceptions. Work through each section
and complete the tasks.
"""

print("--- Python Exceptions Handling Assignment ---")

# --- Section 1: Basic Try-Except ---

print("\n--- Section 1: Basic Try-Except ---")

# 1.1 Catching a ValueError:
#    - Ask the user to enter an integer.
#    - Use a `try-except` block to catch a `ValueError` if the user enters non-numeric input.
#    - If an error occurs, print "Invalid input. Please enter a whole number."
#    - If successful, print "You entered: [number]".

# Your code here:
try:
    user_input_int = input("Enter a whole number: ")
    number = int(user_input_int)
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input. Please enter a whole number.")

# 1.2 Catching a ZeroDivisionError:
#    - Ask the user to enter two numbers.
#    - Convert them to floats.
#    - Use a `try-except` block to perform division.
#    - Catch `ZeroDivisionError` if the second number is zero, printing "Error: Cannot divide by zero."
#    - If successful, print the result of the division.

# Your code here:
try:
    num_str1 = input("Enter the first number: ")
    num_str2 = input("Enter the second number: ")
    n1 = float(num_str1)
    n2 = float(num_str2)
    result = n1 / n2
    print(f"Result of division: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter numeric values.")


# --- Section 2: Multiple Except Blocks ---

print("\n--- Section 2: Multiple Except Blocks ---")

# 2.1 Handling Multiple Specific Exceptions:
#    - Create a list `my_list = [1, 2, 3]`.
#    - Ask the user for an index and a value.
#    - Use a `try-except` block to:
#      - Convert the index and value to integers.
#      - Attempt to assign the value to the list at the given index.
#    - Catch `ValueError` for invalid number input.
#    - Catch `IndexError` if the index is out of bounds.
#    - Print appropriate error messages for each.

# Your code here:
my_list = [1, 2, 3]
print(f"Current list: {my_list}")
try:
    index_str = input("Enter an index to modify the list: ")
    value_str = input("Enter a value to place at that index: ")
    index = int(index_str)
    value = int(value_str)
    my_list[index] = value
    print(f"List after modification: {my_list}")
except ValueError:
    print("Error: Invalid input. Please enter whole numbers for index and value.")
except IndexError:
    print("Error: Index out of bounds. Please enter a valid index.")

# 2.2 Catching a Generic Exception:
#    - Modify the previous exercise. Add a generic `except Exception as e:` block
#      at the end to catch any other unexpected errors and print a general message
#      like "An unexpected error occurred: [error_details]".

# Your code here:
my_list_gen = [10, 20, 30]
print(f"Current list: {my_list_gen}")
try:
    index_str_gen = input("Enter an index to modify the list: ")
    value_str_gen = input("Enter a value to place at that index: ")
    index_gen = int(index_str_gen)
    value_gen = int(value_str_gen)
    my_list_gen[index_gen] = value_gen
    print(f"List after modification: {my_list_gen}")
except ValueError:
    print("Error: Invalid input. Please enter whole numbers for index and value.")
except IndexError:
    print("Error: Index out of bounds. Please enter a valid index.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# --- Section 3: The `else` and `finally` Blocks ---

print("\n--- Section 3: The `else` and `finally` Blocks ---")

# 3.1 Using `else` Block:
#    - Ask the user for a filename.
#    - Use a `try-except-else` block to attempt opening the file for reading.
#    - If `FileNotFoundError` occurs, print "File not found."
#    - In the `else` block (if no exception occurs), read and print the first line of the file, then close it.
#    - Test with an existing file (e.g., this script itself) and a non-existent file.

# Your code here:
file_name = input("Enter a filename to read (e.g., this_script.py): ")
try:
    file = open(file_name, 'r')
except FileNotFoundError:
    print("File not found.")
else:
    first_line = file.readline()
    print(f"First line of '{file_name}': {first_line.strip()}")
    file.close()

# 3.2 Using `finally` Block:
#    - Create a function `divide_safe(a, b)` that performs division.
#    - Use a `try-except-finally` block.
#    - Catch `ZeroDivisionError`.
#    - In the `finally` block, print "Division attempt finished." regardless of whether an error occurred.
#    - Call `divide_safe(10, 2)` and `divide_safe(10, 0)`.

# Your code here:
def divide_safe(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print("Error: Division by zero inside divide_safe.")
    finally:
        print("Division attempt finished.")

divide_safe(10, 2)
divide_safe(10, 0)

# --- Section 4: Raising Exceptions ---

print("\n--- Section 4: Raising Exceptions ---")

# 4.1 Raising a Built-in Exception:
#    - Define a function `check_positive(number)` that raises a `ValueError`
#      with a message "Number must be positive" if the input `number` is not positive.
#    - Call `check_positive(5)` and `check_positive(-3)` within `try-except` blocks
#      to demonstrate catching the raised exception.

# Your code here:
def check_positive(number):
    if number <= 0:
        raise ValueError("Number must be positive")
    print(f"{number} is a positive number.")

try:
    check_positive(5)
except ValueError as e:
    print(f"Caught error: {e}")

try:
    check_positive(-3)
except ValueError as e:
    print(f"Caught error: {e}")

# --- Section 5: Custom Exceptions ---

print("\n--- Section 5: Custom Exceptions ---")

# 5.1 Defining and Raising a Custom Exception:
#    - Define a custom exception class named `InvalidAgeError` that inherits from `Exception`.
#    - Define a function `set_user_age(age)` that raises `InvalidAgeError` if the
#      `age` is less than 0 or greater than 120.
#    - Call `set_user_age(30)` and `set_user_age(150)` within `try-except` blocks
#      to demonstrate catching your custom exception.

# Your code here:
class InvalidAgeError(Exception):
    """Custom exception raised for invalid age values."""
    pass

def set_user_age(age):
    if not 0 <= age <= 120:
        raise InvalidAgeError(f"Age {age} is outside the valid range (0-120).")
    print(f"User age set to: {age}")

try:
    set_user_age(30)
except InvalidAgeError as e:
    print(f"Caught custom error: {e}")

try:
    set_user_age(150)
except InvalidAgeError as e:
    print(f"Caught custom error: {e}")

# --- Section 6: Advanced Exception Handling (Optional) ---

print("\n--- Section 6: Advanced Exception Handling (Optional) ---")

# 6.1 Using `assert` for Debugging/Pre-conditions:
#    - Define a function `calculate_average(numbers)` that takes a list of numbers.
#    - Use an `assert` statement to ensure the input list is not empty.
#    - If the assertion fails, it will raise an `AssertionError`.
#    - Call `calculate_average([1, 2, 3])` and `calculate_average([])`.

# Your code here:
def calculate_average(numbers):
    assert len(numbers) > 0, "List of numbers cannot be empty"
    return sum(numbers) / len(numbers)

try:
    avg1 = calculate_average([1, 2, 3])
    print(f"Average of [1, 2, 3]: {avg1}")
except AssertionError as e:
    print(f"Caught assertion error: {e}")

try:
    avg2 = calculate_average([])
    print(f"Average of []: {avg2}") # This line won't be reached if assertion fails
except AssertionError as e:
    print(f"Caught assertion error: {e}")

# 6.2 Chaining Exceptions (`raise from`):
#    - Define a function `fetch_data_from_api()` that simulates an API call and might raise a `ConnectionError`.
#    - Define another function `process_report()` that calls `fetch_data_from_api()`.
#    - If `fetch_data_from_api()` fails, `process_report()` should catch `ConnectionError` and then raise a new `ReportGenerationError` (custom exception) *from* the original `ConnectionError`.
#    - Demonstrate catching `ReportGenerationError` and inspecting the original cause.

# Your code here:
class ReportGenerationError(Exception):
    """Custom exception for errors during report generation."""
    pass

def fetch_data_from_api(success=False):
    if not success:
        raise ConnectionError("Failed to connect to API.")
    return "Data fetched successfully."

def process_report(api_success):
    try:
        data = fetch_data_from_api(api_success)
        print(f"Report processed: {data}")
    except ConnectionError as e:
        raise ReportGenerationError("Could not generate report due to API connection issue.") from e

try:
    process_report(False) # Simulate API failure
except ReportGenerationError as e:
    print(f"\nCaught ReportGenerationError: {e}")
    if e.__cause__:
        print(f"Original cause: {e.__cause__}")

try:
    process_report(True) # Simulate API success
except ReportGenerationError as e:
    print(f"\nCaught ReportGenerationError: {e}")


print("\n--- End of Python Exceptions Handling Assignment ---")
