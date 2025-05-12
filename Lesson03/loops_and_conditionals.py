"""
Python Loops and Conditionals Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
Python loops (for and while) and conditional statements (if, elif, else),
starting from fundamental concepts and progressing to more advanced uses.
Work through each section and complete the tasks.
"""

print("--- Python Loops and Conditionals Assignment ---")

# --- Section 1: Basic Conditionals (if, else) ---

print("\n--- Section 1: Basic Conditionals (if, else) ---")

# 1.1 Simple If Statement:
#    - Ask the user to enter a number.
#    - If the number is greater than 10, print "The number is greater than 10."

# Your code here:
user_number_1 = int(input("Enter a number: "))
if user_number_1 > 10:
    print("The number is greater than 10.")

# 1.2 If-Else Statement:
#    - Ask the user to enter their age.
#    - If the age is 18 or older, print "You are eligible to vote."
#    - Otherwise, print "You are not eligible to vote yet."

# Your code here:
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# --- Section 2: More Conditionals (elif) ---

print("\n--- Section 2: More Conditionals (elif) ---")

# 2.1 If-Elif-Else Statement:
#    - Ask the user to enter a grade (A, B, C, D, or F).
#    - Print a corresponding message for each grade:
#      - A: "Excellent!"
#      - B: "Good job!"
#      - C: "Satisfactory."
#      - D: "Needs improvement."
#      - F: "Failed."
#    - If the user enters an invalid grade, print "Invalid grade."

# Your code here:
user_grade = input("Enter your grade (A, B, C, D, or F): ").upper()
if user_grade == 'A':
    print("Excellent!")
elif user_grade == 'B':
    print("Good job!")
elif user_grade == 'C':
    print("Satisfactory.")
elif user_grade == 'D':
    print("Needs improvement.")
elif user_grade == 'F':
    print("Failed.")
else:
    print("Invalid grade.")

# --- Section 3: Basic Loops (for loop) ---

print("\n--- Section 3: Basic Loops (for loop) ---")

# 3.1 Iterating through a List:
#    - Create a list of fruits: ['apple', 'banana', 'cherry'].
#    - Use a for loop to print each fruit in the list.

# Your code here:
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 3.2 Iterating through a Range:
#    - Use a for loop and the `range()` function to print numbers from 1 to 5 (inclusive).

# Your code here:
for i in range(1, 6):
    print(i)

# 3.3 Looping with Index:
#    - Iterate through the 'fruits' list using indices and print the index along with the fruit.

# Your code here:
for index in range(len(fruits)):
    print(f"Index {index}: {fruits[index]}")

# --- Section 4: Basic Loops (while loop) ---

print("\n--- Section 4: Basic Loops (while loop) ---")

# 4.1 Simple While Loop:
#    - Initialize a counter variable to 0.
#    - Use a while loop to print numbers from 0 to 3 (inclusive).

# Your code here:
counter = 0
while counter <= 3:
    print(counter)
    counter += 1

# 4.2 While Loop with User Input:
#    - Ask the user to enter "quit" to exit the loop.
#    - Keep prompting the user for input until they enter "quit".

# Your code here:
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter something (or 'quit' to exit): ")
    print(f"You entered: {user_input}")

# --- Section 5: Loop Control Statements ---

print("\n--- Section 5: Loop Control Statements ---")

# 5.1 `break` Statement:
#    - Iterate through the numbers from 1 to 10.
#    - If the number is 5, use the `break` statement to exit the loop.
#    - Print the numbers encountered before breaking.

# Your code here:
for number in range(1, 11):
    if number == 5:
        break
    print(number)

# 5.2 `continue` Statement:
#    - Iterate through the numbers from 1 to 10.
#    - If the number is even, use the `continue` statement to skip to the next iteration.
#    - Print only the odd numbers.

# Your code here:
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)

# --- Section 6: Nested Loops and Conditionals ---

print("\n--- Section 6: Nested Loops and Conditionals ---")

# 6.1 Nested For Loops:
#    - Use nested for loops to print a simple pattern of asterisks (*) like this:
#      *
#      **
#      ***
#      ****

# Your code here:
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

# 6.2 Nested Loops with Conditionals:
#    - Given a list of lists representing a matrix: `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
#    - Iterate through the matrix and print only the even numbers.

# Your code here:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for number in row:
        if number % 2 == 0:
            print(number)

# --- Section 7: Advanced Looping and Conditional Techniques ---

print("\n--- Section 7: Advanced Looping and Conditional Techniques ---")

# 7.1 Looping with `else` Block:
#    - Iterate through numbers from 2 to 10 using a for loop.
#    - Check if each number is prime. If a divisor is found, break the loop.
#    - Use the `else` block of the for loop to print "Prime number" if the loop completes without finding a divisor.

# Your code here:
for num in range(2, 11):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

# 7.2 Conditional Expressions (Ternary Operator):
#    - Ask the user to enter a number.
#    - Use a conditional expression to determine if the number is even or odd and print the result in a single line.

# Your code here:
user_number_2 = int(input("Enter another number: "))
result = "Even" if user_number_2 % 2 == 0 else "Odd"
print(f"The number is {result}.")

# 7.3 Looping through Dictionaries:
#    - Create a dictionary `student_info` = {'name': 'Bob', 'age': 22, 'major': 'Science'}.
#    - Use a for loop to print all the keys in the dictionary.
#    - Use a for loop to print all the values in the dictionary.
#    - Use a for loop to print all the key-value pairs in the dictionary.

# Your code here:
student_info = {'name': 'Bob', 'age': 22, 'major': 'Science'}

print("\nKeys in student_info:")
for key in student_info:
    print(key)

print("\nValues in student_info:")
for value in student_info.values():
    print(value)

print("\nKey-value pairs in student_info:")
for key, value in student_info.items():
    print(f"{key}: {value}")

print("\n--- End of Python Loops and Conditionals Assignment ---")