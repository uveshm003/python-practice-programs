"""
Python Command Line Arguments Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
how to work with command line arguments in Python using the `sys` module
and the `argparse` module, starting from fundamental concepts and
progressing to more advanced uses. Work through each section and complete
the tasks.
"""

import sys
import argparse

print("--- Python Command Line Arguments Assignment ---")

# --- Section 1: Basic Command Line Arguments (using sys.argv) ---

print("\n--- Section 1: Basic Command Line Arguments (using sys.argv) ---")

# 1.1 Accessing Command Line Arguments:
#    - Run this script from your terminal with a few arguments (e.g., `python your_script_name.py arg1 123 True`).
#    - Inside the script, print the `sys.argv` list. Observe how the arguments are stored.
#    - Print the name of the script itself (the first element of `sys.argv`).
#    - Print the number of command line arguments provided.

# Your code here:
print(f"Command line arguments (sys.argv): {sys.argv}")
print(f"Script name: {sys.argv[0]}")
print(f"Number of arguments: {len(sys.argv) - 1} (excluding script name)")

# 1.2 Using Basic Arguments:
#    - Modify the script to expect two command line arguments after the script name.
#    - Assign these arguments to variables `name` and `age_str`.
#    - Print a message like "Hello, [name]! You are [age] years old." Make sure to convert `age_str` to an integer.
#    - Run the script from the terminal with your name and age (e.g., `python your_script_name.py Alice 30`).
#    - What happens if you run the script with fewer or more than two arguments?

# Your code here:
if len(sys.argv) == 3:
    name = sys.argv[1]
    age_str = sys.argv[2]
    try:
        age = int(age_str)
        print(f"Hello, {name}! You are {age} years old.")
    except ValueError:
        print("Error: Age must be an integer.")
else:
    print("Usage: python your_script_name.py <name> <age>")

# --- Section 2: Introduction to argparse ---

print("\n--- Section 2: Introduction to argparse ---")

# 2.1 Creating a Simple Argument Parser:
#    - Create an `ArgumentParser` object.
#    - Add an argument `--name` that expects a string value and has a help message "Your name".
#    - Parse the command line arguments using `parser.parse_args()`.
#    - Print the value of the `name` argument.
#    - Run the script from the terminal with the `--name` argument (e.g., `python your_script_name.py --name Bob`).
#    - Try running it without the argument and observe the output.

# Your code here:
parser = argparse.ArgumentParser(description="A simple program to greet you.")
parser.add_argument("--name", type=str, help="Your name")
args = parser.parse_args()

if args.name:
    print(f"Hello, {args.name}!")
else:
    print("Please provide your name using the --name argument.")

# 2.2 Adding a Positional Argument:
#    - Modify the parser to add a positional argument `greeting` that expects a string and has a help message "The greeting message".
#    - Parse the arguments and print the value of the `greeting` argument along with the name (if provided).
#    - Run the script from the terminal with the positional argument (e.g., `python your_script_name.py Hi --name Charlie`).
#    - Try running it without the positional argument.

# Your code here:
parser = argparse.ArgumentParser(description="A program to greet you with a custom message.")
parser.add_argument("greeting", type=str, help="The greeting message")
parser.add_argument("--name", type=str, help="Your name")
args = parser.parse_args()

if args.name:
    print(f"{args.greeting}, {args.name}!")
else:
    print(f"{args.greeting}!")

# --- Section 3: Argument Types and Choices ---

print("\n--- Section 3: Argument Types and Choices ---")

# 3.1 Specifying Argument Types:
#    - Add an argument `--age` to the parser that expects an integer value and has a help message "Your age".
#    - Parse the arguments and print the age. Handle potential `None` value for `--age` if not provided.
#    - Run the script with and without the `--age` argument. Try providing non-integer values.

# Your code here:
parser = argparse.ArgumentParser(description="Greets you and tells your age.")
parser.add_argument("greeting", type=str, help="The greeting message")
parser.add_argument("--name", type=str, help="Your name")
parser.add_argument("--age", type=int, help="Your age")
args = parser.parse_args()

if args.name:
    print(f"{args.greeting}, {args.name}!")
if args.age is not None:
    print(f"You are {args.age} years old.")

# 3.2 Limiting Choices for an Argument:
#    - Add an argument `--mood` that expects a string and has a `choices` parameter set to `['happy', 'sad', 'neutral']`.
#    - Add a help message "Your current mood".
#    - Parse the arguments and print the mood. Try providing values outside the allowed choices.

# Your code here:
parser = argparse.ArgumentParser(description="Greets you and asks about your mood.")
parser.add_argument("greeting", type=str, help="The greeting message")
parser.add_argument("--name", type=str, help="Your name")
parser.add_argument("--age", type=int, help="Your age")
parser.add_argument("--mood", type=str, choices=['happy', 'sad', 'neutral'], help="Your current mood")
args = parser.parse_args()

