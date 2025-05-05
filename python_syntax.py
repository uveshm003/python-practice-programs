# 1. Variables, Data Types, Input/Output
print("🎓 Welcome to the Student Management System!\n")

students = []  # List to store student dictionaries

# 2. Functions
def add_student():
    try:
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        grades = list(map(int, input("Enter 3 grades separated by space: ").split()))
        student = {
            "name": name,
            "age": age,
            "grades": grades,
        }
        students.append(student)
        print(f"✅ Student '{name}' added successfully!\n")
    except ValueError:
        print("❌ Invalid input! Please enter correct values.\n")

# 3. Loops, Conditionals
def view_students():
    if not students:
        print("⚠️ No students found.\n")
        return
    for idx, s in enumerate(students, 1):
        print(f"{idx}. {s['name']} (Age: {s['age']}) - Grades: {s['grades']}")

# 4. String manipulation, List comprehension
def average_grade():
    if not students:
        print("⚠️ No data to calculate average.\n")
        return
    for s in students:
        avg = sum(s["grades"]) / len(s["grades"])
        print(f"{s['name']}'s average grade is {avg:.2f}")

# 5. File handling
def save_to_file():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['age']},{' '.join(map(str, s['grades']))}\n")
    print("📁 Data saved to 'students.txt'!\n")

def load_from_file():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                name = parts[0]
                age = int(parts[1])
                grades = list(map(int, parts[2].split()))
                students.append({"name": name, "age": age, "grades": grades})
        print("✅ Data loaded from file.\n")
    except FileNotFoundError:
        print("❌ No saved file found.\n")

# 6. Object-Oriented Programming (Class & Object)
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_average(self):
        return sum(self.grades) / len(self.grades)

# 7. Main loop
def main():
    load_from_file()
    while True:
        print("\n1. Add Student\n2. View Students\n3. Show Averages\n4. Save\n5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            average_grade()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice!\n")

if __name__ == "__main__":
    main()
