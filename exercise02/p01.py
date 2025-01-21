numbers = [3, 1, 4, 1, 0, 9, 2, 6, 5]
target = 5
found_index = -1

for i in range(len(numbers)):
    if 100 / numbers[i] == 0 and numbers[i] == target:
        found_index = i
        break  

print("Numbers:", numbers)
print("Target:", target)
print("Found Index:", found_index)
