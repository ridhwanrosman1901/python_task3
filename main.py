'''
Task 1: Tuples

Creating Tuples:
Create a tuple called fruits containing the following elements: "apple", "banana", "cherry", "date".
Print the first and last element of the tuple.
'''
fruits = ("apple", "banana", "cherry", "date")
print(fruits[0], fruits[3])

'''
Tuple Operations:
Create a new tuple numbers with values (1, 2, 3, 4, 5).
Use tuple unpacking to assign the first two elements of numbers to variables a and b, and the remaining elements to a variable rest.
Print a, b, and rest.
'''
num = (1, 2, 3, 4, 5)
a, b, *rest = num
print(a)
print(b)
print(rest)

'''
Tuple Immutability:
Try to change the second element of the fruits tuple to "blueberry". Write down what happens and why.
'''
updated_fruits = list(fruits)
updated_fruits[1] = "blueberry"
print(updated_fruits)

'''
Creating Sets:
Create a set called colors with the elements "red", "green", "blue", "yellow".
Add the color "purple" to the set.
'''
colors = {"red", "green", "blue", "yellow"}
colors.add("purple")
print(colors)
'''
Set Operations:
Create another set called primary_colors containing "red", "blue", and "yellow".
Find the intersection of colors and primary_colors.
Find the union of colors and primary_colors.
Find the difference between colors and primary_colors.
'''
primary_colors = {"red", "blue", "yellow"}
print(colors & primary_colors)
print(colors | primary_colors)
print(colors - primary_colors)

'''
Set Membership:
Check if "green" is in primary_colors. Print the result.
Check if "orange" is not in colors. Print the result.
'''
check_green = "green" in primary_colors
print(check_green)
check_orange = "orange" not in colors
print(check_orange)
'''
Task 3: Dict

Creating Dictionaries:
Create a dictionary called student_grades with the following key-value pairs:"Alice": 85
"Bob": 90
"Charlie": 78
"Diana": 92
Print the grade of "Bob".
'''
student_grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92
}
print(student_grades["Bob"])
'''
Dictionary Operations:
Add a new student "Eve" with a grade of 88 to the dictionary.
Update "Alice"'s grade to 95.
Remove "Charlie" from the dictionary.
Print the updated dictionary.
'''
student_grades["Eve"] = 88
student_grades["Alice"] = 95
del student_grades["Charlie"]
print(student_grades)
'''
Looping Through a Dictionary:
Loop through the student_grades dictionary and print each student's name and grade in the format "Student: [name], Grade: [grade]".
'''
for student, grade in student_grades.items():
    print(f"Student: {student}, Grade: {grade}")