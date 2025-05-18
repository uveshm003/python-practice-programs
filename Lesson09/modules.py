"""
Python Modules Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
Python modules, including importing, creating, and using them, starting
from fundamental concepts and progressing to more advanced uses. Work
through each section and complete the tasks.
"""

print("--- Python Modules Assignment ---")

# --- Section 1: Importing Built-in Modules ---

print("\n--- Section 1: Importing Built-in Modules ---")

# 1.1 Basic Import:
#    - Import the `math` module.
#    - Use the `math.sqrt()` function to calculate the square root of 16 and print the result.
#    - Use the `math.pi` constant to print the value of pi.

# Your code here:
import math

sqrt_16 = math.sqrt(16)
print(f"The square root of 16 is: {sqrt_16}")
print(f"The value of pi is: {math.pi}")

# 1.2 Importing Specific Names:
#    - From the `datetime` module, import only the `datetime` class.
#    - Use the imported `datetime` class to get the current date and time and print it.

# Your code here:
from datetime import datetime

now = datetime.now()
print(f"The current date and time is: {now}")

# 1.3 Importing with an Alias:
#    - Import the `random` module with the alias `rnd`.
#    - Use the alias `rnd` to generate a random integer between 1 and 10 (inclusive) and print it.

# Your code here:
import random as rnd

random_number = rnd.randint(1, 10)
print(f"A random number between 1 and 10 is: {random_number}")

# --- Section 2: Creating Your Own Modules ---

print("\n--- Section 2: Creating Your Own Modules ---")

# 2.1 Creating a Simple Module:
#    - Create a new Python file named `my_module.py` in the same directory as this script.
#    - In `my_module.py`, define a function named `greet(name)` that prints "Hello, [name] from my_module!".
#    - Also, define a variable named `module_version` and assign it the value "1.0".

# (Create my_module.py with the following content)
"""
# my_module.py
def greet(name):
    print(f"Hello, {name} from my_module!")

module_version = "1.0"
"""

# 2.2 Importing and Using Your Module:
#    - In this main script, import the `my_module`.
#    - Call the `greet()` function from `my_module` with your name as the argument.
#    - Print the value of the `module_version` variable from `my_module`.

# Your code here:
import my_module

my_module.greet("Learner")
print(f"The version of my_module is: {my_module.module_version}")

# 2.3 Importing Specific Names from Your Module:
#    - From `my_module`, import only the `greet` function.
#    - Call the imported `greet` function.

# Your code here:
from my_module import greet

greet("Another Learner")

# --- Section 3: Module Search Path ---

print("\n--- Section 3: Module Search Path ---")

# 3.1 Understanding `sys.path`:
#    - Import the `sys` module.
#    - Print the value of `sys.path`. Observe the list of directories Python searches for modules.
#    - Briefly explain in a comment why the current directory is usually included in `sys.path`.

# Your code here:
import sys

print("Python Module Search Path (sys.path):")
for path in sys.path:
    print(path)

# Explanation: The current directory is usually included in sys.path so that Python
# can easily find and import modules that are located in the same directory as the
# script being executed. This is a common way to organize project-specific modules.

# --- Section 4: Packages (Introduction) ---

print("\n--- Section 4: Packages (Introduction) ---")

# 4.1 Creating a Simple Package:
#    - Create a new directory named `my_package` in the same directory as this script.
#    - Inside `my_package`, create an empty file named `__init__.py`. This makes the directory a Python package.
#    - Inside `my_package`, create another Python file named `utils.py`.
#    - In `my_package/utils.py`, define a function named `say_hello_package(name)` that prints "Hello, [name] from my_package.utils!".

# (Create the directory structure and files with the following content)
"""
# my_package/__init__.py (empty file)

# my_package/utils.py
def say_hello_package(name):
    print(f"Hello, {name} from my_package.utils!")
"""

# 4.2 Importing and Using Your Package:
#    - Import the `utils` module from the `my_package`.
#    - Call the `say_hello_package()` function.

# Your code here:
from my_package import utils

utils.say_hello_package("Package User")

# 4.3 Importing Specific Names from a Package Module:
#    - From `my_package.utils`, import only the `say_hello_package` function.
#    - Call the imported function.

# Your code here:
from my_package.utils import say_hello_package

say_hello_package("Another Package User")

# --- Section 5: Advanced Module Concepts (Optional) ---

print("\n--- Section 5: Advanced Module Concepts (Optional) ---")

# 5.1 Relative Imports (within Packages):
#    - Inside the `my_package` directory, create another module named `helper.py`.
#    - In `my_package/helper.py`, define a function `helper_function()`.
#    - Modify `my_package/utils.py` to import `helper_function` using a relative import
#      (e.g., `from . import helper`) and call it from within `say_hello_package`.

# (Modify my_package/utils.py and create my_package/helper.py)
"""
# my_package/helper.py
def helper_function():
    print("Helper function called from within the package.")

# my_package/utils.py (modified)
from . import helper

def say_hello_package(name):
    print(f"Hello, {name} from my_package.utils!")
    helper.helper_function()
"""

#    - Run this main script again and observe the output.

# (No code needed here, just run the main script)

# 5.2 The `__name__` Variable:
#    - Add the following code to both `my_module.py` and `my_package/utils.py`:
#      ```python
#      if __name__ == "__main__":
#          print("This code runs only when the script is executed directly.")
#      ```
#    - Run `my_module.py` directly from the terminal (e.g., `python my_module.py`).
#    - Then, run this main script again. Observe when the print statement inside the `if __name__ == "__main__":` block is executed and explain why.

# (Run my_module.py directly and then run this main script)
# Explanation: The code inside the `if __name__ == "__main__":` block runs only when
# the script is executed directly. When the module is imported into another script,
# the `__name__` variable is set to the module's name (e.g., 'my_module'), not '__main__',
# so the block is not executed. This is useful for including test code or standalone
# functionality within a module.

print("\n--- End of Python Modules Assignment ---")