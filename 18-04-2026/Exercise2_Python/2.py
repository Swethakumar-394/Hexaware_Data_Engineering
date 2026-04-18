# Exercise 2 — TXT File (Numbers Dataset)

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

print("All numbers:", numbers)

print("Sum of all numbers:", sum(numbers))
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))

count_greater_than_50 = 0
for num in numbers:
    if num > 50:
        count_greater_than_50 += 1

print("Count of numbers greater than 50:", count_greater_than_50)