# Python For Loop Assignment

# Task 1: Print numbers from 1 to 10 excluding 5
print("Task 1")
for i in range(1, 11):
    if i != 5:
        print(i)

# Task 2: Print each string in uppercase
print("\nTask 2")

def print_uppercase(words):
    for word in words:
        print(word.upper())

words = ["python", "java", "html"]
print_uppercase(words)

# Task 3: Sum of even numbers in a list
print("\nTask 3")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for num in numbers:
    if num % 2 == 0:
        total += num

print("Sum of even numbers =", total)

# Task 4: Print dictionary key-value pairs
print("\nTask 4")

student = {
    "Name": "Tejaswi",
    "Age": 22,
    "Course": "Python"
}

for key, value in student.items():
    print(key, ":", value)

# Task 5: First 10 Fibonacci numbers
print("\nTask 5")

a = 0
b = 1

for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c

# Task 6: Average of exam scores
print("\nTask 6")

scores = [80, 85, 90, 75, 95]
total = 0

for score in scores:
    total += score

average = total / len(scores)

print("Average Score =", average)

# Task 7: Print a 5x5 matrix (1 to 25)
print("\nTask 7")

num = 1

for i in range(5):
    for j in range(5):
        print(num, end=" ")
        num += 1
    print()