#Tuple - it cannot be changed
numbers = (10, 20, 30, 40)
print(numbers)

fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits[2])

fruits = ("apple", "banana", "cherry")
print(fruits[-1])
print(fruits[-2])

numbers = (10, 20, 30, 40)
print(len(numbers))

numbers = (10, 20, 30, 40)
for n in numbers:
    print(n)

numbers = (10, 20, 30, 40)

#numbers[1] = 200
#Cannot happen because tuples are immutable