if args.name:
    print(f"{args.greeting}, {args.name}!")
if args.age is not None:
    print(f"You are {args.age} years old.")
if args.mood:
    print(f"Your mood is: {args.mood}")

# --- Section 4: Optional and Required Arguments, Boolean Flags ---

print("\n--- Section 4: Optional and Required Arguments, Boolean Flags ---")

# 4.1 Making an Argument Required:
#    - Modify the `--name` argument to be required. Run the script without it and observe the error message.

# Your code here:
parser = argparse.ArgumentParser(description="Greets you and asks about your mood.")
parser.add_argument("greeting", type=str, help="The greeting message")
parser.add_argument("--name", type=str, help="Your name", required=True)
parser.add_argument("--age", type=int, help="Your age")
parser.add_argument("--mood", type=str, choices=['happy', 'sad', 'neutral'], help="Your current mood")
args = parser.parse_args()

print(f"{args.greeting}, {args.name}!")
if args.age is not None:
    print(f"You are {args.age} years old.")
if args.mood:
    print(f"Your mood is: {args.mood}")

# 4.2 Using Boolean Flags (Actions):
#    - Add a flag `--verbose` that, when present, sets `args.verbose` to `True` (default should be `False`). Use `action='store_true'`.
#    - Modify the script to print an extra "Verbose mode is on." message if `--verbose` is used.
#    - Run the script with and without the `--verbose` flag.

# Your code here:
parser = argparse.ArgumentParser(description="Greets you and optionally shows verbose output.")
parser.add_argument("greeting", type=str, help="The greeting message")
parser.add_argument("--name", type=str, help="Your name", required=True)
parser.add_argument("--age", type=int, help="Your age")
parser.add_argument("--mood", type=str, choices=['happy', 'sad', 'neutral'], help="Your current mood")
parser.add_argument("--verbose", action='store_true', help="Enable verbose output")
args = parser.parse_args()

print(f"{args.greeting}, {args.name}!")
if args.age is not None:
    print(f"You are {args.age} years old.")
if args.mood:
    print(f"Your mood is: {args.mood}")
if args.verbose:
    print("Verbose mode is on.")

# --- Section 5: Advanced argparse Features (Optional) ---

print("\n--- Section 5: Advanced argparse Features (Optional) ---")

# 5.1 Using `nargs` for Variable Number of Arguments:
#    - Add an argument `--hobbies` that can take zero or more string values. Use `nargs='*'`.
#    - Parse the arguments and print the list of hobbies (if any).
#    - Run the script with different numbers of hobbies (e.g., `--hobbies reading hiking coding`).

# Your code here:
parser = argparse.ArgumentParser(description="Greets you and lists your hobbies.")
parser.add_argument("greeting", type=str, help="The greeting message")
parser.add_argument("--name", type=str, help="Your name", required=True)
parser.add_argument("--hobbies", nargs='*', type=str, help="Your hobbies (space-separated)")
args = parser.parse_args()

print(f"{args.greeting}, {args.name}!")
if args.hobbies:
    print(f"Your hobbies are: {', '.join(args.hobbies)}")

# 5.2 Using `nargs='+'` for One or More Arguments:
#    - Change `--hobbies` to use `nargs='+'`. Run the script without any hobbies and observe the result.

# Your code here:
parser = argparse.ArgumentParser(description="Greets you and lists your hobbies.")
parser.add_argument("greeting", type=str, help="The greeting message")
parser.add_argument("--name", type=str, help="Your name", required=True)
parser.add_argument("--hobbies", nargs='+', type=str, help="Your hobbies (space-separated)")
args = parser.parse_args()

print(f"{args.greeting}, {args.name}!")
if args.hobbies:
    print(f"Your hobbies are: {', '.join(args.hobbies)}")

# 5.3 Using `action='append'` to Collect Multiple Occurrences of an Argument:
#    - Add an argument `--email` with `action='append'` to allow the user to specify multiple email addresses.
#    - Parse the arguments and print the list of email addresses.
#    - Run the script with multiple `--email` arguments (e.g., `--email user1@example.com --email user2@example.org`).

# Your code here:
parser = argparse.ArgumentParser(description="Greets you and collects email addresses.")
parser.add_argument("greeting", type=str, help="The greeting message")
parser.add_argument("--name", type=str, help="Your name", required=True)
parser.add_argument("--email", action='append', type=str, help="Your email address (can be specified multiple times)")
args = parser.parse_args()

print(f"{args.greeting}, {args.name}!")
if args.email:
    print(f"Your email addresses are: {', '.join(args.email)}")

print("\n--- End of Python Command Line Arguments Assignment ---")