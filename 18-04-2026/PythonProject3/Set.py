#SET
numbers = {10, 20, 30, 40}
print(numbers)

#It will remove the duplicates
numbers = {10, 10,20, 20, 30, 40}
print(numbers)

#List to set
numbers = [10, 20, 30, 40, 50]
unique_numbers = set(numbers)
print(unique_numbers)

#Add
numbers = {10, 20, 30, 40, 50}
numbers.add(40)
print(numbers)

#Update
numbers = {10, 20, 30, 40}
numbers.update([30, 40, 50])
print(numbers)

#Union
set1 = {10, 20, 30}
set2 = {30, 40, 50}
result = set1.union(set2)
print(result)

result = set1.difference(set2)
print(result)

result = set2.difference(set1)
print(result)

result = set1.intersection(set2)
print(result)