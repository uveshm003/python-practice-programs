# Step 1: Declare variables
name = "Alice"
age = 24
height = 5.6  # in feet
is_student = True

# Step 2: Print the variables with explanation
print("Name:", name)
print("Age:", age)
print("Height:", height, "feet")
print("Is Student:", is_student)

# Step 3: Ask user for their own details
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_height = float(input("Enter your height in feet: "))
user_student_status = input("Are you a student? (yes/no): ")

# Step 4: Convert student input to boolean
is_user_student = user_student_status.lower() == "yes"

# Step 5: Display the entered information
print("\nYour Details:")
print("Name:", user_name)
print("Age:", user_age)
print("Height:", user_height, "feet")
print("Is Student:", is_user_student)

# Step 6: Simple operation: calculate age difference
age_difference = abs(age - user_age)
print("\nThe age difference between you and", name, "is", age_difference, "years.")
