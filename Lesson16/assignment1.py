"""
Python Classes Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
Python classes, including object-oriented programming (OOP) concepts like
attributes, methods, inheritance, and polymorphism. Work through each section
and complete the tasks.
"""

print("--- Python Classes Assignment ---")

# --- Section 1: Basic Class and Objects ---

print("\n--- Section 1: Basic Class and Objects ---")

# 1.1 Defining a Simple Class:
#    - Define a class named 'Dog'.
#    - Inside the class, define a method named 'bark' that prints "Woof!".
#    - Create an instance (object) of the 'Dog' class named 'my_dog'.
#    - Call the 'bark' method on 'my_dog'.

# Your code here:
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()

# 1.2 Class with an `__init__` Method (Constructor) and Attributes:
#    - Define a class named 'Car'.
#    - Add an `__init__` method that takes 'make' and 'model' as parameters.
#    - Store 'make' and 'model' as instance attributes.
#    - Add a method 'display_info' that prints the car's make and model.
#    - Create two 'Car' objects with different makes and models.
#    - Call 'display_info' on both car objects.

# Your code here:
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car: {self.make} {self.model}")

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.display_info()
car2.display_info()

# --- Section 2: Class and Instance Attributes/Methods ---

print("\n--- Section 2: Class and Instance Attributes/Methods ---")

# 2.1 Class Attributes vs. Instance Attributes:
#    - Define a class 'Student'.
#    - Add a class attribute `school_name` and set it to "Global High School".
#    - Add an `__init__` method that takes 'name' and 'student_id' as instance attributes.
#    - Create two 'Student' objects.
#    - Print the `school_name` using both the class name and an instance.
#    - Change `school_name` using the class name and observe the effect on instances.

# Your code here:
class Student:
    school_name = "Global High School"

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")

print(f"Student1's school (via instance): {student1.school_name}")
print(f"Student2's school (via instance): {student2.school_name}")
print(f"School name (via class): {Student.school_name}")

Student.school_name = "New Global High School" # Modifying class attribute

print(f"Student1's school (after class change): {student1.school_name}")
print(f"Student2's school (after class change): {student2.school_name}")

# 2.2 Instance Methods and `self`:
#    - In the 'Car' class from Section 1.2, add a method `start_engine` that prints
#      "The [make] [model] engine is starting." (use `self` to access attributes).
#    - Call `start_engine` on one of your car objects.

# Your code here:
# (Re-defining Car class for clarity, or assume it's already defined above)
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car: {self.make} {self.model}")

    def start_engine(self):
        print(f"The {self.make} {self.model} engine is starting.")

car3 = Car("Ford", "Mustang")
car3.start_engine()

# --- Section 3: Inheritance ---

print("\n--- Section 3: Inheritance ---")

# 3.1 Basic Inheritance:
#    - Define a base class 'Animal' with an `__init__` method taking 'name' and a method 'speak' that prints "Animal makes a sound".
#    - Define a derived class 'Cat' that inherits from 'Animal'.
#    - In 'Cat', override the 'speak' method to print "Meow!".
#    - Create an 'Animal' object and a 'Cat' object.
#    - Call 'speak' on both objects.

# Your code here:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animal_obj = Animal("Generic Animal")
cat_obj = Cat("Whiskers")

animal_obj.speak()
cat_obj.speak()

# 3.2 Using `super()` in Inheritance:
#    - Define a base class 'Person' with an `__init__` method taking 'name' and 'age'.
#    - Define a derived class 'Developer' that inherits from 'Person'.
#    - In 'Developer's `__init__` method, also take 'programming_language'.
#    - Use `super().__init__(name, age)` to call the base class constructor.
#    - Add a method 'code' to 'Developer' that prints "[name] is coding in [programming_language]".
#    - Create a 'Developer' object and call its 'code' method.

# Your code here:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Developer(Person):
    def __init__(self, name, age, programming_language):
        super().__init__(name, age)
        self.programming_language = programming_language

    def code(self):
        print(f"{self.name} is coding in {self.programming_language}.")

dev1 = Developer("Rohan", 28, "Python")
dev1.code()

# --- Section 4: Polymorphism ---

print("\n--- Section 4: Polymorphism ---")

# 4.1 Polymorphism with Methods:
#    - Define a base class 'Shape' with a method 'area' that returns 0.
#    - Define two derived classes: 'Circle' (with a 'radius' attribute) and 'Rectangle' (with 'width' and 'height' attributes).
#    - Override the 'area' method in 'Circle' to calculate `pi * radius**2`.
#    - Override the 'area' method in 'Rectangle' to calculate `width * height`.
#    - Create a list of different 'Shape' objects (Circle, Rectangle).
#    - Iterate through the list and call the 'area' method on each object.

# Your code here:
import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6), Circle(2.5)]

print("\nCalculating areas (Polymorphism):")
for shape in shapes:
    print(f"Area: {shape.area():.2f}")

# --- Section 5: Advanced Class Concepts (Optional) ---

print("\n--- Section 5: Advanced Class Concepts (Optional) ---")

# 5.1 Class Methods (using `@classmethod`):
#    - Define a class 'Product' with a class attribute `tax_rate` = 0.05.
#    - Add a class method `set_tax_rate(cls, new_rate)` that modifies the `tax_rate`.
#    - Add an instance method `calculate_total_price(self, price)` that returns `price * (1 + self.tax_rate)`.
#    - Create a product instance. Print its total price. Change the tax rate using the class method.
#    - Create another product instance and print its total price to see the effect of the changed class attribute.

# Your code here:
class Product:
    tax_rate = 0.05

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate
        print(f"Tax rate updated to: {cls.tax_rate}")

    def calculate_total_price(self, price):
        return price * (1 + self.tax_rate)

product_a = Product("Laptop")
print(f"Price of Laptop (before tax change): {product_a.calculate_total_price(1000):.2f}")

Product.set_tax_rate(0.08) # Change tax rate using class method

product_b = Product("Mouse")
print(f"Price of Mouse (after tax change): {product_b.calculate_total_price(50):.2f}")

# 5.2 Static Methods (using `@staticmethod`):
#    - In the 'Product' class, add a static method `is_valid_price(price)` that returns `True` if `price` is positive, `False` otherwise.
#    - Call `is_valid_price` using both the class name and an instance.

# Your code here:
# (Re-defining Product class with static method)
class Product:
    tax_rate = 0.05

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate
        print(f"Tax rate updated to: {cls.tax_rate}")

    @staticmethod
    def is_valid_price(price):
        return price > 0

    def calculate_total_price(self, price):
        return price * (1 + self.tax_rate)

print(f"Is 100 a valid price (via class)? {Product.is_valid_price(100)}")
product_c = Product("Keyboard")
print(f"Is -5 a valid price (via instance)? {product_c.is_valid_price(-5)}")

# 5.3 Operator Overloading (`__str__` and `__add__`):
#    - Define a class 'Vector' with `x` and `y` attributes.
#    - Implement the `__str__` method to return a user-friendly string representation (e.g., "Vector(x=1, y=2)").
#    - Implement the `__add__` method to allow adding two 'Vector' objects (element-wise addition).
#    - Create two 'Vector' objects, print them, and print their sum.

# Your code here:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Can only add Vector objects to a Vector.")

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v_sum = v1 + v2

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Vector Sum: {v_sum}")

print("\n--- End of Python Classes Assignment ---")
