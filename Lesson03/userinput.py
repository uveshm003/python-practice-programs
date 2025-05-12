"""
Python User Input Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
how to take user input in Python, starting from fundamental concepts and
progressing to more advanced handling and validation. Work through each
section and complete the tasks.
"""

print("--- Python User Input Assignment ---")

# --- Section 1: Basic Input ---

print("\n--- Section 1: Basic Input ---")

# 1.1 Getting Simple String Input:
#    - Ask the user for their name and store it in a variable called 'name'.
#    - Print a greeting message using the entered name (e.g., "Hello, [name]!").

# Your code here:
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# 1.2 Getting Numerical Input (Initial Attempt):
#    - Ask the user for their age and store it in a variable called 'age_str'.
#    - Print the entered age.
#    - What is the datatype of 'age_str'? Verify using `type()`.

# Your code here:
age_str = input("Please enter your age: ")
print(f"Your age is: {age_str}")
print(f"Datatype of age_str: {type(age_str)}")
# Explanation: The input() function always returns a string.

# --- Section 2: Converting Input Datatypes ---

print("\n--- Section 2: Converting Input Datatypes ---")

# 2.1 Converting String to Integer:
#    - Ask the user to enter their age again.
#    - Convert the input to an integer using `int()` and store it in a variable called 'age_int'.
#    - Print the age and verify its datatype using `type()`.

# Your code here:
age_str_again = input("Please enter your age again: ")
age_int = int(age_str_again)
print(f"Your age (as integer): {age_int}")
print(f"Datatype of age_int: {type(age_int)}")

# 2.2 Converting String to Float:
#    - Ask the user to enter a floating-point number.
#    - Convert the input to a float using `float()` and store it in a variable called 'float_num'.
#    - Print the number and verify its datatype.

# Your code here:
float_str = input("Please enter a floating-point number: ")
float_num = float(float_str)
print(f"You entered: {float_num}")
print(f"Datatype of float_num: {type(float_num)}")

# --- Section 3: Handling Potential Errors (try-except) ---

print("\n--- Section 3: Handling Potential Errors (try-except) ---")

# 3.1 Handling ValueError for Integer Conversion:
#    - Ask the user to enter their age.
#    - Use a `try-except` block to handle the case where the user enters non-numeric input.
#    - If a `ValueError` occurs, print an error message.
#    - If the conversion is successful, print the age.

# Your code here:
while True:
    age_input_safe = input("Please enter your age (numeric): ")
    try:
        age_safe = int(age_input_safe)
        print(f"Your age is: {age_safe}")
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a whole number for your age.")

# 3.2 Handling ValueError for Float Conversion:
#    - Ask the user to enter a price.
#    - Use a `try-except` block to handle non-numeric input and print an appropriate error message.
#    - If successful, print the price.

# Your code here:
while True:
    price_input = input("Please enter a price (e.g., 10.50): ")
    try:
        price = float(price_input)
        print(f"The price is: {price}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the price.")

# --- Section 4: Getting Multiple Inputs ---

print("\n--- Section 4: Getting Multiple Inputs ---")

# 4.1 Getting Space-Separated Input:
#    - Ask the user to enter two numbers separated by a space (e.g., "5 10").
#    - Read the input, split it into two strings, convert them to integers, and store them in variables 'num_a' and 'num_b'.
#    - Print the sum of 'num_a' and 'num_b'.

# Your code here:
two_numbers_str = input("Enter two numbers separated by a space: ")
num_a_str, num_b_str = two_numbers_str.split()
num_a = int(num_a_str)
num_b = int(num_b_str)
print(f"The sum of {num_a} and {num_b} is: {num_a + num_b}")

# 4.2 Getting Comma-Separated Input:
#    - Ask the user to enter three colors separated by commas (e.g., "red,green,blue").
#    - Read the input, split it into a list of color strings, and print the list.

# Your code here:
colors_str = input("Enter three colors separated by commas: ")
color_list = colors_str.split(',')
print(f"The colors you entered are: {color_list}")

# --- Section 5: Input with Prompts and Formatting ---

print("\n--- Section 5: Input with Prompts and Formatting ---")

# 5.1 Using f-strings in Prompts:
#    - Ask the user for their favorite color using an f-string prompt that includes their name (obtained earlier).

# Your code here:
favorite_color = input(f"{name}, what is your favorite color? ")
print(f"Your favorite color is: {favorite_color}")

# 5.2 Formatting Output with User Input:
#    - Ask the user for the name of a product and its price.
#    - Print a formatted string displaying the product name and price with two decimal places.

# Your code here:
product_name = input("Enter the name of a product: ")
while True:
    try:
        product_price_str = input(f"Enter the price of {product_name}: ")
        product_price = float(product_price_str)
        break
    except ValueError:
        print("Invalid price. Please enter a valid number.")

print(f"The price of {product_name} is: ₹{product_price:.2f}")

# --- Section 6: Advanced Input Handling (Optional) ---

print("\n--- Section 6: Advanced Input Handling (Optional) ---")

# 6.1 Validating Input within a Loop:
#    - Ask the user to enter a number between 1 and 10 (inclusive).
#    - Use a `while` loop to keep asking until a valid number is entered.

# Your code here:
while True:
    valid_num_str = input("Enter a number between 1 and 10 (inclusive): ")
    try:
        valid_num = int(valid_num_str)
        if 1 <= valid_num <= 10:
            print(f"You entered a valid number: {valid_num}")
            break
        else:
            print("Number is out of the valid range. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# 6.2 Getting Password Input (Security Consideration):
#    - Import the `getpass` module.
#    - Use `getpass.getpass()` to securely get a password from the user (the input will be hidden).
#    - Print a message indicating that the password has been received (do not print the actual password).

# Your code here:
import getpass

password = getpass.getpass("Enter your password: ")
print("Password received securely.")
# Important Note: In real applications, you should never print or store passwords directly.

# 6.3 Handling Multiple Exceptions:
#    - Ask the user to enter a number.
#    - Use a single `try` block with multiple `except` clauses to handle both `ValueError` (if input is not a number)
#      and potentially other exceptions (though not explicitly anticipated here).

# Your code here:
number_input_multi_except = input("Enter a number: ")
try:
    processed_number = int(number_input_multi_except) * 2
    print(f"The number multiplied by 2 is: {processed_number}")
except ValueError:
    print("Error: Invalid input. Please enter a whole number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- End of Python User Input Assignment ---")