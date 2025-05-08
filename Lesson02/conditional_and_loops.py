# Title: Loops and Conditionals in Python

# Task 1: Check if a number is positive, negative or zero
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Task 2: Print even numbers between 1 and 20 using a for loop
print("\nEven numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

# Task 3: Sum of all numbers entered by the user until they enter 0
print("\n\nEnter numbers to sum them (enter 0 to stop):")
total = 0
while True:
    value = int(input("Enter a number: "))
    if value == 0:
        break
    total += value

print("Total sum is:", total)

# Task 4: FizzBuzz Challenge from 1 to 30
# Print "Fizz" if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if both
print("\nFizzBuzz from 1 to 30:")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
