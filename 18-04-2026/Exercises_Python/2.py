#Frequency Counter

numbers = [10, 20, 10, 30, 20, 10, 40]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency count:", freq)
