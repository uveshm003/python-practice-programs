"""
Python Lists Assignment: From Basics to Advanced

This program provides a series of exercises designed to help you understand
Python lists, starting from fundamental concepts and progressing to more
advanced uses. Work through each section and complete the tasks.
"""

print("--- Python Lists Assignment ---")

# --- Section 1: Introduction to Lists ---

print("\n--- Section 1: Introduction to Lists ---")

# 1.1 Creating Lists:
#    - Create an empty list named 'empty_list'.
#    - Create a list named 'my_list' containing the elements 1, 2, 3, 4, 5.
#    - Create a list named 'mixed_list' containing an integer, a string, a float, and a boolean.

# Your code here:
empty_list = []
my_list = [1, 2, 3, 4, 5]
mixed_list = [10, "hello", 3.14, True]

print(f"Empty list: {empty_list}")
print(f"My list: {my_list}")
print(f"Mixed list: {mixed_list}")

# 1.2 List Mutability:
#    - Change the first element of 'my_list' to 0.
#    - Change the last element of 'mixed_list' to False.
#    - Print the modified lists.

# Your code here:
my_list[0] = 0
mixed_list[-1] = False

print(f"Modified my_list: {my_list}")
print(f"Modified mixed_list: {mixed_list}")

# --- Section 2: Accessing List Elements ---

print("\n--- Section 2: Accessing List Elements ---")

# 2.1 Indexing:
#    - Access and print the third element of 'my_list'.
#    - Access and print the second element of 'mixed_list' using negative indexing.

# Your code here:
third_element_my_list = my_list[2]
second_element_mixed_list_neg = mixed_list[-2]

print(f"Third element of my_list: {third_element_my_list}")
print(f"Second element of mixed_list (negative index): {second_element_mixed_list_neg}")

# 2.2 Slicing:
#    - Create a new list 'sub_list' containing elements from the second to the fourth (inclusive) of 'my_list'.
#    - Create another list 'even_indexed' containing elements at even indices of 'my_list'.
#    - Create a reversed copy of 'my_list' using slicing.

# Your code here:
sub_list = my_list[1:4]
even_indexed = my_list[::2]
reversed_list = my_list[::-1]

print(f"Sub-list of my_list (indices 1 to 3): {sub_list}")
print(f"Elements at even indices of my_list: {even_indexed}")
print(f"Reversed my_list: {reversed_list}")

# --- Section 3: Basic List Operations ---

print("\n--- Section 3: Basic List Operations ---")

# 3.1 Concatenation:
#    - Create two lists: 'list1' = [10, 20] and 'list2' = [30, 40].
#    - Concatenate 'list1' and 'list2' to create a new list 'combined_list'.

# Your code here:
list1 = [10, 20]
list2 = [30, 40]
combined_list = list1 + list2

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Combined list: {combined_list}")

# 3.2 Repetition:
#    - Create a list 'repeated_list' by repeating 'list1' three times.

# Your code here:
repeated_list = list1 * 3

print(f"Repeated list: {repeated_list}")

# 3.3 Membership:
#    - Check if the number 3 is present in 'my_list'. Print the boolean result.
#    - Check if the string "hello" is present in 'mixed_list'. Print the boolean result.

# Your code here:
is_3_present = 3 in my_list
is_hello_present = "hello" in mixed_list

print(f"Is 3 present in my_list? {is_3_present}")
print(f"Is 'hello' present in mixed_list? {is_hello_present}")

# --- Section 4: Modifying Lists ---

print("\n--- Section 4: Modifying Lists ---")

# 4.1 `append()`:
#    - Add the number 6 to the end of 'my_list'.

# Your code here:
my_list.append(6)
print(f"my_list after append(6): {my_list}")

# 4.2 `insert()`:
#    - Insert the number 100 at the beginning (index 0) of 'my_list'.

# Your code here:
my_list.insert(0, 100)
print(f"my_list after insert(0, 100): {my_list}")

# 4.3 `extend()`:
#    - Create a new list 'another_list' = [7, 8].
#    - Extend 'my_list' by adding all elements from 'another_list'.

# Your code here:
another_list = [7, 8]
my_list.extend(another_list)
print(f"my_list after extend(another_list): {my_list}")

# 4.4 `remove()`:
#    - Remove the first occurrence of the number 3 from 'my_list'.

# Your code here:
if 3 in my_list:
    my_list.remove(3)
    print(f"my_list after remove(3): {my_list}")
else:
    print("3 is not in my_list to remove.")

# 4.5 `pop()`:
#    - Remove and print the last element of 'my_list'.
#    - Remove and print the element at index 2 of 'my_list'.

# Your code here:
last_element = my_list.pop()
print(f"Popped last element from my_list: {last_element}, updated my_list: {my_list}")

element_at_index_2 = my_list.pop(2)
print(f"Popped element at index 2 from my_list: {element_at_index_2}, updated my_list: {my_list}")

# 4.6 `clear()`:
#    - Create a new list 'temp_list' = [1, 2, 3].
#    - Clear all elements from 'temp_list'.

# Your code here:
temp_list = [1, 2, 3]
temp_list.clear()
print(f"temp_list after clear(): {temp_list}")

# --- Section 5: List Functions ---

print("\n--- Section 5: List Functions ---")

