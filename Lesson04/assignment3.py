import os
import platform

def list_files_in_directory():
    directory = "."  # Current directory
    print(f"\n--- Files in Current Directory ('{directory}') ---")
    try:
        files = os.listdir(directory)
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_system_information():
    system = platform.system()
    node_name = platform.node()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()

    print("\n--- System Information ---")
    print(f"Operating System: {system}")
    print(f"Node Name: {node_name}")
    print(f"Release: {release}")
    print(f"Version: {version}")
    print(f"Machine: {machine}")
    print(f"Processor: {processor}")

def calculate_factorial():
    number = 5  # Example number
    factorial = 1
    if number < 0:
        print("\n--- Factorial Calculation ---")
        print("Factorial does not exist for negative numbers.")
    elif number == 0:
        print("\n--- Factorial Calculation ---")
        print("The factorial of 0 is 1.")
    else:
        for i in range(1, number + 1):
            factorial = factorial * i
        print("\n--- Factorial Calculation ---")
        print(f"The factorial of {number} is {factorial}")

if __name__ == "__main__":
    while True:
        try:
            choice = int(input("\nEnter a number to run a program:\n1. List Files in Current Directory\n2. Get System Information\n3. Calculate Factorial\n4. Exit\nYour choice: "))
            if choice == 1:
                list_files_in_directory()
            elif choice == 2:
                get_system_information()
            elif choice == 3:
                calculate_factorial()
            elif choice == 4:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter an integer.")