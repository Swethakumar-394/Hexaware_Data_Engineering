#Insert
#from List import fruits

numbers = [10, 20, 30, 40, 50]
numbers.insert(2, 60)
print(numbers)

#Remove
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)

#Remove Last Element
numbers.pop()
print(numbers)
print(len(numbers))

numbers = [10, 20, 30, 40]
for num in numbers:
    print(num)

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("banana is present")