# 5.1 `len()`:
#    - Find and print the number of elements in 'combined_list'.

# Your code here:
length_combined_list = len(combined_list)
print(f"Length of combined_list: {length_combined_list}")

# 5.2 `count()`:
#    - Count and print the number of times the number 20 appears in 'combined_list'.

# Your code here:
count_of_20 = combined_list.count(20)
print(f"Count of 20 in combined_list: {count_of_20}")

# 5.3 `index()`:
#    - Find and print the index of the first occurrence of the number 40 in 'combined_list'.

# Your code here:
if 40 in combined_list:
    index_of_40 = combined_list.index(40)
    print(f"Index of 40 in combined_list: {index_of_40}")
else:
    print("40 is not in combined_list.")

# 5.4 `sort()`:
#    - Create a list 'unsorted_list' = [5, 1, 4, 2, 8].
#    - Sort 'unsorted_list' in ascending order (in-place).
#    - Sort 'unsorted_list' in descending order (in-place).

# Your code here:
unsorted_list = [5, 1, 4, 2, 8]
unsorted_list.sort()
print(f"Sorted (ascending) unsorted_list: {unsorted_list}")
unsorted_list.sort(reverse=True)
print(f"Sorted (descending) unsorted_list: {unsorted_list}")

# 5.5 `sorted()`:
#    - Create a list 'original_list' = [3, 1, 4, 1, 5, 9].
#    - Create a new sorted list 'ascending_sorted' using `sorted()` without modifying 'original_list'.
#    - Create another new sorted list 'descending_sorted' using `sorted()` in reverse order.

# Your code here:
original_list = [3, 1, 4, 1, 5, 9]
ascending_sorted = sorted(original_list)
descending_sorted = sorted(original_list, reverse=True)

print(f"Original list: {original_list}")
print(f"Ascending sorted list (using sorted()): {ascending_sorted}")
print(f"Descending sorted list (using sorted()): {descending_sorted}")

# --- Section 6: List Comprehension ---

print("\n--- Section 6: List Comprehension ---")

# 6.1 Basic List Comprehension:
#    - Use list comprehension to create a new list 'squares' containing the square of each number in 'my_list'.

# Your code here:
squares = [x**2 for x in my_list]
print(f"Squares of elements in my_list: {squares}")

# 6.2 List Comprehension with Condition:
#    - Use list comprehension to create a new list 'even_numbers' containing only the even numbers from 'original_list'.

# Your code here:
even_numbers = [x for x in original_list if x % 2 == 0]
print(f"Even numbers from original_list: {even_numbers}")

# 6.3 Nested List Comprehension (Optional):
#    - Given a list of lists 'matrix' = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#      use nested list comprehension to flatten it into a single list 'flattened_matrix'.

# Your code here:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [number for row in matrix for number in row]
print(f"Flattened matrix: {flattened_matrix}")

# --- Section 7: Advanced List Operations (Optional) ---

print("\n--- Section 7: Advanced List Operations (Optional) ---")

# 7.1 Using Lists as Stacks (LIFO):
#    - Create a list 'stack' = [10, 20, 30].
#    - "Push" the element 40 onto the stack (append).
#    - "Pop" the last element from the stack and print it.
#    - "Pop" the last element again and print it.

# Your code here:
stack = [10, 20, 30]
stack.append(40)
print(f"Stack after push(40): {stack}")
popped_item1 = stack.pop()
print(f"Popped item 1: {popped_item1}, updated stack: {stack}")
popped_item2 = stack.pop()
print(f"Popped item 2: {popped_item2}, updated stack: {stack}")

# 7.2 Using Lists as Queues (FIFO - inefficient for large queues):
#    - Create a list 'queue' = ['a', 'b', 'c'].
#    - "Enqueue" the element 'd' (append).
#    - "Dequeue" the first element from the queue and print it (using `pop(0)`).
#    - "Dequeue" the first element again and print it.
#    - Note: For efficient queue implementations, consider using `collections.deque`.

# Your code here:
queue = ['a', 'b', 'c']
queue.append('d')
print(f"Queue after enqueue('d'): {queue}")
dequeued_item1 = queue.pop(0)
print(f"Dequeued item 1: {dequeued_item1}, updated queue: {queue}")
dequeued_item2 = queue.pop(0)
print(f"Dequeued item 2: {dequeued_item2}, updated queue: {queue}")

# 7.3 Copying Lists:
#    - Create a list 'original' = [1, 2, [3, 4]].
#    - Create a shallow copy 'shallow' using slicing.
#    - Create a deep copy 'deep' using `copy.deepcopy()`.
#    - Modify the nested list in 'original' (e.g., `original[2][0] = 5`).
#    - Print 'original', 'shallow', and 'deep' to observe the difference.

# Your code here:
import copy

original = [1, 2, [3, 4]]
shallow = original[:]
deep = copy.deepcopy(original)

original[2][0] = 5

print(f"Original list: {original}")
print(f"Shallow copy: {shallow}")
print(f"Deep copy: {deep}")
# Explanation: Shallow copy shares references to nested objects, so changes in
# original's nested list affect the shallow copy. Deep copy creates entirely
# independent copies of all objects.

print("\n--- End of Python Lists Assignment ---")