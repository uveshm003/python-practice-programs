# Step 1: Declare variables of different data types
name = "John Doe"                  # String
age = 25                           # Integer
height = 5.9                       # Float
is_employed = True                # Boolean
skills = ["Python", "Flutter"]     # List
education = ("BSc", "MSc")         # Tuple
profile = {"name": "John", "age": 25}  # Dictionary
unique_ids = {101, 102, 103}       # Set

# Step 2: Print all variables with their types
print("Name:", name, "→", type(name))
print("Age:", age, "→", type(age))
print("Height:", height, "→", type(height))
print("Is Employed:", is_employed, "→", type(is_employed))
print("Skills:", skills, "→", type(skills))
print("Education:", education, "→", type(education))
print("Profile:", profile, "→", type(profile))
print("Unique IDs:", unique_ids, "→", type(unique_ids))

# Step 3: Perform operations using data types
print("\nAdding a skill to the list...")
skills.append("Django")
print("Updated Skills:", skills)

print("\nAccessing tuple element:", education[0])
print("Name from dictionary:", profile["name"])

# Step 4: Ask the user to input their own data and display types
user_age = input("\nEnter your age: ")
print("You entered:", user_age, "| Type:", type(user_age))  # still string

# Convert to int
user_age = int(user_age)
print("Converted Age:", user_age, "| Type:", type(user_age))
