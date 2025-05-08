# Title: User Input Assignment in Python

# Task 1: Take name and age as input and display a greeting
name = input("Enter your name: ")
age = input("Enter your age: ")

# Validating if age is a number
if age.isdigit():
    print(f"Hello, {name}! You are {age} years old.")
else:
    print("Invalid age. Please enter a number.")

# Task 2: Ask the user for two numbers and add them
num1 = input("\nEnter the first number: ")
num2 = input("Enter the second number: ")

# Convert to float and add
try:
    sum_result = float(num1) + float(num2)
    print(f"The sum of {num1} and {num2} is: {sum_result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")

# Task 3: BMI Calculator
print("\n--- BMI Calculator ---")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {round(bmi, 2)}")

# Task 4: Favorite things survey
print("\n--- Favorite Things Survey ---")
color = input("What is your favorite color? ")
movie = input("What is your favorite movie? ")
food = input("What is your favorite food? ")

print(f"\nNice! So your favorite color is {color},")
print(f"your favorite movie is {movie},")
print(f"and your favorite food is {food}.")

# Task 5: Age in 2050
current_age = int(input("\nEnter your current age: "))
age_in_2050 = current_age + (2050 - 2025)
print(f"You will be {age_in_2050} years old in 2050.")

# Task 6: Password Check
print("\n--- Login System ---")
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid username or password.")
