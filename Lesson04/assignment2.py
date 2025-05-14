import datetime
import math

def calculate_circle_area_circumference():
    radius = 7  # Example radius
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    print("\n--- Circle Calculations ---")
    print(f"Radius: {radius}")
    print(f"Area: {area:.2f}")
    print(f"Circumference: {circumference:.2f}")

def display_current_date_time():
    now = datetime.datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    print("\n--- Current Date and Time ---")
    print(f"Current Date and Time (Ahmedabad): {formatted_datetime} IST")

def check_palindrome():
    word = "madam"  # Example word
    if word == word[::-1]:
        print(f"\n--- Palindrome Check ---")
        print(f"'{word}' is a palindrome.")
    else:
        print(f"\n--- Palindrome Check ---")
        print(f"'{word}' is not a palindrome.")

if __name__ == "__main__":
    while True:
        try:
            choice = int(input("\nEnter a number to run a program:\n1. Calculate Circle Area and Circumference\n2. Display Current Date and Time\n3. Check if a Word is a Palindrome\n4. Exit\nYour choice: "))
            if choice == 1:
                calculate_circle_area_circumference()
            elif choice == 2:
                display_current_date_time()
            elif choice == 3:
                check_palindrome()
            elif choice == 4:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter an integer.")