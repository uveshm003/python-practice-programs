import random
from collections import Counter

def analyze_text_frequency():
    text = """This is a sample text. This text contains some repeated words.
    Sample text analysis can be useful for various purposes.
    This sample aims to demonstrate text frequency analysis."""
    words = text.lower().split()
    word_counts = Counter(words)
    most_common = word_counts.most_common(5)
    print("\n--- Text Frequency Analysis ---")
    for word, count in most_common:
        print(f"{word}: {count}")

def simulate_dice_rolls():
    rolls = [random.randint(1, 6) for _ in range(100)]
    roll_counts = Counter(rolls)
    print("\n--- Dice Roll Simulation (100 Rolls) ---")
    for roll, count in sorted(roll_counts.items()):
        print(f"Number {roll}: {count} times")

def process_student_scores():
    student_scores = {
        "Alice": [85, 92, 78],
        "Bob": [76, 88, 95],
        "Charlie": [60, 70, 80],
        "David": [90, 82, 75]
    }
    student_averages = {}
    for name, scores in student_scores.items():
        average = sum(scores) / len(scores)
        student_averages[name] = average
    print("\n--- Student Score Averages ---")
    for student, average in student_averages.items():
        print(f"{student}: {average:.2f}")

if __name__ == "__main__":
    while True:
        try:
            choice = int(input("\nEnter a number to run a program:\n1. Text Frequency Analysis\n2. Dice Roll Simulation\n3. Student Score Averages\n4. Exit\nYour choice: "))
            if choice == 1:
                analyze_text_frequency()
            elif choice == 2:
                simulate_dice_rolls()
            elif choice == 3:
                process_student_scores()
            elif choice == 4:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter an integer.")